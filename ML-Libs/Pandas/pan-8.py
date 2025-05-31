# Cleaning Data -1

import pandas as pd

data = pd.read_csv(
    "https://raw.githubusercontent.com/analyticsindiamagazine/MocksDatasets/main/Customer_Missing.csv"
)

print(data.head())

# Find NULL Values

print(data.isnull().sum())

# Removing/Cleaning NULL Values = dropna()

data2 = data.dropna()  # returns a new dataframe

# if you want to make changes in the original dataframe itself :-

# data.dropna(inplace=True)

print(data2.isnull().sum())


# Repalcing NULL Values : fillna()

# fill in a specific value

data3 = data.copy()

df = data3.fillna(60)
print(df.isnull().sum())

# in the org dataset = inplace = True

# only a specific col

df2 = data3["Cust_City"].fillna("Home")
print(df2)

# if whole dataset is used : data["Cust_City"].fillna(60,inplace="True")

# using mean/median/mode


mean1 = data3["Cust_Age"].mean()

df4 = data3["Cust_Age"].fillna(mean1)
print(df4)
