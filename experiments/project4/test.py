import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Example DataFrame
data = {
    "title": ["movie a", "movie a", "movie b", "movie c", "movie d"],
    "type": ["tv", "cinema", "tv", "cinema", "cinema"],
    "release_year": [2020, 2020, 2021, 2022, 2022],
    "listed_in_new": [
        "drama",
        "drama",
        "comedy",
        "drama",
        "drama",
    ],
    "country": ["usa", "usa", "usa", "ita", "ita"],
    "director_new": [
        "director_a",
        "director_b",
        "director_b",
        "director_c",
        "director_d",
    ],
    "cast_new": ["cast_a", "cast_a", "cast_b", "cast_b", "cast_c"],
}
df = pd.DataFrame(data)

# Encode categorical variables
label_encoders = {}
for col in ["type", "listed_in_new", "country", "director_new", "cast_new"]:
    label_encoders[col] = LabelEncoder()
    df[col] = label_encoders[col].fit_transform(df[col])

# Split data into features and target variable
X = df.drop(columns=["title"])
y = df["title"]

# Train Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)

# Example of prediction
# Suppose you have a new movie with the following features
new_movie_features = {
    "type": "tv",
    "release_year": 2023,
    "listed_in_new": "drama",
    "country": "usa",
    "director_new": "director_a",
    "cast_new": "cast_a",
}

# Encode the new movie features
encoded_features = {}
for col in new_movie_features:
    if col in label_encoders:
        encoded_features[col] = label_encoders[col].transform(
            [new_movie_features[col]]
        )[0]
    else:
        encoded_features[col] = new_movie_features[col]

# Convert the encoded features into a DataFrame
new_movie_df = pd.DataFrame([encoded_features])


# Predict the title for the new movie
predicted_title = clf.predict(new_movie_df)
print("Predicted Title:", predicted_title[0])
