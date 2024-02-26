import os
import pandas as pd

os.system("clear")

data = {
    "Brand": ["Ford", "Ford", "Ford"],
    "Model": ["Sierra", "F-150", "Mustang"],
    "Typ": ["2.0 GL", "Raptor", "Mach-E, Mach-1"],
}
df = pd.DataFrame(data)

# Explode the "country" column to split the comma-separated values into separate rows
df_expanded = df.assign(Type_new=df["Typ"].str.split(", ")).explode(
    "Type_new", ignore_index=True
)

# df_expanded = df.assign(country_new=df["country"].str.split(", "))

print(df)
print("-----------------")
print(df_expanded)
