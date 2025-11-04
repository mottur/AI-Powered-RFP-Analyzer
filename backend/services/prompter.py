"""
Module for prompting the LLM (Llama 3 70B) for both validation and summarization of chunks
classified into categories using LLM.
Model: https://openrouter.ai/meta-llama/llama-3.3-70b-instruct:free
"""

import requests
import json
import os
from core.shared import LABELS, verbose, logger
from utils.parse import estimate_tokens
from dotenv import load_dotenv
from pathlib import Path


# Load the .env file from the project root
env_path = Path(__file__).resolve().parents[2] / '.env'
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv('API_KEY')

if not API_KEY:
    raise ValueError("No API_KEY found in environment variables")

# Format for prompting the LLM
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "HTTP-Referer": "AI-Powered-RFP-Analyzer",
    "Content-Type": "application/json",
}

data = {
    "model": "meta-llama/llama-3.3-70b-instruct:free",
    "messages": [
        {"role": "system", "content": ""},
        {"role": "user", "content": ""}
    ]
}


def validate_extraction(chunks: list[dict]) -> str:
    """
    Validates the chunking and classification of sections by the SetFit Transformer model.
    """
    labels = "\n".join(f"{key}: {value}" for key, value in LABELS.items())
    msg = "You are a helpful assistant for classifying chunks of text from Request for Proposal (RFP) " \
          "documents. Given a chunk of text from an RFP, determine which category it best fits from the " \
          "following categories: " + ", ".join(LABELS.keys())
    data["messages"][0]["content"] = msg
    data["messages"][1]["content"] = f"""The following json provides chunks of text from an RFP document.
        Consider the following json:\n{json.dumps(chunks)}\n
        For each chunk, decide on one of the labels, which are defined:\n{labels}\n
        If none of the labels fit, return N/A. No explanation is required.
        Return ONLY the same json with the key 'true_label' appended to each chunk, with the value being the chosen label.
    """
    result = _call_llm_endpoint(data)
    if verbose:
        logger.info("Validation result:\n" + result)
    return result


def summarize(categories: dict) -> str:
    """
    Using an LLM model, this function:
    - Summarizes the categories.
    - Suggests actionable insights or next steps.
    """
    labels = "\n".join(f"{key}: {value}" for key, value in LABELS.items())
    msg = "You are a helpful assistant for summarizing Request for Proposal (RFP) documents. " \
    "Given a category of text from an RFP, provide a detailed summary and suggest actionable " \
    "insights or next steps for responding to the RFP."
    text = {key: None for key in LABELS.keys()}
    for key in text.keys():
        text[key] = [sec["title"] + "\n" + sec["body"] for sec in categories[key]["sections"]]
    data["messages"][0]["content"] = msg
    data["messages"][1]["content"] = f"The following json provides chunks of text from an RFP document." \
                                    f"The keys are the categories, which are defined:\n{labels}\n" \
                                    f"Consider the following json:\n{str(text)}\n" \
                                    f"Provide a detailed summary of the chunks in each category based on the descriptions provided above, " \
                                    f"keeping in mind that the chunks may correspond to more than one category. " \
                                    f"Key details and specific technologies and tools in the chunks should be included in the summaries. " \
                                    f"After that, suggest actionable insights or next steps. " \
                                    f"Return ONLY a json string with the defined categories as keys, " \
                                    f"the generated summaries for each category as values, " \
                                    f"and an additional key 'Insights', which should include the generated insights and/or actionable steps as the value."
    result = _call_llm_endpoint(data)
    if verbose:
        logger.info("Summarization result:\n" + result)
    return result


def _call_llm_endpoint(data: dict) -> str:
    """
    Calls the OpenRouter API LLM endpoint with the data
    """
    input_tokens = estimate_tokens(data)
    logger.info("Input tokens: " + str(input_tokens))
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    retries = 0
    while retries < 2 and (not response.ok or response.text[:500].strip() == ""):
        if not response.ok:
            try:
                logger.exception("Issue during LLM labeling: " + response.json().get("error", {}).get("message", response.text) + " Retrying...")
            except ValueError:
                logger.exception("Issue during LLM labeling: " + response.text + " Retrying...")
        else:
            logger.exception("Issue during LLM labeling: LLM endpoint returning truncated output. Retrying...")
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        retries += 1
    if not response.ok:
        try:
            raise RuntimeError(response.json().get("error", {}).get("message", response.text))
        except ValueError:
            raise RuntimeError(response.text)
    elif response.text[:500].strip() == "":
        raise RuntimeError("LLM endpoint returning truncated output.")
    result = response.json()["choices"][0]["message"]["content"]
    return result