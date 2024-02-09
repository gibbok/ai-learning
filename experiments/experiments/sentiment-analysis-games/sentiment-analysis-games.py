import os
import pandas as pd

dir_path = "./experiments/sentiment-analysis-games/"

# Read data
df = pd.read_csv(os.path.join(dir_path, "data.csv"))

# Clean review data
# trim, remove line breacks, remove line with length <= 2
df = df.assign(review=df["review"].str.strip().str.replace(r"\n", "")).loc[
    df["review"].str.len() > 2
]

# Save cleaned data
df.to_csv(os.path.join(dir_path, "data-clean.csv"), index=False)
