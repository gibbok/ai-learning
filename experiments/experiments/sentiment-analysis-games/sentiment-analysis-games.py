import pandas as pd

# Read data
data = pd.read_csv("./experiments/sentiment-analysis-games/data.csv")
reviews = data[["review"]]

# Drop empty rows
reviews = reviews.dropna()
reviews["review"] = reviews["review"].str.strip()

# Remove any non-word or non-whitespace character
special_chars = r"[^\w\s]"
reviews["review"] = reviews["review"].str.replace(special_chars, "", regex=True)

print(reviews)
