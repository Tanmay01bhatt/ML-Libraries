# Marker size =  ms

import numpy as np
import matplotlib.pyplot as plt

x_p = np.array([3, 8, 12, 4, 25, 10])
y_p = np.array([0, 1, 2, 3, 4, 5])

plt.plot(x_p, y_p, marker="o", ms=20)
plt.show()

# mfc = face color
# mec = edge color

plt.plot(x_p, y_p, marker="h", ms=15, mfc="r", mec="k")
plt.show()
