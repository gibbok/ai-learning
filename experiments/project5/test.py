import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [25, 30, 35, 40, 45],
    "City": ["New York", "Los Angeles", "Chicago", "New York", "New York"],
    "City_Enum": [0, 1, 2, 0, 0],
}

# Create DataFrame
df = pd.DataFrame(data)

# Mapping of city enumeration to city names
city_map = {0: "New York", 1: "Los Angeles", 2: "Chicago"}

# Map numerical values to city names
df["City"] = df["City_Enum"].map(city_map)

# Plot KDE plot
sns.kdeplot(data=df, x="City_Enum")
plt.xticks(
    ticks=df["City_Enum"].unique(), labels=df["City"].unique(), rotation=45
)  # Set the xticks to city names
plt.xlabel("City")
plt.ylabel("Density")
plt.title("Density Plot of Cities")
plt.show()
