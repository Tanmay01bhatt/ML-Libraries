# 1- Read Csv

import pandas as pd

df = pd.read_csv(
    "https://gitlab.com/AnalyticsIndiaMagazine/practicedatasets/-/raw/main/bootcamp/logistic_regression/diabetes.csv"
)

print(df)

"""
df.to_string() = always print the ENTIRE Dataframe
                does NOT obey the max_rows setting


print(df) =  prints a shortened versions
        obeys the max row setting(param)
"""

"""

2 - Read JSON = stores big datatsets

df2 = pd.read_json("data.json")
print(df2.to_string())


"""


"""
3 - Read Excel = for excel files

df3 = pd.read_excel('file.xlsx', sheet_name = 1) # if you want to read a specific sheet

                    OR

df4 = pd.read_excel('file.xlsx', use_cols='A:E',nrows = 5) # you you want to read and analyse specific rows and columns.

"""
