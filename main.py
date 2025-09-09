"""
FastAPI application code for the AI-Powered RFP Analyzer.
"""

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from uuid import uuid4
from extraction import chunk_text
from classification import classify_and_tag, classify_manually, train_classifier
from summarization import summarize, validate_extraction
from shared import LABELS
import json
import os
import random


session_store = {}

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the AI-Powered RFP Analyzer!"}

""" 
CLASSIFIER TRAINING ENDPOINT:
This endpoint trains the classifier on provided data.
"""
@app.post("/train-classifier/")
async def train_model(files: list[UploadFile] = File(...)) -> JSONResponse:
# async def train_model() -> JSONResponse:
    if os.path.exists("extracted.json"):
        use_files = input("Use extracted.json file for training? ")
    else:
        use_files = 'no'
    if use_files.lower() == 'exit' or use_files.lower() == 'stop' or use_files.lower() == '':
        return JSONResponse(status_code=500, content={"error": "Aborted process"})
    if use_files.lower() == 'no' or use_files.lower() == 'n':
        texts = []
        for file in files:
            try:
                file_contents = await file.read()
                sections = chunk_text(file_contents)
                texts.extend(sections)
                print(f"Extracted {len(sections)} sections from {file.filename}.")

            except Exception as e:
                return JSONResponse(status_code=500, content={"error": str(e)})
        try:
            with open("extracted.json", 'w') as json_file:
                json.dump(texts, json_file, indent=4)
            print(f"Saved extracted sections to extracted.json.")
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})
    else:
        try:
            with open("extracted.json", 'r') as json_file:
                texts = json.load(json_file)
            print(f"Loaded extracted.json for training.")
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})
        
    if os.path.exists("manual.json"):
        use_files = input("Use manual.json file for training? ")
    else:
        use_files = 'no'
    if use_files.lower() == 'exit' or use_files.lower() == 'stop' or use_files.lower() == '':
        return JSONResponse(status_code=500, content={"error": "Aborted process"})
    if use_files.lower() == 'no' or use_files.lower() == 'n':
        try:
            categories = classify_manually(texts)
            with open("manual.json", 'w') as json_file:
                json.dump(categories, json_file, indent=4)
            print(f"Classified all sections manually.")
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})
    else:
        try:
            with open("manual.json", 'r') as json_file:
                categories = json.load(json_file)
            print(f"Loaded manual.json for training.")
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})
    
    if os.path.exists("labeled.json"):
        use_files = input("Use labeled.json file for training? ")
    else:
        use_files = 'no'
    if use_files.lower() == 'exit' or use_files.lower() == 'stop' or use_files.lower() == '':
        return JSONResponse(status_code=500, content={"error": "Aborted process"})
    if use_files.lower() == 'no' or use_files.lower() == 'n':
        try:
            # categories = {label: {"sections": []} for label in LABELS}
            with open("synthetic.json", 'r') as json_file:
                synthetic = json.load(json_file)
            for cat in categories:
                categories[cat]["sections"].extend(synthetic[cat]["sections"])
            with open("labeled.json", 'w') as json_file:
                json.dump(categories, json_file, indent=4)
            print("Loaded synthetic data.")
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})
    else:
        try:
            with open("labeled.json", 'r') as json_file:
                categories = json.load(json_file)
            print(f"Loaded labeled.json for training.")
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})
    
    if os.path.exists("train.json") and os.path.exists("eval.json"):
        use_files = input("Use train.json and eval.json files for training? ")
    else:
        use_files = 'no'
    if use_files.lower() == 'exit' or use_files.lower() == 'stop' or use_files.lower() == '':
        return JSONResponse(status_code=500, content={"error": "Aborted process"})
    if use_files.lower() == 'no' or use_files.lower() == 'n':        
        try:
            train_texts = []
            eval_texts = []
            for cat in categories:
                train_samples = random.sample(categories[cat]["sections"], 12)
                eval_samples = [item for item in categories[cat]["sections"] if item not in train_samples]
                train_texts.extend(train_samples)
                eval_texts.extend(eval_samples)
            with open("train.json", 'w') as json_file:
                json.dump(train_texts, json_file, indent=4)
            with open("eval.json", 'w') as json_file:
                json.dump(eval_texts, json_file, indent=4)
        
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})
    else:
        try:
            with open("train.json", 'r') as json_file:
                train_texts = json.load(json_file)
            with open("eval.json", 'r') as json_file:
                eval_texts = json.load(json_file)
            print(f"Loaded train.json and eval.json for training.")
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})
    
    try:
        ttexts = [sec['title'] + "\n" + sec['body'] for sec in train_texts]
        tlabels = [sec['true_label'] for sec in train_texts]
        etexts = [sec['title'] + "\n" + sec['body'] for sec in eval_texts]
        elabels = [sec['true_label'] for sec in eval_texts]
        metrics = train_classifier(ttexts, tlabels, etexts, elabels)
        return JSONResponse(content={"message": "Training completed successfully.", "metrics": metrics})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

""" 
TEXT EXTRACTION ENDPOINT:
This endpoint accepts a PDF file upload and extracts clean text from it.
"""
@app.post("/extract-text/")
async def extract_pdf_text(file: UploadFile = File(...)) -> JSONResponse:
    try:
        file_contents = await file.read()
        sections = chunk_text(file_contents)
        categories, run_id = classify_and_tag(sections)
        session_id = str(uuid4())
        session_store[session_id] = categories
        try:
            with open("extracted.json", 'w') as json_file:
                json.dump(categories, json_file, indent=4)
            print(f"Saved extracted sections to extracted.json.")
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})
        return JSONResponse(content={"session_id": session_id, "categories": categories, "mlflow_run_id": run_id})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    
""" 
VALIDATION ENDPOINT:
This endpoint validates extraction logic through prompt engineering.
"""
@app.post("/validate-extraction/")
async def validate(session_id: str) -> JSONResponse:
    try:
        categories = session_store.get(session_id)
        if not categories:
            raise HTTPException(status_code=404, detail="Session not found: make sure to extract text first.")
        categories = validate_extraction(categories)
        return JSONResponse(content={"categories": categories})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

""" 
SUMMARIZATION ENDPOINT:
This endpoint summarizes the contents of each category in the PDF file and suggests actionable insights or next steps.
"""
@app.post("/summarize-text/")
async def summarize_text(session_id: str) -> JSONResponse:
    try:
        categories = session_store.get(session_id)
        if not categories:
            raise HTTPException(status_code=404, detail="Session not found")
        summaries = summarize(categories)
        return JSONResponse(content={"summaries": summaries})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})