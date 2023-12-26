"""
Calculate Food Expenditures based on historical data.
The result are reported in both CZK and EUR currencies.
"""

from sklearn.linear_model import LinearRegression
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import requests

print(pd.__version__)

# Get latest currency rates
response = requests.get("https://open.er-api.com/v6/latest/EUR").json()
czk_rate = None
if "rates" in response:
    czk_rate = response["rates"]["CZK"]
else:
    raise Exception("Could not get rates")

# Read data
data = pd.read_csv("./data/expenditures.csv")

# Get years as positive numbers
years = data["years"].abs()
# Get food_cost as positive numbers, and fill missing values with average from prev and next rows
food_cost = data["food_shared"].abs().interpolate(method="linear")

data_sanitized = pd.DataFrame({"years": years, "food_shared": food_cost})

X = data_sanitized[["years"]]  # Features (independent variable)
y = data_sanitized["food_shared"]  # Target (dependent variable)

# Initialize the Linear Regression model and train the model
model = LinearRegression()
model.fit(X, y)

# Make a future prediction
new_year = 2024
predicted_y = model.predict([[new_year]])

# Rate conversions
predicted_y_eur = predicted_y / czk_rate
predicted_y_month = predicted_y / 12
predicted_y_month_eur = predicted_y_month / czk_rate

print(
    f"Predicted food_share for year {new_year}: {predicted_y} CZK or {predicted_y_eur} EUR"
)
print(
    f"Predicted food_share per month is {predicted_y_month} CZK or {predicted_y_month_eur} EUR"
)

# Predict using the trained model
predicted_y_trained = model.predict(X)
predicted_y_trained_df = pd.DataFrame(
    {"years": years, "food_shared": predicted_y_trained}
)

# Plotting the regression line in a new window
# Create a figure with 1 row and 2 columns
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# First regplot
sns.regplot(x="years", y="food_shared", data=data_sanitized, ax=axes[0])
axes[0].set_title("Historical Data")

# Second regplot
sns.regplot(x="years", y="food_shared", data=predicted_y_trained_df, ax=axes[1])
axes[1].set_title("Forecast")

plt.show()
