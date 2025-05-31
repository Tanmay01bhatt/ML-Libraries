# Seaborn =  easy to work  with datasets
# less code (than matplot)

"""
BASICS :
If you want to plot a :

1 - Bar Graph : sns.barplot()
2 - Boxplot : sns.boxplot()
3 - Scatter : sns.scatter() ... etc

All are used for simple and direct comparisions of data.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Replot = ideal for comparision of patterns across categories.

df = pd.read_csv("Seaborn/Dataset/1651277648862_healthinsurance.csv")
# print(df.head())

"""
error resolved :
import os
print("Current working directory:", os.getcwd())
"""
# Scatter Plot

sns.relplot(x="age", y="weight", data=df, kind="scatter")
plt.show()

# hue = color based on a 3rd category or column

sns.relplot(x="age", y="weight", data=df, kind="scatter", hue="sex")
plt.show()

# style = using a 4th cat differenciates groups by marker shape(.*+^) or pattern(ls = : -.)

sns.relplot(
    x="age", y="weight", data=df, kind="scatter", hue="sex", style="hereditary_diseases"
)
plt.show()

# col = creates subplots based on a seperate category

sns.relplot(x="age", y="weight", data=df, kind="scatter", hue="sex", col="diabetes")
plt.show()


# LinePLot
sns.relplot(x="age", y="weight", data=df, kind="line", hue="sex")
plt.show()
