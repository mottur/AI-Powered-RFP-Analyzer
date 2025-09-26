"""
FastAPI application code for the AI-Powered RFP Analyzer.
"""

from typing import Optional
from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from uuid import uuid4
from extraction import chunk_text
from classification import classify_and_tag, classify_manually, train_classifier
from summarization import summarize, validate_extraction
from shared import LABELS
import json
import re
import os
import random


session_store = {}

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Vite dev server
        "http://localhost:5173",  # Vite default port
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to the AI-Powered RFP Analyzer!"}

""" 
CLASSIFIER TRAINING ENDPOINT:
This endpoint trains the classifier on provided data.
"""
@app.post("/train-classifier/")
async def train_model(option: str = Form("useExisting"), files: Optional[list[UploadFile]] = File(None)) -> JSONResponse:
    if option == "customPdfs":
        if not files:
            return JSONResponse(status_code=400, content={"error": "No files provided for customPdfs option."})
        
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
        
        return JSONResponse(content={"chunks": texts})
        
        # try:
        #     categories = classify_manually(texts)
        #     with open("manual.json", 'w') as json_file:
        #         json.dump(categories, json_file, indent=4)
        #     print(f"Classified all sections manually.")
        # except Exception as e:
        #     return JSONResponse(status_code=500, content={"error": str(e)})
    
    if option == "customJson":
        if not files:
            return JSONResponse(status_code=400, content={"error": "No files provided for customJson option."})
        
        try:
            file_contents = await files[0].read()
            categories = json.loads(file_contents.decode("utf-8"))
            print(f"Loaded custom json file for training.")
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})

    if option == "useExisting":
        try:
            with open("manual.json", 'r') as json_file:
                categories = json.load(json_file)
            print(f"Loaded manual.json for training.")
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})
        
    # Add synthetic data
    try:
        with open("synthetic.json", 'r') as json_file:
            synthetic = json.load(json_file)
        for cat in categories:
            categories[cat]["sections"].extend(synthetic[cat]["sections"])
        with open("labeled.json", 'w') as json_file:
            json.dump(categories, json_file, indent=4)
        print("Loaded synthetic data.")
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
 
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
    
    try:
        ttexts = [sec['title'] + "\n" + sec['body'] for sec in train_texts]
        tlabels = [sec['true_label'] for sec in train_texts]
        etexts = [sec['title'] + "\n" + sec['body'] for sec in eval_texts]
        elabels = [sec['true_label'] for sec in eval_texts]
        metrics = train_classifier(ttexts, tlabels, etexts, elabels)
        print("Metrics: ", metrics)
        return JSONResponse(content={"metrics": metrics})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

    # if os.path.exists("extracted.json"):
    #     use_files = input("Use extracted.json file for training? ")
    # else:
    #     use_files = 'no'
    # if use_files.lower() == 'exit' or use_files.lower() == 'stop' or use_files.lower() == '':
    #     return JSONResponse(status_code=500, content={"error": "Aborted process"})
    # if use_files.lower() == 'no' or use_files.lower() == 'n':
        # texts = []
        # for file in files:
        #     try:
        #         file_contents = await file.read()
        #         sections = chunk_text(file_contents)
        #         texts.extend(sections)
        #         print(f"Extracted {len(sections)} sections from {file.filename}.")

        #     except Exception as e:
        #         return JSONResponse(status_code=500, content={"error": str(e)})
        # try:
        #     with open("extracted.json", 'w') as json_file:
        #         json.dump(texts, json_file, indent=4)
        #     print(f"Saved extracted sections to extracted.json.")
        # except Exception as e:
        #     return JSONResponse(status_code=500, content={"error": str(e)})
    # else:
    #     try:
    #         with open("extracted.json", 'r') as json_file:
    #             texts = json.load(json_file)
    #         print(f"Loaded extracted.json for training.")
    #     except Exception as e:
    #         return JSONResponse(status_code=500, content={"error": str(e)})
        
    # if os.path.exists("manual.json"):
    #     use_files = input("Use manual.json file for training? ")
    # else:
    #     use_files = 'no'
    # if use_files.lower() == 'exit' or use_files.lower() == 'stop' or use_files.lower() == '':
    #     return JSONResponse(status_code=500, content={"error": "Aborted process"})
    # if use_files.lower() == 'no' or use_files.lower() == 'n':
        # try:
        #     categories = classify_manually(texts)
        #     with open("manual.json", 'w') as json_file:
        #         json.dump(categories, json_file, indent=4)
        #     print(f"Classified all sections manually.")
        # except Exception as e:
        #     return JSONResponse(status_code=500, content={"error": str(e)})
    # else:
    #     try:
    #         with open("manual.json", 'r') as json_file:
    #             categories = json.load(json_file)
    #         print(f"Loaded manual.json for training.")
    #     except Exception as e:
    #         return JSONResponse(status_code=500, content={"error": str(e)})
    
    # if os.path.exists("labeled.json"):
    #     use_files = input("Use labeled.json file for training? ")
    # else:
    #     use_files = 'no'
    # if use_files.lower() == 'exit' or use_files.lower() == 'stop' or use_files.lower() == '':
    #     return JSONResponse(status_code=500, content={"error": "Aborted process"})
    # if use_files.lower() == 'no' or use_files.lower() == 'n':
    #     try:
    #         # categories = {label: {"sections": []} for label in LABELS}
    #         with open("synthetic.json", 'r') as json_file:
    #             synthetic = json.load(json_file)
    #         for cat in categories:
    #             categories[cat]["sections"].extend(synthetic[cat]["sections"])
    #         with open("labeled.json", 'w') as json_file:
    #             json.dump(categories, json_file, indent=4)
    #         print("Loaded synthetic data.")
    #     except Exception as e:
    #         return JSONResponse(status_code=500, content={"error": str(e)})
    # else:
    #     try:
    #         with open("labeled.json", 'r') as json_file:
    #             categories = json.load(json_file)
    #         print(f"Loaded labeled.json for training.")
    #     except Exception as e:
    #         return JSONResponse(status_code=500, content={"error": str(e)})
    
    # if os.path.exists("train.json") and os.path.exists("eval.json"):
    #     use_files = input("Use train.json and eval.json files for training? ")
    # else:
    #     use_files = 'no'
    # if use_files.lower() == 'exit' or use_files.lower() == 'stop' or use_files.lower() == '':
    #     return JSONResponse(status_code=500, content={"error": "Aborted process"})
    # if use_files.lower() == 'no' or use_files.lower() == 'n':        
    #     try:
    #         train_texts = []
    #         eval_texts = []
    #         for cat in categories:
    #             train_samples = random.sample(categories[cat]["sections"], 12)
    #             eval_samples = [item for item in categories[cat]["sections"] if item not in train_samples]
    #             train_texts.extend(train_samples)
    #             eval_texts.extend(eval_samples)
    #         with open("train.json", 'w') as json_file:
    #             json.dump(train_texts, json_file, indent=4)
    #         with open("eval.json", 'w') as json_file:
    #             json.dump(eval_texts, json_file, indent=4)
        
    #     except Exception as e:
    #         return JSONResponse(status_code=500, content={"error": str(e)})
    # else:
    #     try:
    #         with open("train.json", 'r') as json_file:
    #             train_texts = json.load(json_file)
    #         with open("eval.json", 'r') as json_file:
    #             eval_texts = json.load(json_file)
    #         print(f"Loaded train.json and eval.json for training.")
    #     except Exception as e:
    #         return JSONResponse(status_code=500, content={"error": str(e)})
    
    # try:
    #     ttexts = [sec['title'] + "\n" + sec['body'] for sec in train_texts]
    #     tlabels = [sec['true_label'] for sec in train_texts]
    #     etexts = [sec['title'] + "\n" + sec['body'] for sec in eval_texts]
    #     elabels = [sec['true_label'] for sec in eval_texts]
    #     metrics = train_classifier(ttexts, tlabels, etexts, elabels)
    #     return JSONResponse(content={"metrics": metrics})
    # except Exception as e:
    #     return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/save-labels/")
async def save_labeled_chunks(chunks: list[dict]) -> JSONResponse:
    try:
        categories = {label: {"sections": []} for label in LABELS}

        for sec in chunks:
            label = sec.get("true_label")
            if label and label in categories:
                categories[label]["sections"].append(sec)

        # Save labeled data
        with open("manual.json", 'w') as json_file:
            json.dump(categories, json_file, indent=4)

        return JSONResponse(content={"message": "Labels saved."})
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
    
import json
import re

def _safe_json_loads(text: str):
    """
    Attempts to safely parse a string that looks like JSON.
    Fixes common LLM issues like smart quotes and trailing commas.
    """
    try:
        # Remove surrounding markdown code fences, e.g. ```json ... ```
        text = text.strip()
        if text.startswith("```"):
            text = re.sub(r"^```(?:json)?", "", text)
            text = re.sub(r"```$", "", text)
        text = text.strip()

        # Common fixes: replace smart quotes with normal ones
        text = text.replace("“", "\"").replace("”", "\"").replace("’", "'")

        # Remove any trailing commas before closing brackets/braces
        text = re.sub(r",\s*([\]}])", r"\1", text)

        # Attempt to parse
        return json.loads(text)
    except json.JSONDecodeError as e:
        print("Failed to parse JSON:", e)
        print("Problematic content:\n", text)
        raise ValueError("LLM output could not be parsed into valid JSON.")


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
        if isinstance(summaries, str):
            summaries = _safe_json_loads(summaries)
        return JSONResponse(content={"summaries": summaries})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})