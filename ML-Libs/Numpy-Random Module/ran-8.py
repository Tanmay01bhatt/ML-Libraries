# Binomial Distribution

# params:
# n = no. of trials
# p = probab of occurence of each trial
# size = shape of array

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.binomial(n=10, p=0.5, size=1000)
sns.displot(x)
plt.show()
