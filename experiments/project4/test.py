import os
import pandas as pd
import json
import matplotlib.pyplot as plt
import networkx as nx

os.system("clear")

# Example DataFrame
data = {
    "title": ["Terminator", "movie a", "movie b", "movie c", "True Lies"],
    "type": ["cinema", "cinema", "tv", "cinema", "cinema"],
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
        "James Cameron",
        "director_b",
        "director_b",
        "director_c",
        "James Cameron",
    ],
    "cast_new": [
        "Arnold Schwarzenegger",
        "cast_a",
        "cast_b",
        "cast_b",
        "Arnold Schwarzenegger",
    ],
}
df = pd.DataFrame(data)

grouped = df.groupby(["director_new", "cast_new"]).size().reset_index(name="count")


print(grouped)

# df_network = pd.DataFrame(
#     {"from": ["A", "B", "C", "A", "A", "B"], "to": ["D", "A", "E", "C", "E", "E"]}
# )

# # Build a dataframe with 4 connections
# df = pd.DataFrame(
#     {"from": ["A", "B", "C", "A", "A", "B"], "to": ["D", "A", "E", "C", "E", "E"]}
# )

# # Build your graph
# G = nx.from_pandas_edgelist(df, "from", "to")

# # Plot it
# nx.draw(G, with_labels=True)
# plt.show()
