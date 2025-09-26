"""
Module for extracting and chunking text from PDF documents.
"""

import fitz     # PyMuPDF
import re
from collections import defaultdict
from shared import LABELS

# NUMBERED_PATTERN = r'^\b((?:[IVXLCDM]+|\d{1,2}(?!\d)|[A-Za-z](?![A-Za-z])))([.)\s])\s*'
NUMBERED_PATTERN = r'^\b((?:[IVXLCDM]+|\d{1,2}(?!\d)|[A-Za-z]))([.)]\s+|\s{2,})'

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

def _is_heading(line_text, fontnames, x_positions, previous_line=None, next_line=None, previous_x_positions=None) -> bool:
    """
    Heading detection WITHOUT left-alignment check.
    """
    line_text_clean = line_text.strip()
    if line_text_clean.startswith("o "):
        line_text_clean = line_text_clean.replace("o ", "\u2022")
    
    pattern = "blahblahblah"
    if pattern in line_text_clean:
        print(f"\n=== CHECKING HEADING: '{line_text_clean}' ===")
        if previous_line:
            print(f"  Previous: '{previous_line.strip()}'")
        if next_line:
            print(f"  Next: '{next_line.strip()}'")

    # Reject empty or very short lines
    if len(line_text_clean) < 3:
        if pattern in line_text_clean:
            print("  -> REJECT: Too short")
        return False

    # Reject common false positives
    false_positives = ["u.s.", "u. s.", "us fish", "us.", "page", "p a g e"]
    if any(fp in line_text_clean.lower() for fp in false_positives):
        if pattern in line_text_clean:
            print("  -> REJECT: False positive")
        return False

    # Reject lines that look like TOC entries
    if _looks_like_toc_line(line_text_clean):
        if pattern in line_text_clean:
            print("  -> REJECT: TOC line")
        return False

    # Ignore common heading false positives
    common_false_headings = [
        "table of contents", "contents", "index", "appendix", "appendices",
        "references", "bibliography", "glossary", "acknowledgments", "acknowledgements",
        "abstract", "executive summary", "list of figures", "list of tables",
        "footnotes", "endnotes", "copyright", "disclaimer", "preface", "foreword"
    ]
    if any(false_heading in line_text_clean.lower() for false_heading in common_false_headings):
        if pattern in line_text_clean:
            print("  -> REJECT: Common false heading")
        return False

    # Check for numbered headings pattern
    # numbered_pattern = r'^\b(?!(?<!\d)\d{2,}(?!\d))([IVXLCDM]+|\d+|[A-Z])[.)\s]\s*'
    numbered_pattern = NUMBERED_PATTERN
    numbered_match = re.match(numbered_pattern, line_text_clean, re.IGNORECASE)
    
    if numbered_match:
        if pattern in line_text_clean:
            print(f"  -> NUMBERED PATTERN FOUND: {numbered_match.groups()}")
        
        # Check for inline lists within the same line
        all_numbered_patterns = re.findall(numbered_pattern, line_text_clean, re.IGNORECASE)
        if pattern in line_text_clean:
            print(f"  All numbered patterns in line: {all_numbered_patterns}")
        
        if len(all_numbered_patterns) > 1:
            if _are_consecutive_items(all_numbered_patterns[0], all_numbered_patterns[1]):
                if pattern in line_text_clean:
                    print("  -> REJECT: Inline list detected (multiple patterns in one line)")
                return False
        
        current_id = numbered_match.group(1)
        
        # Check if this CONTINUES a list from previous line
        if previous_line:
            prev_clean = previous_line.strip()
            prev_match = re.match(numbered_pattern, prev_clean, re.IGNORECASE)
            if prev_match:
                prev_id = prev_match.group(1)
                if _are_consecutive_items(prev_id, current_id):
                    if pattern in line_text_clean:
                        print(f"  -> REJECT: Continues list from previous line ({prev_id} -> {current_id})")
                    return False
        
        # Check if this STARTS a list (only if it matches specific patterns)
        if _is_list_starter(current_id):
            # Check if next line continues this list
            if next_line:
                next_clean = next_line.strip()
                next_match = re.match(numbered_pattern, next_clean, re.IGNORECASE)
                if next_match:
                    next_id = next_match.group(1)
                    if _are_consecutive_items(current_id, next_id):
                        if pattern in line_text_clean:
                            print(f"  -> REJECT: Starts list continued on next line ({current_id} -> {next_id})")
                        return False
        
        if pattern in line_text_clean:
            print("  -> ACCEPT: Numbered heading")
        return True

    # # ACCEPT bold text
    # if has_bold:
    #     if pattern in line_text_clean:
    #         print("  -> ACCEPT: Bold text")
    #     return True

    # Check for uppercase headings
    is_uppercase = line_text_clean.isupper()
    word_count = len(line_text_clean.split())
    if pattern in line_text_clean:
        print(f"  Uppercase: {is_uppercase}, Word count: {word_count}")
    
    # ACCEPT uppercase headings
    if is_uppercase and 2 <= word_count <= 10:
        if pattern in line_text_clean:
            print("  -> ACCEPT: Uppercase heading")
        return True

    if pattern in line_text_clean:
        print("  -> REJECT: No heading pattern matched")
    return False

def _are_consecutive_items(prev_id, current_id):
    """
    Check if two heading IDs are consecutive.
    """
    # Normalize to strings for comparison
    prev_id = str(prev_id).upper()
    current_id = str(current_id).upper()
    
    try:
        # Consecutive numbers (1 → 2, 5 → 6, etc.)
        if prev_id.isdigit() and current_id.isdigit():
            return int(current_id) == int(prev_id) + 1
        
        # Consecutive letters (A → B, C → D, etc.)
        if (prev_id.isalpha() and len(prev_id) == 1 and 
            current_id.isalpha() and len(current_id) == 1):
            return ord(current_id) == ord(prev_id) + 1
        
        # Consecutive Roman numerals (I → II, II → III, IV → V, etc.)
        roman_numerals = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
        if prev_id in roman_numerals and current_id in roman_numerals:
            prev_index = roman_numerals.index(prev_id)
            current_index = roman_numerals.index(current_id)
            return current_index == prev_index + 1
            
    except (ValueError, IndexError):
        pass
        
    return False

def _is_list_starter(item_id):
    """
    Check if an ID is a list starter pattern (1, a, A, i, I).
    """
    item_id = str(item_id).upper()
    
    # List starters: 1, a, A, i, I
    list_starters = {'1', 'A', 'I'}
    
    # Single lowercase letters are also list starters
    original_id = str(item_id)
    if original_id.isalpha() and len(original_id) == 1 and original_id.islower():
        return True
    
    return item_id in list_starters


# def _looks_like_toc_line(line: str) -> bool:
#     """
#     Returns True if the line looks like a Table of Contents entry.
#     """
#     line = line.strip()
    
#     # Lines ending with page numbers
#     if re.search(r'\d{1,3}\s*$', line):
#         return True
        
#     # Lines with leader dots
#     if re.search(r'\.{3,}\s*\d*$', line):
#         return True
        
#     # Common TOC patterns
#     toc_patterns = [
#         "contents", "table of", "chapter", "section", "page", "part",
#         "figure", "table", "illustration", "attachment", "annex"
#     ]
#     if any(pattern in line.lower() for pattern in toc_patterns):
#         return True
        
#     return False

def _looks_like_toc_line(line: str) -> bool:
    """
    Returns True if the line looks like a Table of Contents entry.
    """
    line = line.strip()
    
    # Lines ending with page numbers that are likely TOC entries
    # More specific pattern to avoid matching phone numbers, dates, etc.
    if re.search(r'(?:^|\s)\d{1,3}\s*$', line):
        # Additional check: the line should not look like contact info
        if not _looks_like_contact_info(line):
            return True
        
    # Lines with leader dots (but not email addresses or URLs)
    if re.search(r'(?<!\.)\.{3,}(?!\.)\s*\d*$', line) and not re.search(r'[@:/]', line):
        return True
        
    # Common TOC patterns (but not if it's part of other text)
    toc_patterns = [
        r'^contents$', r'^table of contents$', r'^chapter\b', r'^section\b', 
        r'^page\b', r'^part\b', r'^figure\b', r'^table\b', 
        r'^illustration\b', r'^attachment\b', r'^annex\b'
    ]
    
    for pattern in toc_patterns:
        if re.search(pattern, line.lower()):
            return True
            
    return False

def _looks_like_contact_info(line: str) -> bool:
    """
    Returns True if the line looks like contact information.
    """
    line_lower = line.lower()
    
    # Common contact info patterns
    contact_patterns = [
        r'@',  # Email addresses
        r'\.(com|org|net|gov|edu)$',  # Website endings
        r'ph#', r'phone', r'tel', r'fax',
        r'email', r'e-mail', r'contact',
        r'ext\.', r'extension',
        r'\d{3}[-.)]\d{3}[-.]\d{4}',  # Phone number patterns
        r'\(\d{3}\)\s*\d{3}-\d{4}'    # Another phone pattern
    ]
    
    return any(re.search(pattern, line_lower) for pattern in contact_patterns)

def _similar_formatting(line1, line2):
    """
    Check if two lines have similar formatting (rough heuristic)
    """
    # Similar length (within 50% difference)
    len_ratio = abs(len(line1) - len(line2)) / max(len(line1), len(line2))
    
    # Both start with similar patterns
    both_have_numbers = bool(re.match(r'\b\d', line1)) and bool(re.match(r'\b\d', line2))
    both_have_letters = bool(re.match(r'\b[A-Z]', line1)) and bool(re.match(r'\b[A-Z]', line2))
    
    return len_ratio < 0.5 or both_have_numbers or both_have_letters

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

def split_large_chunk(chunk, max_chars=2000):
    """
    Split chunk body into subchunks if it's too long.
    Try to preserve semantic coherence by splitting on paragraph boundaries.
    Empty subchunks are discarded.
    """
    body = chunk["body"]
    if len(body.strip()) <= max_chars:
        return [chunk]

    paragraphs = [p.strip() for p in body.split("\n\n") if p.strip()]
    subchunks = []
    buffer = ""

    for para in paragraphs:
        if len(buffer) + len(para) + 2 <= max_chars:
            buffer += para + "\n\n"
        else:
            if buffer.strip():  # only add non-empty buffer
                subchunks.append(buffer.strip())
            buffer = para + "\n\n"

    if buffer.strip():
        subchunks.append(buffer.strip())

    result = []
    for i, sub in enumerate(subchunks):
        if not sub.strip():
            continue  # skip empty subchunks
        new_chunk = dict(chunk)
        new_chunk["body"] = sub
        if len(subchunks) > 1:
            new_chunk["title"] = f"{chunk['title']} (Part {i+1})"
        result.append(new_chunk)

    return result

def _is_valid_chunk(chunk):
    if chunk["title"] and len(chunk["title"].split()) > 5:
        return True
    if chunk["body"] and len(chunk["body"].split()) > 5:   # add only if not empty/short body
        return True
    return False

def chunk_text(pdf_bytes: bytes) -> list:
    """
    Fixed chunk_text that properly handles all lines including the one after Contacts.
    """
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    chunks = []
    current_chunk = None
    pending_heading_id = None

    # First, extract ALL text lines in order using text extraction
    all_lines = []
    for page_num, page in enumerate(doc, start=1):
        # Get text with proper ordering
        text = page.get_text("text", sort=True)
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()
            if line and not _looks_like_toc_line(line):
                all_lines.append({
                    'text': line,
                    'page': page_num,
                    'fontnames': set(),  # We'll get this separately if needed
                    'x_positions': []    # We'll get this separately if needed
                })

    # DEBUG: Print ALL lines to see what's actually there
    # print("\n=== ALL LINES EXTRACTED ===")
    # for i, line_data in enumerate(all_lines):
    #     print(f"{i:3d}: '{line_data['text']}'")

    # Now get position information for each line using a second pass
    for i, line_data in enumerate(all_lines):
        line_text = line_data['text']
        page_num = line_data['page']
        
        # Use dict extraction to get font and position info for this specific line
        page = doc[page_num - 1]
        blocks = page.get_text("dict")["blocks"]
        
        line_fontnames = set()
        line_x_positions = []
        line_found = False
        
        for block in blocks:
            if block["type"] != 0:
                continue
            for line in block["lines"]:
                # Build the extracted text and collect all span info in one pass
                extracted_text = ""
                temp_fontnames = set()
                temp_x_positions = []
                
                for span in line["spans"]:
                    extracted_text += span["text"]
                    temp_fontnames.add(span["font"])
                    temp_x_positions.append(span["origin"][0])
                
                extracted_text = extracted_text.strip()
                
                # Check if this line matches our target text
                if extracted_text == line_text or line_text in extracted_text or extracted_text in line_text:
                    line_found = True
                    line_fontnames = temp_fontnames
                    line_x_positions = temp_x_positions
                    break
            
            if line_found:
                break
        
        # Update the line data with font and position info
        all_lines[i]['fontnames'] = line_fontnames
        all_lines[i]['x_positions'] = line_x_positions

    # Now process all lines with complete information
    for i, line_data in enumerate(all_lines):
        line_text = line_data['text']
        fontnames = line_data['fontnames']
        x_positions = line_data['x_positions']
        page_num = line_data['page']
        
        # Get context lines
        prev_line_data = all_lines[i - 1] if i > 0 else None
        prev_line_text = prev_line_data['text'] if prev_line_data else None
        next_line_data = all_lines[i + 1] if i + 1 < len(all_lines) else None
        next_line_text = next_line_data['text'] if next_line_data else None

        # print(f"\nProcessing line {i}: '{line_text}'")
        # if prev_line_text:
        #     print(f"  Previous: '{prev_line_text}'")
        # if next_line_text:
        #     print(f"  Next: '{next_line_text}'")

        # Check if this is a heading ID part
        if re.match(r'^(?:[IVXLCDM]+|\d+|[A-Z])[.)]\s*$', line_text):
            pending_heading_id = line_text
            print(f"  -> Found heading ID: '{pending_heading_id}'")
            continue

        # Check if we have a pending heading ID
        if pending_heading_id and line_text.isupper() and len(line_text.split()) >= 2:
            complete_heading = pending_heading_id + " " + line_text
            print(f"  -> Combined multi-line heading: '{complete_heading}'")
            
            is_heading = _is_heading(complete_heading, fontnames, x_positions,
                               previous_line=prev_line_text, 
                               next_line=next_line_text)
            
            if is_heading:
                if current_chunk:
                    current_chunk["body"] = _clean_text(current_chunk["body"])
                    chunks.append(current_chunk)
                
                heading_id, heading_title = _extract_heading_id_and_title(complete_heading)
                
                current_chunk = {
                    "id": heading_id,
                    "title": heading_title,
                    "body": "",
                    # "page": page_num,
                    # "parent_id": None,
                }
            
            pending_heading_id = None
            continue

        # Reset pending heading if this line doesn't continue it
        if pending_heading_id:
            print(f"  -> Adding pending ID '{pending_heading_id}' to current chunk")
            if current_chunk:
                current_chunk["body"] += " " + pending_heading_id
            pending_heading_id = None

        # Normal line processing
        is_heading = _is_heading(line_text, fontnames, x_positions,
                               previous_line=prev_line_text, next_line=next_line_text)
        
        if is_heading:
            if current_chunk:
                current_chunk["body"] = _clean_text(current_chunk["body"])
                if _is_valid_chunk(current_chunk):
                    chunks.append(current_chunk)
            
            heading_id, heading_title = _extract_heading_id_and_title(line_text)
            
            current_chunk = {
                "id": heading_id,
                "title": heading_title,
                "body": "",
                "page": page_num,
                "parent_id": None,
            }
            
        else:
            if current_chunk is not None:
                current_chunk["body"] += " " + line_text

    # Handle any remaining pending heading
    if pending_heading_id and current_chunk:
        current_chunk["body"] += " " + pending_heading_id

    # Save the last chunk
    if current_chunk:
        current_chunk["body"] = _clean_text(current_chunk["body"])
        if _is_valid_chunk(current_chunk):
            chunks.append(current_chunk)

    doc.close()
    return chunks

def _extract_heading_id_and_title(full_text: str) -> tuple:
    """
    Bulletproof heading extraction that works with NUMBERED_PATTERN
    """
    # Your pattern - note it only has ONE capturing group
    match = re.match(NUMBERED_PATTERN, full_text)
    
    if match:
        # Only group 1 exists - the ID part
        heading_id = match.group(1)
        
        # Find where the pattern ends to get the title
        pattern_end = match.end()
        remaining_text = full_text[pattern_end:].strip()
        
        # Now we need to figure out what delimiter was used
        # Look at the character right after the ID in the original text
        id_length = len(heading_id)
        if id_length < len(full_text):
            delimiter_char = full_text[id_length]
            if delimiter_char in ['.', ')', ' ']:
                heading_id_part = heading_id + delimiter_char if delimiter_char in ['.', ')'] else heading_id
            else:
                heading_id_part = heading_id
        else:
            heading_id_part = heading_id
        
        return heading_id_part, remaining_text
    
    # Fallback methods for cases that don't match the pattern
    # Method 2: Manual parsing for edge cases
    for i, char in enumerate(full_text):
        if char in ['.', ')'] and i + 1 < len(full_text) and full_text[i + 1].isspace():
            potential_id = full_text[:i + 1].strip()
            potential_title = full_text[i + 1:].strip()
            
            id_part = potential_id[:-1]
            if (id_part.isdigit() or 
                id_part.isalpha() and len(id_part) == 1 or
                id_part.upper() in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']):
                return potential_id, potential_title
    
    # Method 3: Split on whitespace for cases like "1         Title"
    if re.match(r'^\s*([IVXLCDM]+|\d+|[A-Z])\s+\S', full_text):
        # Split on first sequence of whitespace
        match = re.match(r'^\s*(\S+)\s+(\S.*)$', full_text)
        if match:
            heading_id = match.group(1)
            heading_title = match.group(2)
            
            # Check if the ID ends with . or ) and handle accordingly
            if heading_id and heading_id[-1] in ['.', ')']:
                return heading_id, heading_title
            else:
                return heading_id, heading_title
    
    # If all else fails
    return "", full_text