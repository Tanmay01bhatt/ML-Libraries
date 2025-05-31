# Pandas  = refers to 'Panel Data' or 'Python Data Analysis'

# Core Data Structures:

# 1 - Series = 1-D Array / column on a table

import pandas as pd

ser = pd.Series([10, 20, 30, 40, 50])  # pass a 1-D array to it.

print(ser)

print(ser[3])

# With Labels :

ser2 = pd.Series([1, 3, 5, 7, 9, 11], index=["a", "b", "c", "d", "e", "f"])
print(ser2)

print(ser2["d"])


# Can also use dictionaries (Not Recommended) = Always use 1-d arrays(logically correct)

cal = {"d1": 100, "d2": 400, "d3": 500}
ser3 = pd.Series(cal)
print(ser3)
print(ser3["d2"])
