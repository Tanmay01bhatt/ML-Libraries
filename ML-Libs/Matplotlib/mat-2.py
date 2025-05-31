import matplotlib.pyplot as plt
import numpy as np

# Default x - points
# If we don't specify points on x-axis , then they will given default values based on the length of y-points.

y_p = np.array([3, 8, 12, 4, 25, 10])

plt.plot(y_p)
plt.show()

"""
def values of x:
        x_p = [0,1,2,3,4,5] will be automatically provided

x_p = range(len(y_p))

"""

# UNLIKE x_p , default values of y are NOT provided .

x_p = np.array([10, 20, 30, 40, 50])
plt.plot(x_p)
plt.show()

# iterpreted as y-values and def x_values in turn are provided
