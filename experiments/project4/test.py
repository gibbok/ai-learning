import os
import pandas as pd
import json
import matplotlib.pyplot as plt

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

# Group by release_year and count the occurrences of each type
type_count_by_year = (
    df.groupby(["release_year", "type"]).size().unstack(fill_value=0).transpose()
)


print(type_count_by_year)

# Plotting
for col in type_count_by_year.columns:
    plt.plot(type_count_by_year.index, type_count_by_year[col], marker="o", label=col)
plt.title("Number of Releases by Type Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Releases")
plt.legend()
plt.grid(True)
plt.show()
