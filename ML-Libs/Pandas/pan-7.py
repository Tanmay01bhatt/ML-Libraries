# Analysing Datasets/Dataframes

import pandas as pd

df = pd.read_csv(
    "https://gitlab.com/AnalyticsIndiaMagazine/practicedatasets/-/raw/main/bootcamp/logistic_regression/diabetes.csv"
)

# 2 - Summary Statistics

# describe() = mean,standard dev,quratiles,median,mode,max,min,etc

print(df.describe())

# column-wise statistics

print(df["Age"].mean())
print(df["Age"].sum())
print(df["Age"].max())


# 3 - Distribution of Values
data = pd.read_csv(
    "https://raw.githubusercontent.com/analyticsindiamagazine/MocksDatasets/main/Data%20Science%20Salary.csv"
)

# value_counts() = freq of each unique value in a col.

print(data["Location"].value_counts())

# unique() = a list of all different values present/unique values .

print(data["Location"].unique())

# nunique = no. of unique values present

# isnull() = finds the number of null values present.

# in the entire dataset

print(data.isnull().sum())

# in a column :

print(data["Location"].isnull().sum())
