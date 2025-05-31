# As the size of dataset increases =  scatter plots become less and less useful

# in such cases we use :

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv("Seaborn/Dataset/1651277648862_healthinsurance.csv")

# 1- Boxplot = anomaly detection = uses q1,q2,q3,max,min values
# y col = numerical

sns.catplot(x="sex", y="age", data=df, kind="box")
plt.show()

# 2- Boxen Plot
# Plots using different quartile values (more than q1,q2,q3)
# therefore provides more detailed insight of data.

sns.catplot(x="sex", y="age", data=df, kind="boxen", hue="smoker")
plt.show()
