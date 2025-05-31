# Histograms = divides data into bins and cont the number of observations in each bin

import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)
data2 = np.random.randn(1000)
# Basic
plt.hist(data)
plt.show()

# Customized

plt.hist(data, bins=20, color="red", edgecolor="black", alpha=0.3)
plt.show()

# hist + kde (normalizes the data) nothing in this case since the data is already under normal distribution.

plt.hist(data, bins=20, color="yellow", edgecolor="green", alpha=0.8, density=True)
plt.show()

# Multiple / Stacked histograms

plt.hist([data, data2], bins=25, stacked=True, color=["red", "blue"], edgecolor="black")
plt.show()

# comparing directly

plt.hist(
    [data, data2], bins=25, stacked=False, color=["red", "blue"], edgecolor="black"
)
plt.show()
