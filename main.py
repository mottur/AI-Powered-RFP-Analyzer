import fitz     # PyMuPDF
import re
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

""" 
TEXT EXTRACTION ENDPOINT:
This endpoint accepts a PDF file upload and extracts clean text from it.
"""
@app.post("/extract-text/")
async def extract_pdf_text(file: UploadFile = File(...)):
    try:
        file_contents = await file.read()

        with fitz.open(stream=file_contents, filetype="pdf") as doc:
            raw_text = ""
            for page in doc:
                page_text = page.get_text("text")
                raw_text += page_text + "\n"

        # Clean the text
        cleaned_text = clean_text(raw_text)

        return JSONResponse(content={"text": cleaned_text})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

def clean_text(text: str) -> str:
    """
    Cleans extracted text by:
    - Removing excessive whitespace within lines
    - Removing empty lines (e.g. "\n\n\n")
    - Stripping leading/trailing spaces from lines
    """
    text = re.sub(r'[ \t]+', ' ', text)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    cleaned_text = "\n".join(lines)
    return cleaned_text