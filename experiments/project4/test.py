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

# Count unique elements in column 'A'
unique = df["listed_in_new"].unique()
# print(df)

filtered_df = df[df["country"] == "usa"]

# Extract the titles from the filtered DataFrame

# Print the titles
# print(filtered_df)

# Loop through each unique country and print titles
# for country in df["country"].unique():
#     filtered_df = df[df["country"] == country]
#     titles_country = filtered_df["title"].tolist()
#     print(f"Titles from {country}: {titles_country}")


temp_dict = {}

# Loop through each unique country and filter titles
for country in df["country"].unique():
    filtered_df = df[df["country"] == country]
    titles_country = filtered_df["title"].unique().tolist()
    temp_dict[country] = titles_country

# print(temp_dict)

json_string = json.dumps(temp_dict, indent=4)
print(json_string)
