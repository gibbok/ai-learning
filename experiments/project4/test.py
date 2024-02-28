import os
import pandas as pd
import json
import matplotlib.pyplot as plt
import networkx as nx

os.system("clear")

# Example DataFrame
data = {
    "title": ["movie a", "movie a", "movie b", "movie c", "movie d"],
    "type": ["tv", "cinema", "tv", "cinema", "cinema"],
    "release_year": [2020, 2020, 2021, 2022, 2022],
    "listed_in_new": [
        "drama",
        "drama",
        "commedy",
        "drama",
        "drama",
    ],
    "country": ["usa", "usa", "usa", "ita", "ita"],
    "director_new": [
        "director_a",
        "director_b",
        "director_b",
        "director_c",
        "director_d",
    ],
    "cast_new": ["cast_a", "cast_a", "cast_b", "cast_b", "cast_c"],
}
df = pd.DataFrame(data)

grouped = (
    df.groupby("title")["director_new"].apply(list).reset_index(name="director_new")
)
new_df = grouped.explode("director_new")

print(new_df)

# # Build a dataframe with 4 connections
# df = pd.DataFrame(
#     {"from": ["A", "B", "C", "A", "A", "B"], "to": ["D", "A", "E", "C", "E", "E"]}
# )

# # Build your graph
# G = nx.from_pandas_edgelist(df, "from", "to")

# # Plot it
# nx.draw(G, with_labels=True)
# plt.show()
