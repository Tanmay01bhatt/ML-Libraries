# Distributions

# Normal Distribution

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

x = random.normal(size=(2, 3))

print(x)  # random distribution of size =(2x3)


# parameters :
#  loc = mean value
# scale =  standard deviation
# size =  shape of array

y = random.normal(loc=1, scale=2, size=(2, 3))

y = y.flatten()  # (6,)
# displot accepts only 1-D arrays

sns.displot(y, kind="kde")
plt.show()
