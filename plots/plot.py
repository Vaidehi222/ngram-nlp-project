import pandas as pd
import matplotlib.pyplot as plt

# Load results
df = pd.read_csv("results/results.csv")

# Plot for each dataset
for dataset in df["Dataset"].unique():
    subset = df[df["Dataset"] == dataset]

    plt.figure()
    plt.bar(subset["Model"], subset["Perplexity"])
    plt.title(f"{dataset} Model Comparison")
    plt.xlabel("Model")
    plt.ylabel("Perplexity")

    plt.savefig(f"plots/{dataset}_comparison.png")
    plt.close()

print("Graphs saved in plots/")