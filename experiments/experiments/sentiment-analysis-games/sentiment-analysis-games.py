import pandas as pd

dir_path = "./experiments/sentiment-analysis-games/"

# Read data
df = pd.read_csv(dir_path + "data.csv")

# Strip content
df["review"] = df["review"].str.strip()

# Drop empty rows
df = df.dropna()

# Remove any line breaks
special_chars = r"\n*"
df["review"] = df["review"].str.replace(special_chars, "", regex=True)

# Select only review
# df = df[["review"]]

df.to_csv(dir_path + "data-clean.csv", index=False)
