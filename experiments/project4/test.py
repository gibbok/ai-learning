import os
import pandas as pd

os.system("clear")

# Example DataFrame
data = {
    "listed_in_new": ["drama", "commedy", "drama", "action", "action"],
}
df = pd.DataFrame(data)

# Count unique elements in column 'A'
unique = df["listed_in_new"].unique()


print("Unique in column 'A':", unique)
