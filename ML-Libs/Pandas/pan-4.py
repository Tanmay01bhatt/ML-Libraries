# iloc = Index based Selection

import pandas as pd

df = pd.DataFrame(
    {
        "Name": ["Tom", "Ron", "Bob", "Emily"],
        "Age": [18, 24, 42, 33],
        "City": ["London", "Paris", "Australia", "Japan"],
    }
)

print(df)

# 1 row

r1 = df.iloc[1]
print("\n", r1)

# 1st and 3rd row

r2 = df.iloc[[0, 2]]
print(r2)

# get a spcific value

val = df.iloc[2, 1]  # 2nd row 1st col element
print(val)

# Slicing

slice = df.iloc[1:4]
print(slice)

# slice 1st 3 rows and 1st 2 cols

s2 = df.iloc[0:3, 0:2]
print(s2)

# rows 1 to 4 and col 2 to 4

s3 = df.iloc[1:4, 2:4]
print(s3)


"""
LABELS VS INDEX

LABEL = INDIVIDUAL NAME : 'a','name','age','x','y'

INDEX = COLLECTION OF LABELS : Index ['x','y','z']
                                    OR
                               Index['Name','Age','loc']     

"""

# df.index =  all row labels

# df.columns =  all col labels
