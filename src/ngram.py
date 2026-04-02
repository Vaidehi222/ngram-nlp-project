from collections import defaultdict
from typing import List, Tuple, Dict

def generate_ngrams(tokens: List[str], n: int) -> List[Tuple]:
    return [tuple(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]

class NGramModel:
    def __init__(self, n: int):
        self.n = n
        self.ngram_counts = defaultdict(int)
        self.context_counts = defaultdict(int)
        self.vocab = set()

    def train(self, tokens: List[str]):
        self.vocab = set(tokens)
        ngrams = generate_ngrams(tokens, self.n)

        for gram in ngrams:
            self.ngram_counts[gram] += 1
            context = gram[:-1]
            self.context_counts[context] += 1

    def get_vocab_size(self):
        return len(self.vocab)

    def get_ngram_count(self, ngram: Tuple):
        return self.ngram_counts[ngram]

    def get_context_count(self, context: Tuple):
        return self.context_counts[context]