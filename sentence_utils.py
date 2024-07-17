import re

def split_into_sentences_custom(paragraph):
    """Split paragraph into sentences based on periods and question marks."""
    pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s+'
    sentences = re.split(pattern, paragraph)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return sentences
