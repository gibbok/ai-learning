import pandas as pd

data = {
    "age": [39, 50],
    "workclass": [
        " State-gov",
        " Self-emp-not-inc",
    ],
    "fnlwgt": [
        77516,
        83311,
    ],
    "education": [
        " Bachelors",
        " Bachelors",
    ],
    "education-num": [
        13,
        13,
    ],
    "marital-status": [
        " Never-married",
        " Married-civ-spouse",
    ],
    "occupation": [
        " Adm-clerical",
        " Exec-managerial",
    ],
    "relationship": [
        " Not-in-family",
        " Husband",
    ],
    "race": [
        " White",
        " White",
    ],
    "sex": [
        " Male",
        " Male",
    ],
    "capital-gain": [
        2174,
        0,
    ],
    "capital-loss": [
        0,
        0,
    ],
    "hours-per-week": [
        40,
        13,
    ],
    "native-country": [
        " United-States",
        " United-States",
    ],
    "salary": [
        " <=50K",
        " <=50K",
    ],
}

df = pd.DataFrame(data)
print(df)
