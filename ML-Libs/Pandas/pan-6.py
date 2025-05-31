# Analysing Dataframes/Datasets -1

import pandas as pd

df = pd.read_csv(
    "https://gitlab.com/AnalyticsIndiaMagazine/practicedatasets/-/raw/main/bootcamp/logistic_regression/diabetes.csv"
)

# head() = print top 5 rows

print(df.head())

# for top 10 rows :

print(df.head(10))

# tail() = last 5 rows

print(df.tail())

# shape = row x col or depth x row x col if 3-D dataset

print(df.shape)  # (768, 9)

# index = all row labels

print(df.index)  # RangeIndex(start=0, stop=768, step=1)

# columns = all col labels

print(df.columns)

# dtypes = gets the datatype (of the entire dataset or a specific col if you want )

print(df.dtypes)

# info() = summary of dataset : total rows,cols,memory usage,dtypes,etc.

print(df.info())
