# Dataframe-2
# With custom labels  = index param


import pandas as pd

df = pd.DataFrame(
    {
        "Name": ["Tom", "Jon", "Emily", "Alice"],
        "Age": [20, 18, 32, 27],
        "Loc": ["Paris", "Aus", "Japan", "India"],
    },
    index=["a", "b", "c", "d"],
)

print(df)

# ACCESSING ROWS:
# 1 - use loc = label based selection / row/col name =labels
# df.loc[]

row2 = df.loc["b"]
print(row2)

# multiple rows  [[ ]]

rows = df.loc[["a", "c"]]
print(rows)

# specific value

loc = df.loc["c", "Loc"]
print(loc)

# subset of rows and cols

sub = df.loc[["b", "d"]], ["Name", "Age"]
#             rows          cols
print(sub)

# conditonal(filtering)
fil = df.loc[df["Age"] > 25]
print(fil)

# multiple conditions :

fil2 = df.loc[(df["Loc"] == "India") & (df["Age"] > 18)]
print(fil2)

# Slicing

slic = df.loc["a":"c"]
print(slic)
