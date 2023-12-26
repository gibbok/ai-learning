from sklearn.linear_model import LinearRegression
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Given data
X = [[1], [2], [3], [4], [5]]  # Features (independent variable)
y = [2, 3, 4, 5, 6]  # Target (dependent variable)

# Initialize the Linear Regression model
model = LinearRegression()

# Creating a DataFrame from X and y
data = pd.DataFrame({"X": [val[0] for val in X], "Y": y})

# Fit the model using the given data
model.fit(X, y)

# Coefficient (slope) and intercept
coef = model.coef_[0]
intercept = model.intercept_

print(f"Coefficient: {coef}")  # Coefficient or slope of the line
print(f"Intercept: {intercept}")  # Intercept of the line

# Predict using the trained model
predicted_y = model.predict(X)

# Display predicted values
for i, x in enumerate(X):
    print(f"X = {x[0]}, Predicted Y = {predicted_y[i]}")

# Predict a new value
new_value = 8
predicted_y_new = model.predict([[new_value]])
print(f"Predicted Y for new value {new_value}: {predicted_y_new}")

# Plotting the regression line in a new window
plt.figure()  # Create a new figure
sns.regplot(x="X", y="Y", data=data)
plt.show()  # Show the plot in a new window
