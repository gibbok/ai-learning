import pandas as pd

# Create a DataFrame with a single column 'review' and some empty rows
data = {"review": ["This is a review.", None, "Another review.", "", "Last review."]}
df = pd.DataFrame(data)

# Print the DataFrame before removing empty rows
# print("DataFrame before:")
# print(df)

# Remove empty rows using two approaches:
# 1. Drop rows with any kind of missing values (NaN, None, '')
# df_filtered1 = df.dropna(subset=["review"], how="any")

# 2. Explicitly handle empty strings, ensuring 'review' column has non-empty strings
df_filtered2 = df[df["review"].str.strip() != ""]

# Print both DataFrames after filtering
# print("DataFrame after removing empty rows with 'dropna':")
# print(df_filtered1)
# print("DataFrame after removing empty rows with string checks:")
print(df_filtered2)
