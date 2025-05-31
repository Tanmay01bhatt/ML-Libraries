# Heatmap = like 2-D Arrays
# Each numeric value corresponds to color intensity

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv(
    "https://gitlab.com/AnalyticsIndiaMagazine/practicedatasets/-/raw/main/bootcamp/random_forest_regression/advertising.csv"
)

# Sample

arr = np.array([[1, 2, 3], [4, 5, 6], [6, 7, 8]])
sns.heatmap(arr)
plt.show()

# Using a dataset
"""
DataFrame.pivot(index, columns, values)
 pivot with 1 index column, 1 column to pivot, and 1 value to fill.
data_pivot = df.pivot(index="TV", columns="Radio", values="Sales")  # cols of the dataset
sns.heatmap(data_pivot)
plt.show()
"""
# converts a long format dataset to 2d array.(only takes in three agrs)

# Coreelation matrices
corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
# show corr vales            # center cmap at 0
plt.show()
