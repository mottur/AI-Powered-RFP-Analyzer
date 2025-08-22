import fitz     # PyMuPDF
import re
import spacy
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from transformers import pipeline
from uuid import uuid4
from collections import defaultdict

LABELS = {
    "Scope": "This section describes the scope of the project, including its goals, boundaries, assumptions, and context.",
    "Deliverables": "This section lists the deliverables or tangible outputs the contractor is expected to provide.",
    "Company Info": "This section provides background information about the offeror or bidding company.",
    "Timeline": "This section outlines the length of the contract, deadlines, project start and end dates, and other key milestone schedules.",
    "Contractor Info": "This section specifies the required qualifications, certifications, or experience of the contractor.",
}
patterns = [{"label": "IGNORE", "pattern": label} for label in LABELS.keys()]
extra_ignore_terms = ["E-Mail", "Email"]
patterns.extend([{"label": "IGNORE", "pattern": term} for term in extra_ignore_terms])
session_store = {}

app = FastAPI()
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
# "MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli"
nlp = spacy.load("en_core_web_trf")
ruler = nlp.add_pipe("entity_ruler", before="ner")
ruler.add_patterns(patterns)

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
        classify_primary_sections(sections)
        tag_keywords(sections)
        categories = consolidate_categories(sections)
        session_id = str(uuid4())
        session_store[session_id] = categories
        return JSONResponse(content={"session_id": session_id, "categories": categories})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

def clean_text(text: str) -> str:
    """
    Cleans extracted text by:
    - Removing excessive whitespace within lines
    - Removing empty lines (e.g. "\n\n\n")
    - Stripping leading/trailing spaces from lines
    - Removing common page number patterns like '1 | P a g e'
    """
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\b\d+\s*\|\s*P\s*a\s*g\s*e\b', '', text, flags=re.IGNORECASE)
    text = re.sub(r'^\s*\d+\s*$', '', text, flags=re.MULTILINE)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)

def is_heading(line_text, fontnames, x_positions, line_index=None, previous_line=None):
    """
    Determine if a line is a heading based on pattern, boldness, font, and structure.
    Protects against false positives like inline lists and 'U.S.'.
    """
    line_text_clean = line_text.strip()

    # Reject obvious false positives
    if any(variant in line_text_clean.lower() for variant in ["u.s.", "u. s.", "us fish", "us."]):
        return False

    # Must match heading pattern like '1.', 'A)', etc.
    heading_match = re.match(r'^([A-Za-z]|\d+)[.)]\s+', line_text_clean)
    if not heading_match:
        return False

    # Avoid inline-style lists: multiple numbered patterns in one line
    inline_list_hits = re.findall(r'([A-Za-z]|\d+)[.)]\s+', line_text_clean)
    if len(inline_list_hits) > 1:
        return False

    # Short headings likely to be lists (especially if all on same font)
    if len(line_text_clean.split()) <= 6 and not any("bold" in f.lower() for f in fontnames):
        return False

    # Reject lines that continue from a previous paragraph
    if previous_line:
        if previous_line["ends_with_colon"] or not previous_line["was_heading"]:
            return False

    # Finally, allow if bold or clearly left-aligned
    is_bold = any("bold" in f.lower() for f in fontnames)
    is_left_aligned = min(x_positions) < 100 if x_positions else False

    return is_bold or is_left_aligned


def chunk_text(pdf_bytes: bytes):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    chunks = []
    stack = []

    def split_heading_id(h_id):
        match = re.match(r"^([A-Za-z]|\d+)([.)])", h_id)
        return (match.group(1), match.group(2)) if match else ("", "")

    def get_pattern_type(id_core):
        roman_numerals = {'i','ii','iii','iv','v','vi','vii','viii','ix','x'}
        id_lower = id_core.lower()
        if id_core.isdigit():
            return "digit"
        elif id_core.isalpha():
            if id_core.isupper():
                return "upper"
            else:
                return "lower"
        elif id_lower in roman_numerals:
            return "roman"
        return "other"

    def pattern_rank(pat):
        order = ['upper', 'digit', 'lower', 'roman', 'other']
        return order.index(pat) if pat in order else len(order)

    current_chunk = None

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if block["type"] != 0:
                continue

            for line in block["lines"]:
                line_text = ""
                fontnames = set()
                x_positions = []

                for span in line["spans"]:
                    span_text = span["text"].strip()
                    if not span_text:
                        continue
                    line_text += span_text + " "
                    fontnames.add(span["font"])
                    x_positions.append(span["origin"][0])

                line_text = line_text.strip()
                if not line_text:
                    continue

                if is_heading(line_text, fontnames, x_positions):
                    # Save previous chunk
                    if current_chunk:
                        current_chunk["body"] = clean_text(current_chunk["body"])
                        chunks.append(current_chunk)

                    heading_match = re.match(r"^((?:[A-Za-z]|\d+)[.)])\s*", line_text)
                    if heading_match:
                        heading_id = heading_match.group(1)
                        heading_title = line_text[heading_match.end():].strip()
                    else:
                        heading_id = ""
                        heading_title = line_text.strip()

                    id_core, delim = split_heading_id(heading_id)
                    current_pattern = get_pattern_type(id_core)

                    # Determine parent from stack
                    parent_id = None
                    while stack:
                        top_id_core, _ = split_heading_id(stack[-1]["id"])
                        top_pattern = get_pattern_type(top_id_core)
                        if pattern_rank(current_pattern) > pattern_rank(top_pattern):
                            # current is child, parent is top of stack
                            parent_id = stack[-1]["id"]
                            break
                        else:
                            # same or higher level, pop
                            stack.pop()

                    current_chunk = {
                        "id": heading_id,
                        "title": heading_title,
                        "body": "",
                        "page": page_num,
                        "parent_id": parent_id,  # <-- mark parent here
                    }

                    # Push current chunk to stack
                    stack.append(current_chunk)

                else:
                    if current_chunk:
                        current_chunk["body"] += line_text + " "

    # Add last chunk
    if current_chunk:
        current_chunk["body"] = clean_text(current_chunk["body"])
        chunks.append(current_chunk)

    doc.close()
    return chunks

"""
CLASSIFICATION FUNCTIONS:
"""
def classify_section(text: str) -> str:
    hypotheses = list(LABELS.values())
    result = classifier(text, hypotheses, multi_label=True)

    # Map back to original label name
    predicted_description = result["labels"][0]
    for key, desc in LABELS.items():
        if desc == predicted_description:
            return key
    return "Unknown"

def classify_primary_sections(sections):
    for sec in sections:
        context = "This is an excerpt from a government Request for Proposal (RFP) document:\n"
        full_text = context + sec["title"] + "\n" + sec["body"]
        sec["label"] = classify_section(full_text)

def tag_keywords(sections):
    """
    Tags keywords in each section using spaCy's NER.
    """
    for sec in sections:
        full_text = sec["title"] + "\n" + sec["body"]
        doc = nlp(full_text)
        filtered_ents = [ent for ent in doc.ents if ent.label_ != "IGNORE"]
        keywords = {}
        for ent in filtered_ents:
            if ent.label_ not in keywords:
                keywords[ent.label_] = [ent.text]
            else:
                keywords[ent.label_].append(ent.text)
        sec["keywords"] = keywords

def consolidate_categories(sections):
    """
    Consolidates sections into categories based on their labels.
    """
    categories = {label: {"sections": [], "keywords": defaultdict(set)} for label in LABELS}
    for sec in sections:
        label = sec.get("label")
        if label not in categories:
            continue
        for key, values in sec.get("keywords", {}).items():
            categories[label]["keywords"][key].update(values)
        del sec["keywords"]
        categories[label]["sections"].append(sec)
    for label in categories:
        categories[label]["keywords"] = {k: list(v) for k, v in categories[label]["keywords"].items()}
    return categories

""" 
SUMMARIZATION ENDPOINT:
This endpoint summarizes the contents of the PDF file and .
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