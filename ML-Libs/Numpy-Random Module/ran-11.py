# Exponential Distribution

# params:
# scale = average time b/w events / inverse of lambda(1/lambda)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.exponential(scale=2, size=10000)
sns.displot(x, kind="kde")
plt.show()
