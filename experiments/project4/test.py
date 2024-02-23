import pandas as pd

data = pd.DataFrame(
    {
        "title": ["Dick Johnson Is Dead"],
        "listed_in": ["Documentaries, International TV Shows, TV Dramas, TV Mysteries"],
    }
)

# Split the 'listed_in' column into a list and then explode it into separate rows
data = (
    data.assign(listed_in=data["listed_in"].str.split(", "))
    .explode("listed_in")
    .reset_index(drop=True)
)

print(data)
