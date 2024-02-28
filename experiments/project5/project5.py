import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

os.system("clear")

# Read data
dir_path = "./experiments/project5/"
df = pd.read_csv(os.path.join(dir_path, "data.csv"))

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

# # Example usage with new data
# new_data = {
#     "age": [45],
#     "workclass": ["Private"],
#     "fnlwgt": [83311],
#     "education": ["Bachelors"],
#     "education-num": [13],
#     "marital-status": ["Married-civ-spouse"],
#     "occupation": ["Exec-managerial"],
#     "relationship": ["Husband"],
#     "race": ["White"],
#     "sex": ["Male"],
#     "capital-gain": [0],
#     "capital-loss": [0],
#     "hours-per-week": [40],
#     "native-country": ["United-States"],
# }

# # Convert new data to DataFrame
# new_df = pd.DataFrame(new_data)

# # Encode categorical variables
# for column in new_df.select_dtypes(include=["object"]).columns:
#     new_df[column] = label_encoders[column].transform(new_df[column])

# # Predict using the trained model
# prediction = model.predict(new_df)
# print("Predicted salary:", prediction[0])
