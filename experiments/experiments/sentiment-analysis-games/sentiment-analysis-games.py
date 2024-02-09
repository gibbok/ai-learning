import os
import pandas as pd

dir_path = "./experiments/sentiment-analysis-games/"

# Read data
df = pd.read_csv(os.path.join(dir_path, "data.csv"))

# Strip leading and trailing whitespace
df["review"] = df["review"].str.strip()
# Remove line breaks
df["review"] = df["review"].str.replace(r"\n", "")
# Filter rows with review length greater than 2
df = df.loc[df["review"].str.len() > 2]
# Remove duplicates
df = df.drop_duplicates("review")

# Save cleaned data
df.to_csv(os.path.join(dir_path, "data-clean.csv"), index=False)
