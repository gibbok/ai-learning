import os
import pandas as pd

os.system("clear")

# Read
dir_path = "./experiments/project4/"
df = pd.read_csv(os.path.join(dir_path, "data.csv"))

# Remove rows with no country
df = df.dropna(subset=["country"])


# Split the 'listed_in' column into a list and then explode it into separate rows
df = (
    df.assign(listed_in=df["listed_in"].str.split(", "))
    .explode("listed_in")
    .reset_index(drop=True)
)


df.to_csv(os.path.join(dir_path, "results.csv"), index=False)
