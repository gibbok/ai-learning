import os
import pandas as pd
import json
import matplotlib.pyplot as plt
import networkx as nx

os.system("clear")

# Example DataFrame
data = {
    "title": ["Terminator", "Titanic", "movie b", "movie c", "True Lies"],
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
        "James Cameron",
        "director_b",
        "director_c",
        "James Cameron",
    ],
    "cast_new": [
        "Arnold Schwarzenegger",
        "Leonardo DiCaprio",
        "cast_b",
        "cast_b",
        "Arnold Schwarzenegger",
    ],
}
df = pd.DataFrame(data)

grouped = df[["director_new", "cast_new"]]

print(grouped)

df_network = pd.DataFrame({"from": grouped["director_new"], "to": grouped["cast_new"]})

graphic = nx.from_pandas_edgelist(df_network, "from", "to")

nx.draw(graphic, with_labels=True)
plt.show()
