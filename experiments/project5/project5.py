import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

os.system("clear")

# Read data
dir_path = "./experiments/project5/"
df = pd.read_csv(os.path.join(dir_path, "data.csv"))

df_education = df[["education", "education-num"]].drop_duplicates()

# Encode categorical variables
label_encoders = {}
for column in df.select_dtypes(include=["object"]).columns:
    label_encoders[column] = (
        LabelEncoder()
    )  #  Transform non-numerical labels to numerical labels
    df[column] = label_encoders[column].fit_transform(df[column])

# Split features and target
X = df.drop(columns=["salary"])
y = df["salary"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train decision tree model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


def predict_salary(data):
    new_df = pd.DataFrame(data)
    # Encode categorical variables
    label_encoders_2 = {}
    for column in new_df.select_dtypes(include=["object"]).columns:
        label_encoders_2[column] = LabelEncoder()
        new_df[column] = label_encoders[column].fit_transform(new_df[column])
    # Predict using the trained model
    prediction = model.predict(new_df)
    # Map predicted label to readable salary
    predicted_salary = "<=50K" if prediction[0] == 0 else ">50K"
    return predicted_salary


# Example usage with new data
input_1 = {
    "age": [20],
    "workclass": ["Local-gov"],
    "fnlwgt": [125927],
    "education": ["7th-8th"],
    "education-num": [4],
    "marital-status": ["Never-married"],
    "occupation": ["Farming-fishing"],
    "relationship": ["Not-in-family"],
    "race": ["Asian-Pac-Islander"],
    "sex": ["Female"],
    "capital-gain": [1573],
    "capital-loss": [0],
    "hours-per-week": [35],
    "native-country": ["Cuba"],
}
print("Predicted salary 1:", predict_salary(input_1))

input_2 = {
    "age": [38],
    "workclass": ["Private"],
    "fnlwgt": [215646],
    "education": ["Masters"],
    "education-num": [14],
    "marital-status": ["Married-civ-spouse"],
    "occupation": ["Prof-specialty"],
    "relationship": ["NHusband"],
    "race": ["White"],
    "sex": ["Male"],
    "capital-gain": [14344],
    "capital-loss": [0],
    "hours-per-week": [48],
    "native-country": ["United-States"],
}

print("Predicted salary 2:", predict_salary(input_2))

# Plot model
fig, (axes) = plt.subplots(2, 2, figsize=(12, 6))
plot_tree(model, rounded=True, feature_names=X.columns, max_depth=2, ax=axes[0, 0])
sns.kdeplot(df["age"], ax=axes[0, 1])
sns.kdeplot(df["hours-per-week"], ax=axes[1, 1])
g = sns.kdeplot(
    df,
    x="education-num",
    ax=axes[1, 0],
)
g.set_xticks(df_education["education-num"].to_list())
g.set_xticklabels(labels=df_education["education"].to_list(), rotation=45)
plt.tight_layout()
plt.show()
