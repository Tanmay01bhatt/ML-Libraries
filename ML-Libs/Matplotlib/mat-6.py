# Linestyle = ls

import numpy as np
import matplotlib.pyplot as plt

x_p = np.array([3, 8, 12, 4, 25, 10])
y_p = np.array([0, 1, 2, 3, 4, 5])

plt.plot(x_p, ls=":")
plt.show()

# color

plt.plot(x_p, ls="-", c="g")  # 'color' can also be used
plt.show()

# linewidth = thickness of line

plt.plot(y_p, ls="-.", c="m", lw=10)
plt.show()

# multiple lines

plt.plot(x_p, ls="-", c="r", lw=2)
plt.plot(y_p, ls="-", c="b", lw=2)
plt.show()
