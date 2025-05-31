# Format Strings = Shortcut for : marker , line and color style
# marker | line | color     =   ORDER DOES NOT MATTER (MLC)

import numpy as np
import matplotlib.pyplot as plt

x_p = np.array([3, 8, 12, 4, 25, 10])
y_p = np.array([0, 1, 2, 3, 4, 5])

plt.plot(x_p, y_p, "o:r")  # o - marker | : - dotted line | r - color
plt.show()

"""
Linestyle : 

-   solid line
:   doted line
--  dashed line
-.  dash dot line

"""

"""
Color : 

r - red
g - green
b - blue
m - magenta
k - black
.
.
etc
"""
plt.plot(x_p, "h--k")
plt.show()

plt.plot(x_p, y_p, "s-.m")
plt.show()

plt.plot(x_p, "^-g")
plt.show()
