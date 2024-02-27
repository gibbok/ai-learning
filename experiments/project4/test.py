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

# given a title show me all other titles in the same category
# give a title, give me its category
# search all titles for a category
target_category = df[df["title"] == "movie a"].drop_duplicates().head()["listed_in_new"]

movies_in_category = df[df["listed_in_new"].isin(target_category)].drop_duplicates()
print("Movies in the", target_category.iloc[0], "category:")
print(movies_in_category["title"].tolist())
