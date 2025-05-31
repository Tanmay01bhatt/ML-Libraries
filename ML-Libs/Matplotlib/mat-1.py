# Plot a simple line graph with 2 points

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 6])
y = np.array([0, 250])

plt.plot(x, y)
plt.show()


# 2 pomits = a : (1,3) and b = (8,10)
# x = 1 , 8
# y = 3 ,10

x_p = np.array([1, 8])
y_p = np.array([3, 10])

plt.plot(x_p, y_p, "o")  # dots at the exact points
plt.show()
