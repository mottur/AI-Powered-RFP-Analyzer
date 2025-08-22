"""
Module for extracting and chunking text from PDF documents.
"""

import fitz     # PyMuPDF
import re


def _clean_text(text: str) -> str:
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

def _is_heading(line_text, fontnames, x_positions, line_index=None, previous_line=None) -> bool:
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

def _split_heading_id(h_id) -> tuple:
    """Splits a heading ID like '1.' or 'A)' into its core and delimiter."""
    match = re.match(r"^([A-Za-z]|\d+)([.)])", h_id)
    return (match.group(1), match.group(2)) if match else ("", "")

def _get_pattern_type(id_core) -> str:
    """Classifies the heading ID core into a pattern type."""
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

def _pattern_rank(pat) -> int:
    """Ranks pattern types for hierarchy determination."""
    order = ['upper', 'digit', 'lower', 'roman', 'other']
    return order.index(pat) if pat in order else len(order)

def chunk_text(pdf_bytes: bytes) -> list:
    """
    Extracts and chunks text from a PDF into sections based on detected headings.
    Each chunk is a dictionary with keys: id, title, body, page, parent_id.
    """
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    chunks = []
    stack = []

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

                if _is_heading(line_text, fontnames, x_positions):
                    # Save previous chunk
                    if current_chunk:
                        current_chunk["body"] = _clean_text(current_chunk["body"])
                        chunks.append(current_chunk)

                    heading_match = re.match(r"^((?:[A-Za-z]|\d+)[.)])\s*", line_text)
                    if heading_match:
                        heading_id = heading_match.group(1)
                        heading_title = line_text[heading_match.end():].strip()
                    else:
                        heading_id = ""
                        heading_title = line_text.strip()

                    id_core, delim = _split_heading_id(heading_id)
                    current_pattern = _get_pattern_type(id_core)

                    # Determine parent from stack
                    parent_id = None
                    while stack:
                        top_id_core, _ = _split_heading_id(stack[-1]["id"])
                        top_pattern = _get_pattern_type(top_id_core)
                        if _pattern_rank(current_pattern) > _pattern_rank(top_pattern):
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
        current_chunk["body"] = _clean_text(current_chunk["body"])
        chunks.append(current_chunk)

    doc.close()
    return chunks