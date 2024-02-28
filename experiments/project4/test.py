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
}
df = pd.DataFrame(data)
# Build a dataframe with 4 connections
df = pd.DataFrame({"from": ["A", "B", "C", "A"], "to": ["D", "A", "E", "C"]})

# Build your graph
G = nx.from_pandas_edgelist(df, "from", "to")

# Plot it
nx.draw(G, with_labels=True)
plt.show()
