import pandas as pd
from pathlib import Path

INPUT_PATH = Path("results/evaluation.csv")
OUTPUT_PATH = Path("results/summary.csv")


def main():
    df = pd.read_csv(INPUT_PATH)

    summary = (
        df.groupby(["phenomenon", "improved"])
        .size()
        .reset_index(name="count")
    )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(OUTPUT_PATH, index=False)

    print(summary)
    print(f"Saved summary to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()