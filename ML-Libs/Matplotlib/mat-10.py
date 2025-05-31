# Scatter Plots = plt,scatter(x,y)  # does not give default x values

import numpy as np
import matplotlib.pyplot as plt

x = np.array([3, 8, 12, 4, 25, 10])
y = np.array([0, 1, 2, 3, 4, 5])
b = np.array([50, 40, 30, 20, 10, 0])

plt.scatter(x, y, c="r")
plt.show()


# Comparing 2 scatter plots :

plt.scatter(x, y, c="g")
plt.scatter(b, y, c="b")
plt.show()


# Assign Individual color to each dot

colors = ["red", "green", "blue", "yellow", "black", "pink"]
plt.scatter(b, y, c=colors)
plt.show()
