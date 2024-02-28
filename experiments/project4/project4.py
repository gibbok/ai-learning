import os
import pandas as pd
import json
import matplotlib.pyplot as plt
import networkx as nx

os.system("clear")

# Read
dir_path = "./experiments/project4/"
df = pd.read_csv(os.path.join(dir_path, "data.csv"))[0:50]

# Remove rows with no 'country'
df = df.dropna(subset=["country"])

# Split columns with values as string into a list and then explode it into separate rows
df = (
    df.assign(listed_in_new=df["listed_in"].str.split(", "))
    .explode("listed_in_new")
    .reset_index(drop=True)
)
df = df.assign(country_new=df["country"].str.split(", ")).explode(
    "country_new", ignore_index=True
)
df = df.assign(director_new=df["director"].str.split(", ")).explode(
    "director_new", ignore_index=True
)
df = df.assign(cast_new=df["cast"].str.split(", ")).explode(
    "cast_new", ignore_index=True
)

print(df)

print("\n------ List all categories in all country")
unique_listed_in_new = df["listed_in_new"].unique()
print(unique_listed_in_new)

print("\n------ List all titles in all country")
unique_title = df["title"].unique()
print(unique_title)

print("\n------ List all titles by country")
temp_dict = {}
for country in df["country"].unique():
    filtered_df = df[df["country"] == country]
    titles_country = filtered_df["title"].unique().tolist()
    temp_dict[country] = titles_country
json_string_titles = json.dumps(temp_dict, indent=4)
print(json_string_titles)

print("\n------ List all category by country")
temp_dict_listed_in_new = {}
for country in df["country"].unique():
    filtered_df = df[df["country"] == country]
    listed_in_new_country = filtered_df["listed_in_new"].unique().tolist()
    temp_dict_listed_in_new[country] = listed_in_new_country
json_string_category = json.dumps(temp_dict_listed_in_new, indent=4)
print(json_string_category)

print("\n------ Given a title show all other titles in the same category)")
target_category = (
    df[df["title"] == "Angry Birds"].drop_duplicates().head()["listed_in_new"]
)
movies_in_category = df[df["listed_in_new"].isin(target_category)]
movies_in_category_list = set(movies_in_category["title"].to_list())
print(movies_in_category_list)

print("\n------ List all titles in every category")
grouped_titles = df.groupby("listed_in_new")["title"].apply(pd.Series.unique)
for category, titles in grouped_titles.items():
    print(f"Category: {category}")
    print(*titles.tolist(), sep="\n")
    print("-" * 10)

# print("\n------ Show number of TV shows compare to movies by year with a chart")
# type_count_by_year = df.groupby(["release_year", "type"]).size().unstack(fill_value=0)
# type_count_by_year = type_count_by_year.reset_index()
# release_year = type_count_by_year["release_year"].to_list()
# plt.title("Number of Releases by Type Over Years")
# plt.xlabel("Year")
# plt.ylabel("Number of Releases")
# for type_value in type_count_by_year.columns:
#     if type_value == "release_year":
#         continue
#     count_values = []
#     for x in type_count_by_year[type_value]:
#         count_values.append(x)
#     plt.plot(release_year, count_values, label=type_value)
# plt.legend()
# plt.show()

print("\n------ Show Network analysis of Actors / Directors")
grouped = df[["director_new", "cast_new"]]
print(grouped)
df_network = pd.DataFrame({"from": grouped["director_new"], "to": grouped["cast_new"]})
graphic = nx.from_pandas_edgelist(df_network, "from", "to")
nx.draw(graphic, with_labels=True)
plt.show()
