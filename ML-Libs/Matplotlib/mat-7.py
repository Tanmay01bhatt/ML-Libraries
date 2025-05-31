# Labels

import numpy as np
import matplotlib.pyplot as plt

x_p = np.array([3, 8, 12, 4, 25, 10])
y_p = np.array([0, 1, 2, 3, 4, 5])

# x-label and y-label

plt.plot(y_p)
plt.xlabel("Time")
plt.ylabel("Distance")
plt.show()

# title

plt.plot(y_p, c="r", lw=2)
plt.xlabel("Time")
plt.ylabel("Distance")
plt.title("Watch Data")
plt.show()

# Setting the Font

font1 = {"family": "ariel", "color": "red", "size": 12.5}

font2 = {"family": "serif", "color": "green", "size": 12.5}

plt.plot(y_p, c="m", lw=2)
plt.xlabel("Time", fontdict=font1)
plt.ylabel("Distance", fontdict=font2)
plt.show()
