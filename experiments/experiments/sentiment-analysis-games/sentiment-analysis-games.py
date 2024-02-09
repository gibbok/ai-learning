import os
import pandas as pd

dir_path = "./experiments/sentiment-analysis-games/"

# Read data
df = pd.read_csv(os.path.join(dir_path, "data.csv"))

# Clean data
df = df.assign(review=df["review"].str.strip().str.replace(r"\n", "")).loc[
    df["review"].str.len() > 2
]

# Clean data
df["review"] = df["review"].str.strip().str.replace(r"\n", "")

# Save cleaned data
df.to_csv(os.path.join(dir_path, "data-clean.csv"), index=False)
