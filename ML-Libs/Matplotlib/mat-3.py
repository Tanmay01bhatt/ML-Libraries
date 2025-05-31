# Matplotlib Markers
# Indicates the SHAPE of each point
import numpy as np
import matplotlib.pyplot as plt

x_p = np.array([3, 8, 12, 4, 25, 10])
y_p = np.array([0, 1, 2, 3, 4, 5])

# 1 - dot

plt.plot(x_p, y_p, marker="o")
plt.show()

# 2 - star

plt.plot(x_p, y_p, marker="*")
plt.show()

# 3 - hexagon

plt.plot(x_p, y_p, marker="h")
plt.show()

# 4 - triangle

plt.plot(y_p, marker="^")
plt.show()

# 5 - square

plt.plot(y_p, marker="s")
plt.show()
