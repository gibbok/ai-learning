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

# Filter rows with one or two characters
df = df[df["review"].apply(lambda x: len(x) > 2)]

# Select only review
# df = df[["review"]]

df.to_csv(dir_path + "data-clean.csv", index=False)
