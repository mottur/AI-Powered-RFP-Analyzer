"""
API endpoints for summarizing classified categories using an LLM (Llama 3 70B).
"""

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from services.prompter import summarize
from services.session_store import load_session
from core.shared import verbose, logger
from utils.parse import safe_json_loads, truncate_categories


router = APIRouter()


""" 
SUMMARIZATION ENDPOINT:
This endpoint summarizes the contents of each category in the PDF file and suggests actionable insights or next steps.
"""
@router.post("/")
async def summarize_text(session_id: str) -> JSONResponse:
    """
    Summarizes the classified categories using an LLM.
    """
    try:
        categories = load_session(session_id)
        if not categories:
            raise HTTPException(status_code=404, detail="Session not found")
        if verbose:
            logger.info("Starting summarization...")
        categories = truncate_categories(categories)
        summaries = summarize(categories)
        if isinstance(summaries, str):
            summaries = safe_json_loads(summaries)
        if verbose:
            logger.info("Summarization complete.")
        return JSONResponse(content={"summaries": summaries})
    
    except Exception as e:
        if verbose:
            logger.exception("Summarization failed: ", e)
        return JSONResponse(status_code=500, content={"error": str(e)})