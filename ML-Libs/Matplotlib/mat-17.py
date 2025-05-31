# Fig , Axes and Subplots (NOT subplot)

# fig = size of the canvas : (width,height)
# axes = numpy array that we plot

import matplotlib.pyplot as plt
import numpy as np

# Single plot
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])
c = np.array([-3, -2, -1, 0, 1, 2])
d = np.array([9, 4, 1, 0, 1, 4])

fig, axes = plt.subplots()
axes.plot(x, y)
axes.set_title("Single Plot")
plt.show()


# Multiple Subplots  = (1,2) = 1-d array

fig, axes2 = plt.subplots(1, 2, figsize=(10, 5))

axes2[0].plot(x, y)
axes2[0].set_title("Plot 1")

axes2[1].plot(c, d)
axes2[1].set_title("Plot 2")

plt.show()
