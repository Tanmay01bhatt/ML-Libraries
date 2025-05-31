# Poisson Distribution

# params
# lam = rate of occurrence (within a specified duration of time)
# size = shape of array

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.poisson(lam=2, size=1000)
sns.displot(x)
plt.show()
