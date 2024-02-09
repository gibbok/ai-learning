import pandas as pd

# Read data
data = pd.read_csv("./experiments/sentiment-analysis-games/data.csv")

reviews = data[["review"]]

reviews_no_empties = reviews.dropna()
