import os
import pandas as pd

os.system("clear")

data = {
    "title": ["Film A", "Film B", "Film C"],
    "country": ["USA", "UK", "UK"],
    "listed_in": ["action, drama", "drama", "drama"],
}
df = pd.DataFrame(data)

# explode the "country" column to split the comma-separated values into separate rows
df_expanded = df.assign(listed_in_new=df["listed_in"].str.split(", ")).explode(
    "listed_in_new", ignore_index=True
)

print(df)
print("-----------------")
print(df_expanded[["title", "country", "listed_in_new"]])

# how many `listed_in` we have?
print("-----------------")
df_grouped_listed_in = df_expanded.groupby(["listed_in_new"]).count()
print(df_grouped_listed_in)

# list how many `listed_in` we have per `country`?
df_grouped_country = df_expanded.groupby(["country"]).count()
print("-----------------")
print(df_grouped_listed_in)

print("-----------------")
# Group by 'country' and aggregate the 'listed_in' column
result = df_grouped_listed_in.groupby("country")["listed_in_new"]

print(result)
