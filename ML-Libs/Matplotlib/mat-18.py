# 2x2 plots = 2-d array
import numpy as np
import matplotlib.pyplot as plt

x = np.array([3, 8, 12, 4, 25, 10])
y = np.array([0, 1, 2, 3, 4, 5])
a = np.array([2, 4, 8, 32, 64, 128])
b = np.array([50, 40, 30, 20, 10, 0])
c = np.array([-3, -2, -1, 0, 1, 2])
d = np.array([9, 4, 1, 0, 1, 4])

fig, axes = plt.subplots(2, 2, figsize=(10, 5))

axes[0, 0].plot(x, y)
axes[0, 0].set_title("Plot 1")
axes[0, 0].set_xlabel("X-Axis")
axes[0, 0].set_ylabel("Y-Axis")

axes[0, 1].plot(a, b)
axes[0, 1].set_title("Plot 2")
axes[1, 0].plot(c, d)
axes[1, 0].set_title("Plot 3")
axes[1, 1].plot(b, y)
axes[1, 1].set_title("Plot 4")

plt.subplots_adjust(hspace=0.5, wspace=0.5)

fig.suptitle("SUBPLOTS")
plt.show()
