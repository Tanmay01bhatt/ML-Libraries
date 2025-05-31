# Cleaning Data-2

import pandas as pd

data = pd.read_csv(
    "https://raw.githubusercontent.com/analyticsindiamagazine/MocksDatasets/main/Customer_Missing.csv"
)

# improvise a dataset to use dropna

# replacing the empty sreing with NaN values

df1 = data.replace(" ", pd.NA)
df1.dropna(inplace=True)
print(df1.isnull().sum())


# Forward fill = fill the missing values with the prev col value(the col above)

df2 = data.fillna(method="ffill")
print(df2)

# Backward fill = fill the missing values with the next col value (the col above)

df3 = data.fillna(method="bfill")
print(df3)


# Removing dumplicates rows

print(df3.duplicated())
df3.drop_duplicates(inplace=True)

# True = duplicated row
# False = No duplication
