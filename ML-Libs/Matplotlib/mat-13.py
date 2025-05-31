# Alpha = level of transparency of dots

import numpy as np
import matplotlib.pyplot as plt

x = np.array([3, 8, 12, 4, 25, 10])
y = np.array([0, 1, 2, 3, 4, 5])
a = np.array([-3, -2, -1, 0, 1, 2])
d = np.array([9, 4, 1, 0, 1, 4])

plt.scatter(x, y, alpha=0.5)
plt.show()

# 0 = fully transparent
# 1 = fully opaque

# Color,Size and Alpha Combined

colors = np.random.randint(100, size=(6))
size = np.random.randint(100, size=6)

plt.scatter(a, d, c=colors, s=size, alpha=0.6, cmap="inferno")
plt.colorbar(label="Color Intensity")
plt.title("Scatter Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()
