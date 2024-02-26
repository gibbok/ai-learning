import os
import pandas as pd

os.system("clear")

# Read
dir_path = "./experiments/project4/"
df = pd.read_csv(os.path.join(dir_path, "data.csv"))[0:5]

# Remove rows with no 'country'
df = df.dropna(subset=["country"])

# Split columns with values as stringo into a list and then explode it into separate rows
df = (
    df.assign(listed_in_new=df["listed_in"].str.split(", "))
    .explode("listed_in_new")
    .reset_index(drop=True)
)

df = df.assign(country_new=df["country"].str.split(", ")).explode(
    "country_new", ignore_index=True
)

df = df.assign(director_new=df["director"].str.split(", ")).explode(
    "director_new", ignore_index=True
)

df = df.assign(cast_new=df["cast"].str.split(", ")).explode(
    "cast_new", ignore_index=True
)


# print(df)
# Count how many categories we have
grouped_data = df.groupby(["listed_in_new"]).count()
print(grouped_data)

# df.to_csv(os.path.join(dir_path, "results.csv"), index=False)
# grouped_data.to_csv(os.path.join(dir_path, "results_grouped.csv"), index=False)

# Count how many categories we have for each country
