# 2- DataFrame : 2-D Array / rows and cols (table)

# Dictionaries are always used for df creation.

import pandas as pd


data = {"cal": [420, 530, 300, 569, 700], "time": [30, 45, 25, 40, 120]}

df = pd.DataFrame(data)
print(df)

# key = column name
# value = an array of values

col1 = df["time"]
print(col1)  # accessing columns using []
