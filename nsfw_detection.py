import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sentence_utils import split_into_sentences_custom

# Load pretrained model and tokenizer
model_name = "valurank/finetuned-distilbert-adult-content-detection"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def preprocess_text(text):
    """Preprocess the input text by using custom sentence splitter."""
    sentences = split_into_sentences_custom(text)
    return sentences

def detect_nsfw_sentences(sentence):
    """Detect if a sentence is NSFW."""
    inputs = tokenizer(sentence, return_tensors="pt", truncation=True)
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=-1)
    nsfw_score = probs[0][1].item()

    if nsfw_score > 0.5:  # Threshold for NSFW detection
        return f"<nsfw>{sentence}</nsfw>"
    else:
        return sentence

def process_paragraph(paragraph):
    """Process a paragraph to detect and tag NSFW sentences."""
    sentences = preprocess_text(paragraph)
    nsfw_paragraph = []

    for sentence in sentences:
        nsfw_sentence = detect_nsfw_sentences(sentence)
        nsfw_paragraph.append(nsfw_sentence)
    
    return " ".join(nsfw_paragraph)
