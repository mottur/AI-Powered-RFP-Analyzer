"""
FastAPI application code for the AI-Powered RFP Analyzer.
"""

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from uuid import uuid4
from extraction import chunk_text
from classification import classify_and_tag


session_store = {}

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the AI-Powered RFP Analyzer!"}

""" 
TEXT EXTRACTION & CLASSIFICATION ENDPOINT:
This endpoint accepts a PDF file upload and extracts clean text from it, then classifies it.
"""
@app.post("/extract-text/")
async def extract_pdf_text(file: UploadFile = File(...)) -> JSONResponse:
    try:
        file_contents = await file.read()
        sections = chunk_text(file_contents)
        categories = classify_and_tag(sections)
        session_id = str(uuid4())
        session_store[session_id] = categories
        return JSONResponse(content={"session_id": session_id, "categories": categories})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

""" 
SUMMARIZATION ENDPOINT:
This endpoint summarizes the contents of each category in the PDF file, suggests actionable insights or next steps, 
and validates extraction logic through prompt engineering.
https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1
"""
@app.post("/summarize-text/")
async def summarize_text(session_id: str) -> JSONResponse:
    try:
        categories = session_store.get(session_id)
        if not categories:
            raise HTTPException(status_code=404, detail="Session not found")
        
        return JSONResponse(content={"categories": categories})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})