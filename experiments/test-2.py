import pandas as pd
import matplotlib.pyplot as plt

# Given DataFrame
data = {
    "title": ["Film A", "Film B", "Film C"],
    "country": ["USA", "UK", "UK"],
    "listed_in": ["action, drama", "drama", "drama"],
}
df = pd.DataFrame(data)

# Split the 'listed_in' column by comma and strip whitespace
df["listed_in"] = (
    df["listed_in"].str.split(",").apply(lambda x: [item.strip() for item in x])
)

# Group by 'country' and aggregate the 'listed_in' column
result = df.groupby("country")["listed_in"].agg(
    lambda x: [y for sublist in x for y in sublist]
)

# Create a dictionary to store the count of each genre for each country
genre_counts = {}
for country, genres in result.items():
    genre_counts[country] = pd.Series(genres).value_counts()

# Plotting
plt.figure(figsize=(10, 6))

# Scatter plot each genre for each country
for i, (country, counts) in enumerate(genre_counts.items()):
    plt.scatter(
        [i] * len(counts), counts.index, s=counts.values * 100, label=country, alpha=0.5
    )

plt.xlabel("Country")
plt.ylabel("Listed In")
plt.title("Listed In Genres by Country")
plt.xticks(range(len(genre_counts)), genre_counts.keys())
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
