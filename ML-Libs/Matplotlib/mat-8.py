# Grid Lines

import numpy as np
import matplotlib.pyplot as plt

x_p = np.array([3, 8, 12, 4, 25, 10])
y_p = np.array([0, 1, 2, 3, 4, 5])

plt.plot(x_p, ls="-.", lw=2, c="g")
plt.grid()
plt.show()

# axis = which grid lines to show (default = 'both'||x|y)

plt.plot(y_p, ls="--", c="b", lw=2)
plt.grid(axis="x")
plt.show()

# Additional parameters :

plt.plot(x_p, ls="-", c="r", lw=2)
plt.grid(c="black", ls="--", lw=0.5)
plt.show()
