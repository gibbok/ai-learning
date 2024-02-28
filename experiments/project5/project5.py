import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

os.system("clear")

# Read data
dir_path = "./experiments/project5/"
df = pd.read_csv(os.path.join(dir_path, "data.csv"))[0:50]

print(df)

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
    "age": [39],
    "workclass": ["State-gov"],
    "fnlwgt": [77516],
    "education": ["Bachelors"],
    "education-num": [13],
    "marital-status": ["Never-married"],
    "occupation": ["Adm-clerical"],
    "relationship": ["Not-in-family"],
    "race": ["White"],
    "sex": ["Male"],
    "capital-gain": [21740],
    "capital-loss": [0],
    "hours-per-week": [40],
    "native-country": ["United-States"],
}

# Convert new data to DataFrame
new_df = pd.DataFrame(new_data)

# Encode categorical variables
label_encoders_2 = {}
for column in new_df.select_dtypes(include=["object"]).columns:
    label_encoders_2[column] = LabelEncoder()
    new_df[column] = label_encoders[column].fit_transform(new_df[column])

# Predict using the trained model
prediction = model.predict(new_df)

# Map predicted label to readable salary
predicted_salary = "<=50K" if prediction[0] == 0 else ">50K"
print("Predicted salary:", predicted_salary)


plt.figure(figsize=(12, 6))  # Adjust figure size as needed
plot_tree(model, rounded=True, feature_names=X.columns)
plt.show()
