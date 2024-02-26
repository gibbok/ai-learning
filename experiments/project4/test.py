import os
import pandas as pd

os.system("clear")

# Example DataFrame
data = {"A": [1, 2, 3, 1, 2, 3], "B": ["a", "b", "a", "a", "c", "c"]}
df = pd.DataFrame(data)

# Count unique elements in column 'A'
unique_count_A = df["A"].nunique()

# Count unique elements in column 'B'
unique_count_B = df["B"].nunique()

print("Unique count in column 'A':", unique_count_A)
print("Unique count in column 'B':", unique_count_B)
