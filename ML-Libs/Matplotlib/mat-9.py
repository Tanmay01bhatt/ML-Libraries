# Subplot =  display multiple plots in 1 figure

# plt.subplot(rows,cols,index=1,2,3,4,5,6{of plots})

import numpy as np
import matplotlib.pyplot as plt

x = np.array([3, 8, 12, 4, 25, 10])
y = np.array([0, 1, 2, 3, 4, 5])
a = np.array([2, 4, 8, 32, 64, 128])
b = np.array([50, 40, 30, 20, 10, 0])
c = np.array([-3, -2, -1, 0, 1, 2])
d = np.array([9, 4, 1, 0, 1, 4])

# 2 subplots:  (1,2)
plt.subplot(1, 2, 1)
plt.plot(x)

plt.subplot(1, 2, 2)
plt.plot(y)
plt.show()

# top - bottom = (2,1)
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(y)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Plot 1")

plt.subplot(2, 1, 2)
plt.plot(b)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Plot-2", y=1.04)

plt.suptitle("Top-Bottom Graph")
plt.show()

# draw 6 subplots : (2,3)

plt.subplot(2, 3, 1)
plt.plot(x)
plt.title("Plot 1")

plt.subplot(2, 3, 2)
plt.plot(y)
plt.title("Plot 2")

plt.subplot(2, 3, 3)
plt.plot(a)
plt.title("Plot 3")

plt.subplot(2, 3, 4)
plt.plot(b)
plt.title("Plot 4")

plt.subplot(2, 3, 5)
plt.plot(c)
plt.title("Plot 5")

plt.subplot(2, 3, 6)
plt.plot(d)
plt.title("Plot 6")

# Beutify the plots : plt.subplots_adjust()

plt.subplots_adjust(
    hspace=0.5,  # Height (vertical) space between rows
    wspace=0.4,  # Width (horizontal) space between columns
)

plt.show()
