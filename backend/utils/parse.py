"""
Utility functions for processing LLM inputs and outputs.
"""

from core.shared import verbose, logger, TOKEN_LIMIT
from math import floor
import re
import json


def safe_json_loads(text: str):
    """
    Attempts to safely parse a string that looks like JSON.
    Fixes common LLM issues like smart quotes, trailing commas, and missing closing brackets/braces.
    """
    if not text or not isinstance(text, str):
        raise ValueError("Input is empty or not a string.")

    text = text.strip()

    # Remove everything before first ``` and after last ```
    match = re.search(r"```(?:json)?\s*(.*?)\s*```", text, flags=re.IGNORECASE | re.DOTALL)
    if match:
        text = match.group(1)
    else:
        # No fences found; just try the raw text
        text = text

    # Normalize quotes
    text = text.replace("“", '"').replace("”", '"').replace("’", "'")

    # Fix unclosed braces/brackets if needed
    text = _fix_unclosed_brackets(text)

    text = text.strip()

    # Remove trailing commas before closing braces/brackets
    text = re.sub(r",\s*([\]}])", r"\1", text)

    # Load text as json dict
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {e}") from e
    
def _fix_unclosed_brackets(text: str) -> str:
    """
    Adds missing closing brackets/braces if counts don't match.
    """
    open_braces = text.count("{")
    close_braces = text.count("}")
    open_brackets = text.count("[")
    close_brackets = text.count("]")
    text += "}" * max(open_braces - close_braces, 0)
    text += "]" * max(open_brackets - close_brackets, 0)
    return text
    
def truncate_categories(
    categories: dict,
    max_tokens: int = TOKEN_LIMIT
) -> dict:
    """
    Truncates sections of each category such that:
    - All categories are included
    - Initial token budget is max_tokens / N
    - Leftover budget is redistributed to categories that can use more
    - If total tokens are already under the limit, returns input unchanged
    """
    # Check total tokens to see if truncation is needed
    total_estimated_tokens = 0
    for category_name, category_data in categories.items():
        sections = category_data.get("sections", [])
        for section in sections:
            total_estimated_tokens += estimate_tokens(section)

    if total_estimated_tokens <= max_tokens:
        return categories

    num_categories = len(categories)
    base_budget = floor(max_tokens / num_categories)

    token_usage = 0
    truncated_result = []

    # Truncate each category to base_budget
    for category_name, category_data in categories.items():
        sections = category_data.get("sections", [])
        added_sections = []
        used_tokens = 0

        for section in sections:
            section_tokens = estimate_tokens(section)
            if used_tokens + section_tokens > base_budget:
                break
            added_sections.append(section)
            used_tokens += section_tokens

        token_usage += used_tokens
        truncated_result.append({
            "name": category_name,
            "sections": added_sections,
            "remaining_sections": sections[len(added_sections):]
        })

    # Redistribute leftover tokens
    remaining_tokens = max_tokens - token_usage
    while remaining_tokens > 0:
        updated = False
        expandable = [cat for cat in truncated_result if cat["remaining_sections"]]
        if not expandable:
            break

        for cat in expandable:
            next_section = cat["remaining_sections"][0]
            section_tokens = estimate_tokens(next_section)

            if section_tokens <= remaining_tokens:
                cat["sections"].append(next_section)
                cat["remaining_sections"].pop(0)
                remaining_tokens -= section_tokens
                token_usage += section_tokens
                updated = True

        if not updated:
            break  # Can't fit more

    # Build final output dictionary
    final_result = {}
    for cat in truncated_result:
        final_result[cat["name"]] = {
            "sections": cat["sections"]
        }

    return final_result

def split_chunks(chunks: list[dict], max_tokens: int = TOKEN_LIMIT) -> list[list[dict]]:
    """
    Splits the input chunks into smaller segments based on a rough token estimation.
    """
    segments = []
    current_segment = []
    current_token_count = 0

    for chunk in chunks:
        chunk_tokens = estimate_tokens(chunk)

        # If this chunk would exceed the max, start a new segment
        if current_token_count + chunk_tokens > max_tokens:
            if current_segment:
                segments.append(current_segment)
            current_segment = [chunk]
            current_token_count = chunk_tokens
        else:
            current_segment.append(chunk)
            current_token_count += chunk_tokens

    # Add the final segment
    if current_segment:
        segments.append(current_segment)

    return segments


def estimate_tokens(item: dict | str) -> int:
    """
    Roughly estimates the number of tokens in a dictionary, including keys and JSON formatting.
    """
    if isinstance(item, dict):
        json_str = json.dumps(item, ensure_ascii=False)
    else:
        json_str = item
    # 1 token ≈ 4 characters heuristic
    return len(json_str) // 4