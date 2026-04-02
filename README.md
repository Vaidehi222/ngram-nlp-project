🔹Title
N-Gram Language Modeling with Smoothing Techniques

🔹Description
Built word-level unigram, bigram, and trigram language models from scratch in Python. Implemented Laplace and Back-off smoothing techniques and evaluated performance using perplexity on IMDB and Reuters datasets.

🔹Features
Implemented N-gram models (Unigram, Bigram, Trigram)
Applied Laplace and Back-off smoothing
Evaluated using perplexity metric
Compared performance across multiple datasets
Visualized results using graphs

🔹Results
Dataset	 Model	  Smoothing	 Perplexity
IMDB	 Bigram	  Laplace	 4964
IMDB	 Trigram  Backoff	 457
Reuters	 Bigram	  Laplace	 1967
Reuters	 Trigram  Backoff	 125

🔹Key Insights
Trigram + Backoff significantly improves performance
Laplace smoothing overestimates probabilities
Reuters performs better due to structured language
IMDB shows higher perplexity due to noisy text