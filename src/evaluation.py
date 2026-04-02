import math
from .ngram import generate_ngrams
from .smoothing import laplace_smoothing, backoff_smoothing


def calculate_perplexity(tokens, model, smoothing="laplace", models=None):
    n = model.n
    ngrams = generate_ngrams(tokens, n)

    log_prob = 0
    N = len(ngrams)

    # 🔥 CACHE (major speed improvement)
    prob_cache = {}

    for gram in ngrams:

        # Use cached probability if available
        if gram in prob_cache:
            prob = prob_cache[gram]

        else:
            # BACKOFF for trigram
            if smoothing == "backoff" and n == 3:
                tri_model, bi_model, uni_model = models
                prob = backoff_smoothing(gram, tri_model, bi_model, uni_model)

            # Default Laplace
            else:
                prob = laplace_smoothing(gram, model)

            prob_cache[gram] = prob

        # Avoid log(0)
        if prob == 0:
            prob = 1e-10

        log_prob += math.log(prob)

    return math.exp(-log_prob / N)