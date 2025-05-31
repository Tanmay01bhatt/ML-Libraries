# Comparing 2 Distributions :
# Using a Dictionary

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "normal": random.normal(loc=3, scale=5, size=1000),
    "poisson": random.poisson(lam=10, size=1000),
}

sns.displot(data, kind="kde")
plt.show()
