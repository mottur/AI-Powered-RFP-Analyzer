"""
Module for classifying and tagging sections of text using NLP models.
"""

import spacy
import mlflow
import matplotlib
matplotlib.use('Agg')   # use non-interactive backend to prevent display
import matplotlib.pyplot as plt
import os
import io
import numpy as np
from PIL import Image
from collections import defaultdict
from shared import LABELS
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from setfit import SetFitModel, Trainer, TrainingArguments
from datasets import Dataset
from sklearn.utils import shuffle

# SetFit model and trainer initialization
if os.path.exists("./classifier"):
    classifier = SetFitModel.from_pretrained("./classifier")
else:
    classifier = None
trainer = None

# spaCy NER model initialization
nlp = spacy.load("en_core_web_trf")
ruler = nlp.add_pipe("entity_ruler", before="ner")
patterns = [{"label": "IGNORE", "pattern": label} for label in LABELS.keys()]
extra_ignore_terms = ["E-Mail", "Email"]
patterns.extend([{"label": "IGNORE", "pattern": term} for term in extra_ignore_terms])
ruler.add_patterns(patterns)


"""TRAINING AND EVALUATION FUNCTIONS"""

def train_classifier(train_texts: list, train_labels: list, eval_texts: list = None, eval_labels: list = None) -> dict:
    """
    Trains the classifier using few-shot learning.
    """
    train_texts, train_labels = shuffle(train_texts, train_labels, random_state=42)
    train_labels = _add_label_descriptions(train_labels)
    train_dataset = Dataset.from_dict({"text": train_texts, "label": train_labels})
    if eval_texts and eval_labels:
        eval_texts, eval_labels = shuffle(eval_texts, eval_labels, random_state=42)
        eval_labels = _add_label_descriptions(eval_labels)
        eval_dataset = Dataset.from_dict({"text": eval_texts, "label": eval_labels})
    else:
        eval_dataset = None
    
    mlflow.set_experiment("rfp_analyzer")
    run_id = None

    with mlflow.start_run():
        mlflow.log_params({
            "labels": list(LABELS.keys()),
            "classifier": "sentence-transformers/all-MiniLM-L6-v2",
            "num_train_samples": len(train_dataset),
            "num_eval_samples": len(eval_dataset),
            "num_epochs": 1,
            "batch_size": 16,
            "learning_rate": 2e-5
        })

        classifier = SetFitModel.from_pretrained(
            "sentence-transformers/all-MiniLM-L6-v2",
            train_batch_size=16,
            num_iterations=20,  # Number of text pairs for contrastive learning
            num_epochs=1,      # Number of epochs for classification head
            learning_rate=2e-5,
            column_mapping={"text": "text", "label": "label"}
        )
        trainer = Trainer(
            model=classifier,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            metric=_evaluate
        )
        trainer.train()

        metrics = trainer.evaluate()
        mlflow.log_metrics({
            "accuracy": metrics["accuracy"],
            "precision": metrics["precision"],
            "recall": metrics["recall"],
            "f1_score": metrics["f1_score"]
        })

        cm = np.array(metrics["confusion_matrix"])
        cm_image = _plot_confusion_matrix(cm, class_names=list(LABELS.keys()))
        mp_image = _plot_metrics(metrics)
        mlflow.log_image(cm_image, "confusion_matrix.png")
        mlflow.log_image(mp_image, "metrics.png")

        trainer.model.save_pretrained("./classifier")
        mlflow.log_artifacts("./classifier", "model")

        run_id = mlflow.active_run().info.run_id
        mlflow.end_run()
        return metrics, run_id
    
def classify_manually(texts):
    """
    Manual classification for training data.
    """
    categories = {label: {"sections": []} for label in LABELS}
    for sec in texts:
        print("\n---\n")
        print(f"Title: {sec['title']}\n")
        print(f"Body: {sec['body']}\n")
        print("Available Labels:")
        for i, label in enumerate(LABELS.keys()):
            print(f"{i}: {label}")
        while True:
            try:
                choice = input("Enter the number corresponding to the correct label (or -1 to skip): ")
                if choice == "exit":
                    print("Exiting manual classification.")
                    return categories
                else:
                    choice = int(choice)
                if choice == -1:
                    sec["true_label"] = None
                    break
                elif 0 <= choice < len(LABELS):
                    sec["true_label"] = list(LABELS.keys())[choice]
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        if sec["true_label"]:
            print(f"Assigned label: {sec['true_label']}")
            categories[sec["true_label"]]["sections"].append(sec)

    return categories
    
def _add_label_descriptions(labels: list) -> list:
    return [f"{label} - {LABELS[label]}" for label in labels]

def _clean_label(pred_label: str) -> str:
    return pred_label.split(" - ")[0]

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

def _evaluate(y_pred, y_true) -> dict:
    """
    Evaluates classification performance.
    """
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_true, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)
    cm = confusion_matrix(y_true, y_pred)
    
    return {"accuracy": accuracy, "precision": precision, "recall": recall, 
            "f1_score": f1, "confusion_matrix": cm.tolist()}

def _plot_confusion_matrix(cm, class_names=None):
    """Plot confusion matrix and return as PIL Image"""
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    ax.figure.colorbar(im, ax=ax)
    
    if class_names is None:
        class_names = [f"Class {i}" for i in range(len(cm))]
    
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           xticklabels=class_names, 
           yticklabels=class_names,
           title="Confusion Matrix",
           ylabel="True label",
           xlabel="Predicted label")

    # Add text annotations
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], 'd'),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    
    fig.tight_layout()

    # Save to file
    filepath = os.path.join("visualization", "confusion_matrix.png")
    fig.savefig(filepath, format='png', dpi=150, bbox_inches='tight')
    print(f"Confusion matrix saved to: {filepath}")
    
    # Save to buffer and convert to PIL Image
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=150, bbox_inches='tight')
    buf.seek(0)
    pil_image = Image.open(buf)
    plt.close(fig)
    
    return pil_image

def _plot_metrics(metrics: dict):
    """Plot accuracy, precision, recall, and F1-score"""
    labels = list(metrics.keys())
    values = list(metrics.values())

    # Create figure and axes
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(labels, values, color='skyblue')

    # Add value labels on top of bars
    for i, v in enumerate(values):
        ax.text(i, v + 0.01, f"{v:.2f}", ha='center', fontweight='bold')

    # Set labels and title
    ax.set_title("Model Evaluation Metrics")
    ax.set_ylabel("Score")
    ax.set_ylim(0, 1.05)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    fig.tight_layout()

    # Save to file
    filepath = os.path.join("visualization", "metrics.png")
    fig.savefig(filepath, format='png', dpi=300, bbox_inches='tight')
    print(f"Metrics plot saved to: {filepath}")
    
    # Save to buffer and convert to PIL Image
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    buf.seek(0)
    pil_image = Image.open(buf)
    plt.close(fig)
    
    return pil_image


"""CLASSIFICATION AND TAGGING PIPELINE FUNCTIONS"""

def classify_and_tag(sections) -> dict:
    """
    Full pipeline to classify sections and tag keywords.
    """
    mlflow.set_experiment("rfp_analyzer")
    run_id = None

    with mlflow.start_run():
        mlflow.log_params({
            "labels": list(LABELS.keys()),
            "classifier": "sentence-transformers/all-MiniLM-L6-v2",
            "nlp_model": "en_core_web_trf",
        })

        _classify_primary_sections(sections)
        _tag_keywords(sections)
        categories = _consolidate_categories(sections)
       
        run_id = mlflow.active_run().info.run_id
        mlflow.end_run()

    return categories, run_id

def _classify_primary_sections(sections):
    """
    Classifies each section into primary categories using zero-shot classification.
    """
    chunks = [sec["title"] + "\n" + sec["body"] for sec in sections]
    preds = classifier(chunks)
    for sec, pred in zip(sections, preds):
        sec["label"] = _clean_label(pred)

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