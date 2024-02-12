import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Read data
dir_path = "./experiments/sentiment-analysis-games/"
df = pd.read_csv(os.path.join(dir_path, "data.csv"))

# Keep only relevat data
df = df[["review", "voted_up"]]

df.sample(100)

# Preprocess data
df["review"] = df["review"].str.strip()
df["review"] = df["review"].str.replace(r"\n", " ", regex=True)
df = df.loc[df["review"].str.len() > 2]
df = df.drop_duplicates("review")

# Vectorize text
vectorizer = CountVectorizer(analyzer="word", lowercase=False)
features = vectorizer.fit_transform(df["review"].values.tolist())

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    features, df["voted_up"], test_size=0.2, random_state=42
)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict sentiment for each row
y_pred = model.predict(features)

# Add predicted sentiment to the DataFrame
df["predicted_sentiment"] = y_pred

# Convert true sentiment to readable labels
df["true_sentiment"] = df["voted_up"].apply(lambda x: "Upvoted" if x else "Not Upvoted")

# Create a result DataFrame with relevant columns
result_df = df[["review", "true_sentiment", "predicted_sentiment"]]

# Save the result DataFrame as a CSV file
result_df.to_csv(os.path.join(dir_path, "sentiment_results.csv"), index=False)
print("Results saved to", os.path.join(dir_path, "sentiment_results.csv"))
