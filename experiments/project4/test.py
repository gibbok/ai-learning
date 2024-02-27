import os
import pandas as pd
import json
import matplotlib.pyplot as plt

os.system("clear")

# Example DataFrame
data = {
    "title": ["movie a", "movie a", "movie b", "movie c", "movie d"],
    "listed_in_new": [
        "drama",
        "drama",
        "commedy",
        "drama",
        "drama",
    ],
    "country": ["usa", "usa", "usa", "ita", "ita"],
}
df = pd.DataFrame(data)

# Group the DataFrame by 'listed_in_new' and get the titles
grouped_titles = df.groupby("listed_in_new")["title"]

print(grouped_titles)

# Loop through each group and print its category and titles
# for category, titles in grouped_titles:
#     print(f"Category: {category}")
#     print(*titles.tolist(), sep="\n")  # Print titles one per line
#     print("-" * 10)  # Print a separator for clarity
