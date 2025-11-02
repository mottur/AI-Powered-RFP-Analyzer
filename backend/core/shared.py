"""
Shared constants and variables for the backend application.
"""
import logging


LABELS = {
    "Scope": "This section describes the scope of the project, including project goals, boundaries, assumptions, and background context.",
    "Deliverables": "This section lists the deliverables or tangible outputs the offeror/contractor is required to provide, including documentation.",
    "Company Info": "This section provides information about the offeror/contractor, including qualifications, past experience, and mission.",
    "Timeline": "This section outlines the timeline, including the length of the contract, deadlines, project start and end dates, and other key milestone schedules.",
    "Technologies": "This section specifies the tech stack - the environment, technologies, platforms, software, or tools that will be used or required for the project.",
}

EXTRACTED_JSON_PATH = "json_files/extracted.json"
SYNTHETIC_JSON_PATH = "json_files/synthetic.json"
LABELED_JSON_PATH = "json_files/labeled.json"

TOKEN_LIMIT = 7500  # Token limit for requests to Llama 3 70B API

verbose = True      # Enables print statements for debugging if True

logger = logging.getLogger("rfp_app")
logger.setLevel(logging.INFO)