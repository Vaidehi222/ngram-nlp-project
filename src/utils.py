import pandas as pd


def save_results(results, path="results/results.csv"):
    df = pd.DataFrame(results)
    df.to_csv(path, index=False)
    print(f"Results saved to {path}")