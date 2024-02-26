import os
import pandas as pd

os.system("clear")

# Example DataFrame
data = {
    "title": ["movie a", "movie b", "movie c"],
    "listed_in_new": [
        "drama",
        "commedy",
        "drama",
    ],
    "country": ["usa", "usa", "ita"],
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
    titles_country = filtered_df["title"].tolist()
    # Create a temporary dictionary for current country
    temp_dict[country] = titles_country

print(temp_dict)
# Concatenate the list of dictionaries into a DataFrame
# final_df = pd.concat(all_titles_df, ignore_index=True)

# Print the final DataFrame with titles by country
# print(final_df)
