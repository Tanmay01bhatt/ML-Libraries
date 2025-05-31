# Uniform Distribution

# params :
# low = lower bound(def=0.0)
# high = upper bound(def=1.0)
# size = sample size/shape of the array

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.uniform(low=0.0, high=1.0, size=1000)
sns.displot(x, kind="kde")
plt.show()
