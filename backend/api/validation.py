"""
API endpoints for validation of labels using an LLM (Llama 3 70B).
"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from threading import Thread
from services.prompter import validate_extraction
from core.process_state import ProcessState
from core.shared import LABELS, LABELED_JSON_PATH, verbose, logger
from utils.parse import safe_json_loads, split_chunks
import json
import time


router = APIRouter()
_validation_state = ProcessState()

""" 
VALIDATION ENDPOINT:
This endpoint classifies the given chunks using an LLM for validation.
"""
@router.post("/")
async def validate(chunks: list[dict]) -> JSONResponse:
    """
    Validates the given chunks using an LLM.
    """
    # See if a validation job is already running
    if _validation_state.is_busy():
        if verbose:
            logger.info("Validation request rejected: already in progress.")

        return JSONResponse(status_code=409, content={"status": "busy", "message": "Validation by LLM already in progress."})
    
    # If not busy, start validation
    _validation_state.start()

    # Launch the validation task in a background thread
    thread = Thread(target=_background_validate, args=(chunks,))
    thread.start()

    return JSONResponse(status_code=202, content={"status": "pending", "message": "Validation started."})
    
def _background_validate(chunks: list[dict]):
    """
    Background task to validate chunks using an LLM.
    """
    try:
        if verbose:
            logger.info("Starting LLM validation...")

        # Split chunks into manageable segments
        segmented_chunks = split_chunks(chunks)
        all_labeled_chunks = []

        for i, segment in enumerate(segmented_chunks):
            time.sleep(2)
            if verbose:
                logger.info(f"Validating segment {i+1}/{len(segmented_chunks)}...")

            result = validate_extraction(segment)

            # Handle string result from LLM and safely parse
            if isinstance(result, str):
                parsed = safe_json_loads(result)
            else:
                parsed = result  # already parsed

            if not isinstance(parsed, list):
                raise ValueError("Parsed validation result is not a list.")

            all_labeled_chunks.extend(parsed)

        # Save all labeled chunks
        import asyncio
        asyncio.run(save_labeled_chunks(all_labeled_chunks))

        _validation_state.finish()
        if verbose:
            logger.info("Validation complete.")

    except Exception as e:
        _validation_state.finish("Failed to validate extraction using LLM: " + str(e))
        if verbose:
            logger.exception("Failed to validate extraction using LLM: " + str(e))

    
@router.get("/status/")
async def get_validation_status() -> JSONResponse:
    """
    Gets the current status of the validation process.
    """
    if _validation_state.is_busy():
        return JSONResponse(status_code=202, content={
            "status": "pending",
            "message": "Validation still running."
        })

    if _validation_state.get_status().get("error"):
        return JSONResponse(status_code=500, content={
            "status": "failed",
            "message": "Validation failed.",
            "error": _validation_state.get_status().get("error")
        })

    return JSONResponse(content={
        "status": "complete",
        "message": "Validation is complete."
    })

""" 
SAVE LABELS ENDPOINT:
This endpoint saves LLM- or manually-generated true labels to file.
"""
@router.post("/labeled-chunks/")
async def save_labeled_chunks(chunks: list[dict]) -> JSONResponse:
    """
    Saves the labeled chunks to a JSON file.
    """
    try:
        categories = {label: {"sections": []} for label in LABELS}

        for sec in chunks:
            label = sec.get("true_label")
            if label and label in categories:
                categories[label]["sections"].append(sec)

        # Save labeled data
        with open(LABELED_JSON_PATH, 'w') as json_file:
            json.dump(categories, json_file, indent=4)
        if verbose:
            logger.info("Saved labeled chunks to labeled.json.")
        return JSONResponse(content={"message": "Labels successfully saved."})
    except Exception as e:
        if verbose:
            logger.exception("Failed to save labels: " + str(e))
        return JSONResponse(status_code=500, content={"error": "Failed to save labels: " + str(e)})
    