# Color Map = maps colors to numerical values


import numpy as np
import matplotlib.pyplot as plt

x = np.array([3, 8, 12, 4, 25, 10])
y = np.array([0, 1, 2, 3, 4, 5])
a = np.array([50, 40, 30, 20, 10, 0])

colors = [10, 20, 15, 30, 40, 60]

plt.scatter(x, y, c=colors, cmap="viridis")
plt.colorbar()
plt.show()

# The number of values in color array = = the no values in x and y.

x = np.arange(102)
y = np.arange(102)

colors2 = np.random.randint(1000, size=102)

plt.scatter(x, y, c=colors2, cmap="plasma")
plt.show()

"""
Popular c-maps :
viridis
inferno
plasma
coolwarm
tab10
twilight
set1
rainbow
winter

"""
