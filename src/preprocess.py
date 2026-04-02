import re
from typing import List

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

def tokenize(text: str) -> List[str]:
    return text.split()

def add_sentence_tokens(tokens: List[str], n: int) -> List[str]:
    start_tokens = ['<s>'] * (n - 1)
    end_tokens = ['</s>']
    return start_tokens + tokens + end_tokens

def preprocess(text: str, n: int) -> List[str]:
    text = clean_text(text)
    tokens = tokenize(text)
    tokens = add_sentence_tokens(tokens, n)
    return tokens