# Pie Charts - best used in comparing 3-6 values only.

import numpy as np
import matplotlib.pyplot as plt

# Basic

y = np.array([30, 15, 20, 10, 5])
plt.pie(y)
plt.show()

# Labels

labs = ["A", "B", "C", "D", "E"]
plt.pie(y, labels=labs)
plt.show()

# Start angle: default val = 0

plt.pie(y, labels=labs, startangle=90)
plt.show()

# Exoplode and color

colors = ["red", "yellow", "pink", "brown", "green"]
exp = [0.2, 0, 0, 0, 0]

plt.pie(y, colors=colors, labels=labs, explode=exp)
plt.show()

# shadow
plt.pie(y, labels=labs, explode=exp, shadow=True)
plt.show()

# Legend

plt.pie(y, labels=labs)
plt.legend(title="Labels")
plt.axis("equal")  # ensure it's a circle
plt.show()
