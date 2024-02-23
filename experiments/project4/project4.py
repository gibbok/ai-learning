import os
import pandas as pd

dir_path = "./experiments/project4/"
df = pd.read_csv(os.path.join(dir_path, "data.csv"))

df_1 = df[["country", "listed_in"]]
print(len(df_1))
df_1 = df.dropna(subset=["country"])
print(df_1[:100])

df_1.to_csv(os.path.join(dir_path, "results.csv"), index=False)
