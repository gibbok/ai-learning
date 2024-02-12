import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import random

dir_path = "./experiments/sentiment-analysis-games/"

# Read data
df = pd.read_csv(os.path.join(dir_path, "data.csv"))

df = df.sample(5)  # REMOVE THIS

# Keep only data for review
df = df[["review", "voted_up"]]
print(df)
# Strip leading and trailing whitespace
df["review"] = df["review"].str.strip()
# Remove line breaks
df["review"] = df["review"].str.replace(r"\n", " ", regex=True)
# Filter rows with review length greater than 2
df = df.loc[df["review"].str.len() > 2]
# Remove duplicates
df = df.drop_duplicates("review")

# Save cleaned data
df.to_csv(os.path.join(dir_path, "data-clean.csv"), index=False)

vectorizer = CountVectorizer(
    analyzer="word",
    lowercase=False,
)

# Tokenize
reviews_list = df["review"].astype(str).values.tolist()
votes_list = df["voted_up"].astype(bool).values.tolist()
features = vectorizer.fit_transform(reviews_list)
features_nd = features.toarray()

X = features_nd[:, :-1]  # Features (all columns except the last one)
y = features_nd[:, -1]  # Target variable (last column)

X_train, X_test, y_train, y_test = train_test_split(
    features_nd, votes_list, train_size=0.80, random_state=1234
)

log_model = LogisticRegression()
log_model = log_model.fit(X=X_train, y=y_train)

y_pred = log_model.predict(X_test)

print(y_pred)
