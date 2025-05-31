# Categorical Variables = catplot()

# 1 - Categorical-Distribution Plots

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("Seaborn/Dataset/1651277648862_healthinsurance.csv")

# 1- Strip Plot

sns.catplot(x="sex", y="weight", data=df)
plt.show()

sns.catplot(
    x="sex", y="age", data=df, hue="diabetes", jitter=0.05
)  # jitter = better visibilty on hue
plt.show()

""" 
2 - Swarm Plot = Strip plot with no overlapping points

COMPUTATIONALLY HEAVY = TAKES TOO LONG TO PROCESS.

sns.catplot(x="sex", y="diabetes", data=df, kind="swarm")
plt.show()


"""


"""
1 = Discrete and Continuous
    (class)       (reg)


2 = Categorical and Quantitative
    (string)         (numbers)


"""
