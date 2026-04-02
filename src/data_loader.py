import pandas as pd


# =========================
# IMDB DATASET LOADER
# =========================
def load_imdb(path="data/IMDB Dataset.csv"):
    import pandas as pd
    df = pd.read_csv(path)

    df = df.sample(2000)   # 🔥 MUST ADD (for speed)

    df['review'] = df['review'].fillna("")
    return " ".join(df['review'].astype(str).tolist())


# =========================
# REUTERS (APTE SPLIT)
# =========================
def load_reuters_train(path="data/ModApte_train.csv"):
    df = pd.read_csv(path)

    # Detect correct column
    if 'text' in df.columns:
        column = 'text'
    elif 'body' in df.columns:
        column = 'body'
    else:
        raise ValueError("No valid text column found in Reuters train dataset")

    # Clean NaN
    df[column] = df[column].fillna("")

    text_data = " ".join(df[column].astype(str).tolist())
    return text_data


def load_reuters_test(path="data/ModApte_test.csv"):
    df = pd.read_csv(path)

    if 'text' in df.columns:
        column = 'text'
    elif 'body' in df.columns:
        column = 'body'
    else:
        raise ValueError("No valid text column found in Reuters test dataset")

    df[column] = df[column].fillna("")

    text_data = " ".join(df[column].astype(str).tolist())
    return text_data
