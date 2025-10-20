"""
FastAPI application code for the AI-Powered RFP Analyzer.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from api import classification, validation, summarization
from utils.cleanup_mlflow import cleanup_old_runs
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
from core.shared import verbose, logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        if verbose:
            logger.info("Running MLflow cleanup...")
        cleanup_old_runs(experiment_name="rfp_analyzer", keep_last_n=10, dry_run=False)
        if verbose:
            logger.info("MLflow cleanup completed.")
    except Exception as e:
        if verbose:
            logger.info(f"MLflow cleanup failed: {e}")

    yield

app = FastAPI(lifespan=lifespan)
app.mount("/plots", StaticFiles(directory="plots"), name="plots")

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
    return {"message": "Welcome to APRA, the AI-Powered RFP Analyzer Backend!"}

app.include_router(classification.router, prefix="/classification", tags=["classification"])
app.include_router(validation.router, prefix="/validation", tags=["validation"])
app.include_router(summarization.router, prefix="/summarization", tags=["summarization"])