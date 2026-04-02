from src.utils import save_results
from src.data_loader import load_imdb, load_reuters_train, load_reuters_test
from src.preprocess import preprocess
from src.ngram import NGramModel
from src.evaluation import calculate_perplexity


# =========================
# BIGRAM (LAPLACE)
# =========================
def run_bigram(name, train_text, test_text, results):
    train_tokens = preprocess(train_text, n=2)
    test_tokens = preprocess(test_text, n=2)

    model = NGramModel(2)
    model.train(train_tokens)

    pp = calculate_perplexity(test_tokens, model, smoothing="laplace")

    print(f"{name} Bigram Perplexity: {pp}")

    results.append({
        "Dataset": name,
        "Model": "Bigram",
        "Smoothing": "Laplace",
        "Perplexity": pp
    })


# =========================
# TRIGRAM (BACKOFF)
# =========================
def run_trigram_backoff(name, train_text, test_text, results):
    train_tokens = preprocess(train_text, n=3)
    test_tokens = preprocess(test_text, n=3)

    uni_model = NGramModel(1)
    bi_model = NGramModel(2)
    tri_model = NGramModel(3)

    uni_model.train(train_tokens)
    bi_model.train(train_tokens)
    tri_model.train(train_tokens)

    pp = calculate_perplexity(
        test_tokens,
        tri_model,
        smoothing="backoff",
        models=(tri_model, bi_model, uni_model)
    )

    print(f"{name} Trigram (Backoff) Perplexity: {pp}")

    results.append({
        "Dataset": name,
        "Model": "Trigram",
        "Smoothing": "Backoff",
        "Perplexity": pp
    })


# =========================
# MAIN PIPELINE
# =========================
if __name__ == "__main__":

    results = []   # 🔥 FIXED: define results list

    # ===== IMDB =====
    print("\n===== IMDB DATASET =====")

    imdb_text = load_imdb()

    tokens = preprocess(imdb_text, n=2)
    split = int(0.8 * len(tokens))

    train_tokens = tokens[:split]
    test_tokens = tokens[split:]

    train_text_imdb = " ".join(train_tokens)
    test_text_imdb = " ".join(test_tokens)

    run_bigram("IMDB", train_text_imdb, test_text_imdb, results)
    run_trigram_backoff("IMDB", train_text_imdb, test_text_imdb, results)

    # ===== REUTERS =====
    print("\n===== REUTERS DATASET =====")

    train_text_reuters = load_reuters_train()
    test_text_reuters = load_reuters_test()

    run_bigram("Reuters", train_text_reuters, test_text_reuters, results)
    run_trigram_backoff("Reuters", train_text_reuters, test_text_reuters, results)

    # Save results
    save_results(results)