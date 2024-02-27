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
type_count_by_year = df.groupby(["release_year", "type"]).size().unstack(fill_value=0)
type_count_by_year = type_count_by_year.reset_index()

release_year = type_count_by_year["release_year"].to_list()
print(release_year)
for type_value in type_count_by_year.columns:
    count_values = []
    for x in type_count_by_year[type_value]:
        count_values.append(x)
    plt.plot(release_year, count_values, label=type_value)
    # print(type_count_by_year["release_year"], count_values, type_value)
    print("----")


plt.legend()
plt.show()

# release_year = type_count_by_year
# type_cinema = [10, 20, 20]
# type_tv = [5, 18, 30]
# plot line
# plt.plot(release_year, type_cinema, label="cinema")
# plt.plot(release_year, type_tv, label="tv")
