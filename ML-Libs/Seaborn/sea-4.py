# Categorical-Estimate Plots(Central Tendency)


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv("Seaborn/Dataset/1651277648862_healthinsurance.csv")

# Bar Plot

sns.catplot(x="sex", y="diabetes", kind="bar", data=df, hue="smoker")
plt.show()


# Count Plot = freq of each category.

sns.catplot(x="hereditary_diseases", kind="count", data=df)
plt.show()


# Histograms = discrete data = bins
# displot()

sns.displot(x="claim", kind="hist", data=df, bins=20, col="sex")
plt.show()

# kde = pdf is calculated of continuous data

sns.displot(x="claim", data=df, kde=True)
plt.show()

""" or use : kdeplot()
sns.kdeplot(data=df, x="age", y="claim", fill=True, cmap="viridis")
plt.show()
"""
# kde + hist

sns.displot(data=df, x="age", col="sex", kde=True, bins=30)
plt.show()
