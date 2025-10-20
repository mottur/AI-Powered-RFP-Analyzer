"""
API endpoints for training and using the SetFit Transformer model.
"""

from fastapi import APIRouter, Form, File, UploadFile
from fastapi.responses import JSONResponse
from typing import Optional
from threading import Thread
from uuid import uuid4
from services.classifier import classify_and_tag, train_classifier
from services.extractor import chunk_text
from core.process_state import ProcessState
from services.session_store import store_session
from core.shared import EXTRACTED_JSON_PATH, LABELED_JSON_PATH, SYNTHETIC_JSON_PATH, verbose, logger
import json
import random


router = APIRouter()
_training_state = ProcessState()


""" 
CLASSIFIER TRAINING ENDPOINT:
This endpoint trains the classifier on provided data.
"""
@router.post("/train/")
async def train_model(option: str = Form("useExisting"), files: Optional[list[UploadFile]] = File(None)) -> JSONResponse:
    """
    Trains the classifier on provided data.
    """
    # See if a training job is already running
    if _training_state.is_busy():
        return JSONResponse(status_code=409, content={"status": "busy", "message": "Training already in progress."})
    
    # If not busy, start training
    _training_state.start()

    file_data = []
    if option == "customPdfs":
        if not files:
            return JSONResponse(status_code=400, content={"error": "No files provided for customPdfs option."})
        for file in files:
            try:
                file_contents = await file.read()
                file_data.append({
                    "filename": file.filename,
                    "content": file_contents
                })
            except Exception as e:
                logger.exception("Error reading uploaded pdf file(s): " + str(e))
                return JSONResponse(status_code=500, content={"error": "Error reading uploaded pdf file(s): " + str(e)})
            
    elif option == "customJson":
        if not files or len(files) != 1:
            return JSONResponse(status_code=400, content={"error": "A single JSON file must be provided for customJson option."})
        try:
            file_contents = await files[0].read()
            file_data.append({
                "filename": files[0].filename,
                "content": file_contents
            })
        except Exception as e:
            logger.exception("Error reading uploaded json file: " + str(e))
            return JSONResponse(status_code=500, content={"error": "Error reading uploaded json file: " + str(e)})

    # Launch the training task in a background thread
    thread = Thread(target=_background_train_model, args=(option, file_data,))
    thread.start()

    return JSONResponse(status_code=202, content={"status": "pending", "message": "Training started."})

def _background_train_model(option: str, file_data: Optional[list[dict]]) -> JSONResponse:
    """
    Background task to train the classifier.
    """
    try:
        if option == "customPdfs":
            texts = []
            for file in file_data:
                try:
                    sections = chunk_text(file["content"])
                    texts.extend(sections)
                    if verbose:
                        logger.info(f"Extracted {len(sections)} sections from {file['filename']}.")

                except Exception as e:
                    _training_state.finish("Error chunking text: " + str(e))
                    return
            try:
                with open(EXTRACTED_JSON_PATH, 'w') as json_file:
                    json.dump(texts, json_file, indent=4)
                if verbose:
                    logger.info(f"Saved extracted sections to extracted.json.")
            except Exception as e:
                _training_state.finish("Error saving extracted chunks to json file: " + str(e))
                if verbose:
                    logger.exception("Error saving extracted chunks to json file: " + str(e))
                return
            
            _training_state.finish(chunks=texts)
            return
        
        elif option == "customJson":
            try:
                file = file_data[0]
                categories = json.loads(file["content"].decode("utf-8"))
                if verbose:
                    logger.info(f"Loaded custom json file {file['filename']} for training.")
            except Exception as e:
                _training_state.finish("Error loading custom json file: " + str(e))
                if verbose:
                    logger.exception("Error loading custom json file: " + str(e))
                return

        elif option == "useExisting":
            try:
                with open(LABELED_JSON_PATH, 'r') as json_file:
                    categories = json.load(json_file)
                if verbose:
                    logger.info(f"Loaded labeled.json for training.")
            except Exception as e:
                _training_state.finish("Error loading existing json file: " + str(e))
                if verbose:
                    logger.exception("Error loading existing json file: " + str(e))
                return
            
        # Add synthetic data
        try:
            with open(SYNTHETIC_JSON_PATH, 'r') as json_file:
                synthetic = json.load(json_file)
            for cat in categories:
                categories[cat]["sections"].extend(synthetic[cat]["sections"])
            if verbose:
                logger.info("Loaded synthetic data.")
        except Exception as e:
            _training_state.finish("Error loading synthetic data from json file: " + str(e))
            if verbose:
                logger.exception("Error loading synthetic data from json file: " + str(e))
            return
    
        # Split into train and eval sets
        try:
            train_texts = []
            eval_texts = []
            for cat in categories:
                train_samples = random.sample(categories[cat]["sections"], 12)
                eval_samples = [item for item in categories[cat]["sections"] if item not in train_samples]
                train_texts.extend(train_samples)
                eval_texts.extend(eval_samples)
            if verbose:
                logger.info("Split into train and eval datasets.")
        except Exception as e:
            _training_state.finish("Error splitting data into train and eval datasets: " + str(e))
            if verbose:
                logger.exception("Error splitting data into train and eval datasets: " + str(e))
            return
        
        # Train the classifier
        try:
            ttexts = [sec['title'] + "\n" + sec['body'] for sec in train_texts]
            tlabels = [sec['true_label'] for sec in train_texts]
            etexts = [sec['title'] + "\n" + sec['body'] for sec in eval_texts]
            elabels = [sec['true_label'] for sec in eval_texts]
            metrics = train_classifier(ttexts, tlabels, etexts, elabels)
            if verbose:
                logger.info("Metrics: %s", metrics)
            _training_state.finish()
        except Exception as e:
            _training_state.finish("Error training classifier: " + str(e))
            if verbose:
                logger.exception("Error training classifier: " + str(e))
    
    except Exception as e:
        _training_state.finish("Unexpected error during training: " + str(e))
        if verbose:
            logger.exception("Unexpected error during training: " + str(e))
    
@router.get("/status/")
async def get_training_status() -> JSONResponse:
    """
    Gets the current status of the training process.
    """
    if _training_state.is_busy():
        return JSONResponse(status_code=202, content={
            "status": "pending",
            "message": "Training in progress."
        })

    if _training_state.get_status().get("error"):
        return JSONResponse(status_code=500, content={
            "status": "failed",
            "message": "Training failed.",
            "error": _training_state.get_status().get("error")
        })
    
    if _training_state.get_status().get("chunks"):
        return JSONResponse(content={
            "status": "complete",
            "message": "Extraction complete.",
            "chunks": _training_state.get_status().get("chunks")
        })

    return JSONResponse(content={
        "status": "complete",
        "message": "Training complete."
    })


""" 
TEXT EXTRACTION & CLASSIFICATION ENDPOINT:
This endpoint accepts a PDF file upload and extracts clean text from it.
It then chunks the text into sections and classifies them.
"""
@router.post("/")
async def classify_text(file: UploadFile = File(...)) -> JSONResponse:
    """
    Extracts text from the uploaded PDF, chunks it, classifies the chunks, tags keywords, 
    and stores the session.
    """
    try:
        file_contents = await file.read()
        sections = chunk_text(file_contents)
        categories = classify_and_tag(sections)
        session_id = str(uuid4())
        store_session(session_id, categories)

        try:
            with open(EXTRACTED_JSON_PATH, 'w') as json_file:
                json.dump(categories, json_file, indent=4)
            if verbose:
                logger.info(f"Saved extracted sections to extracted.json.")
        except Exception as e:
            if verbose:
                logger.exception("Error saving extracted chunks to json file: " + str(e))
            return JSONResponse(status_code=500, content={"error": "Error saving extracted chunks to json file: " + str(e)})
        
        return JSONResponse(content={"session_id": session_id, "categories": categories})
    except Exception as e:
        if verbose:
            logger.exception("Failed to extract pdf text: " + str(e))
        return JSONResponse(status_code=500, content={"error": "Failed to extract pdf text: " + str(e)})