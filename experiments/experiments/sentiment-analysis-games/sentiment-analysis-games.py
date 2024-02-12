import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score, roc_curve
from matplotlib import pyplot as plt

# Read data
dir_path = "./experiments/sentiment-analysis-games/"
df = pd.read_csv(os.path.join(dir_path, "data.csv"))

# Keep only relevat data
df = df[["review", "voted_up"]]

# Use only a sample of the data
# df.sample(5)

# Preprocess data
df["review"] = df["review"].str.strip()
df["review"] = df["review"].str.replace(r"\n", " ", regex=True)
df = df.loc[df["review"].str.len() > 2]
df = df.drop_duplicates("review")

# Vectorize text
vectorizer = CountVectorizer(analyzer="word", lowercase=False)
reviews = vectorizer.fit_transform(df["review"].values.tolist())

# Split data into training and testing sets
X = reviews
y = df["voted_up"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict sentiment for each row
y_pred = model.predict(reviews)

# Add predicted sentiment to the DataFrame
df["predicted_sentiment"] = y_pred

# Convert true sentiment to readable labels
df["true_sentiment"] = df["voted_up"].apply(lambda x: "Upvoted" if x else "Not Upvoted")

# Create a result DataFrame with relevant columns
result_df = df[["review", "true_sentiment", "predicted_sentiment"]]

# Save the result DataFrame as a CSV file
result_df.to_csv(os.path.join(dir_path, "sentiment_results.csv"), index=False)
print("Results saved to", os.path.join(dir_path, "sentiment_results.csv"))


# Evaluate the model on the testing set

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Accuracy is the percentage of times that a model is correct
# Precision measures the proportion of positive predictions that were actually correct
# Recall measures the proportion of actually positive cases that your model correctly identified
# F1-score combines precision and recall into a single metric, it is balancing act between finding the positives AND not making mistakes!
print("Model evaluation:")
print(f"  Accuracy: {accuracy:.4f}")
print(f"  Precision: {precision:.4f}")
print(f"  Recall: {recall:.4f}")
print(f"  F1-score: {f1:.4f}")


# Use the classification_report function from sklearn.metrics to get a more detailed breakdown of the model's performance per class,
# including precision, recall, F1-score, and support (number of samples in each class).
report = classification_report(y_test, y_pred)
print(report)


# Plot the Receiver Operating Characteristic (ROC) curve and calculate the Area Under the Curve (AUC)
# to understand the model's ability to distinguish between classes at different thresholds.
# ROC curve uses true and false positive rates to visually assess a binary classification model's performance.#
y_score = model.predict_proba(X_test)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_score)
roc_auc = roc_auc_score(y_test, y_score)
plt.plot(fpr, tpr, label="ROC curve (area = %0.2f)" % roc_auc)
plt.plot([0, 1], [0, 1], color="navy", linestyle="--")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve for Sentiment Classification")
plt.legend()
plt.show()
