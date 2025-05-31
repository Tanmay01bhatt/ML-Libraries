# Bar Graph = plt.bar()  |  catergorical data

import numpy as np
import matplotlib.pyplot as plt

x = np.array(["A", "B", "C", "D", "E", "F"])
y = np.array([10, 5, 20, 30, 5, 50])

plt.bar(x, y)
plt.show()

# Horizontal Bars = barh

plt.barh(x, y)
plt.show()

# Colors : Same logic as prev

plt.bar(x, y, color="g")
plt.show()

# Each bar diff color

c = ["red", "yellow", "green", "blue", "magenta", "black"]
plt.bar(x, y, color=c)
plt.show()

# Does NOT support cmap

# Bar Width (1= larger , 0 = small)

plt.bar(x, y, width=0.2, edgecolor=c)
plt.show()

# Bar height = horizontal bars

plt.barh(x, y, height=0.3)
plt.show()
