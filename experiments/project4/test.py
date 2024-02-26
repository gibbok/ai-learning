import os
import pandas as pd

os.system("clear")

data = {
    "title": ["Film A", "Film B", "Film C"],
    "country": ["USA", "UK", "UK"],
    "listed_in": ["action, drama", "drama", "drama"],
}
df = pd.DataFrame(data)

# Explode the "country" column to split the comma-separated values into separate rows
df_expanded = df.assign(listed_in_new=df["listed_in"].str.split(", ")).explode(
    "listed_in_new", ignore_index=True
)

print(df)
print("-----------------")
print(df_expanded[["title", "country", "listed_in_new"]])

df_grouped = df_expanded.groupby(["listed_in_new"]).count()

# ho2 many listed_in we have?
print("-----------------")
print(df_grouped)
