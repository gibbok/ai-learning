import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

os.system("clear")

# Original data
data = {
    "age": [39, 50, 35, 45],  # Adding more samples
    "workclass": [
        "State-gov",
        "Self-emp-not-inc",
        "Private",  # Sample with different workclass
        "Private",  # Sample with different workclass
    ],
    "fnlwgt": [
        77516,
        83311,
        215646,  # Sample with different fnlwgt
        234721,  # Sample with different fnlwgt
    ],
    "education": [
        "Bachelors",
        "Bachelors",
        "HS-grad",  # Sample with different education
        "Masters",  # Sample with different education
    ],
    "education-num": [
        13,
        13,
        9,  # Sample with different education-num
        14,  # Sample with different education-num
    ],
    "marital-status": [
        "Never-married",
        "Married-civ-spouse",
        "Married-civ-spouse",  # Sample with different marital-status
        "Married-civ-spouse",  # Sample with different marital-status
    ],
    "occupation": [
        "Adm-clerical",
        "Exec-managerial",
        "Sales",  # Sample with different occupation
        "Prof-specialty",  # Sample with different occupation
    ],
    "relationship": [
        "Not-in-family",
        "Husband",
        "Husband",  # Sample with different relationship
        "Husband",  # Sample with different relationship
    ],
    "race": [
        "White",
        "White",
        "White",
        "White",
    ],
    "sex": [
        "Male",
        "Male",
        "Male",
        "Male",
    ],
    "capital-gain": [
        2174,
        0,
        0,
        0,
    ],
    "capital-loss": [
        0,
        0,
        0,
        0,
    ],
    "hours-per-week": [
        40,
        13,
        40,
        45,  # Sample with different hours-per-week
    ],
    "native-country": [
        "United-States",
        "United-States",
        "United-States",
        "United-States",
    ],
    "salary": [
        "<=50K",
        "<=50K",
        "<=50K",  # Sample with different salary class
        ">50K",  # Sample with different salary class
    ],
}

# Create DataFrame
df = pd.DataFrame(data)

# Encode categorical variables
label_encoders = {}
for column in df.select_dtypes(include=["object"]).columns:
    label_encoders[column] = LabelEncoder()
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

# Example usage with new data
new_data = {
    "age": [45],
    "workclass": ["Private"],
    "fnlwgt": [83311],
    "education": ["Bachelors"],
    "education-num": [13],
    "marital-status": ["Married-civ-spouse"],
    "occupation": ["Exec-managerial"],
    "relationship": ["Husband"],
    "race": ["White"],
    "sex": ["Male"],
    "capital-gain": [0],
    "capital-loss": [0],
    "hours-per-week": [40],
    "native-country": ["United-States"],
}

# Convert new data to DataFrame
new_df = pd.DataFrame(new_data)

# Encode categorical variables
for column in new_df.select_dtypes(include=["object"]).columns:
    new_df[column] = label_encoders[column].transform(new_df[column])

print(new_df)

# Predict using the trained model
prediction = model.predict(new_df)
print("Predicted salary:", prediction[0])
