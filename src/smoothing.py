def laplace_smoothing(ngram, model):
    context = ngram[:-1]
    vocab_size = model.get_vocab_size()

    numerator = model.get_ngram_count(ngram) + 1
    denominator = model.get_context_count(context) + vocab_size

    return numerator / denominator


def backoff_smoothing(trigram, tri_model, bi_model, uni_model):
    w1, w2, w3 = trigram

    # Trigram
    if tri_model.get_ngram_count((w1, w2, w3)) > 0:
        return tri_model.get_ngram_count((w1, w2, w3)) / tri_model.get_context_count((w1, w2))

    # Bigram
    elif bi_model.get_ngram_count((w2, w3)) > 0:
        return bi_model.get_ngram_count((w2, w3)) / bi_model.get_context_count((w2,))

    # Unigram
    else:
        total = sum(uni_model.ngram_counts.values())
        return uni_model.get_ngram_count((w3,)) / total