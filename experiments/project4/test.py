import os
import pandas as pd

os.system("clear")

data = {
    "Name": ["Film A", "Film B", "Film C"],
    "Country": ["USA", "UK", "ITA"],
    "Type": ["action, drama", "drama", "drama"],
}
df = pd.DataFrame(data)

# Explode the "country" column to split the comma-separated values into separate rows
df_expanded = df.assign(Type_new=df["Type"].str.split(", ")).explode(
    "Type_new", ignore_index=True
)

print(df)
print("-----------------")
print(df_expanded[["Name", "Country", "Type_new"]])

df_grouped = df_expanded.groupby("Type_new").count()

print("-----------------")
print(df_grouped)
