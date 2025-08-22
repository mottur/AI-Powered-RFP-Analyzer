"""
Module for classifying and tagging sections of text using NLP models.
"""

import spacy
from transformers import pipeline
from collections import defaultdict


LABELS = {
    "Scope": "This section describes the scope of the project, including its goals, boundaries, assumptions, and context.",
    "Deliverables": "This section lists the deliverables or tangible outputs the offeror/contractor is required to provide.",
    "Company Info": "This section provides background information about the offeror/contractor, including qualifications, past experience, and mission.",
    "Timeline": "This section outlines the length of the contract, deadlines, project start and end dates, and other key milestone schedules."
}

patterns = [{"label": "IGNORE", "pattern": label} for label in LABELS.keys()]
extra_ignore_terms = ["E-Mail", "Email"]
patterns.extend([{"label": "IGNORE", "pattern": term} for term in extra_ignore_terms])

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
nlp = spacy.load("en_core_web_trf")
ruler = nlp.add_pipe("entity_ruler", before="ner")
ruler.add_patterns(patterns)

def _classify_section(text: str) -> str:
    """
    Classifies a section of text into one of the predefined labels using zero-shot classification."""
    hypotheses = list(LABELS.values())
    result = classifier(text, hypotheses, multi_label=True)

    # Map back to original label name
    predicted_description = result["labels"][0]
    for key, desc in LABELS.items():
        if desc == predicted_description:
            return key
    return "Unknown"

def _classify_primary_sections(sections):
    """
    Classifies each section into primary categories using zero-shot classification.
    """
    for sec in sections:
        context = "This is an excerpt from a government Request for Proposal (RFP) document:\n"
        full_text = context + sec["title"] + "\n" + sec["body"]
        sec["label"] = _classify_section(full_text)

def _tag_keywords(sections):
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

def _consolidate_categories(sections) -> dict:
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

def classify_and_tag(sections) -> dict:
    """
    Full pipeline to classify sections and tag keywords.
    """
    _classify_primary_sections(sections)
    _tag_keywords(sections)
    return _consolidate_categories(sections)