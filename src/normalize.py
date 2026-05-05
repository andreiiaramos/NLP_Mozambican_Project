import json
import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/raw/sentences.csv")
ORTHO_RULES = Path("rules/orthography_rules.json")
LEXICON = Path("rules/lexicon.json")
OUTPUT_PATH = Path("data/processed/normalized_sentences.csv")


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def normalize_sentence(sentence, ortho_rules, lexicon):
    normalized = sentence

    # Apply informal orthography rules
    for old, new in ortho_rules.items():
        normalized = normalized.replace(old, new)

    # Apply borrowed vocab lexicon
    for old, new in lexicon.items():
        normalized = normalized.replace(old, new)

    return normalized


def main():
    df = pd.read_csv(DATA_PATH)

    ortho_rules = load_json(ORTHO_RULES)
    lexicon = load_json(LEXICON)

    df["normalized_sentence"] = df["sentence"].apply(
        lambda s: normalize_sentence(str(s), ortho_rules, lexicon)
    )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print(f"Saved normalized data to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()