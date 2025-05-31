# Size = size of the dots

import numpy as np
import matplotlib.pyplot as plt

x = np.array([3, 8, 12, 4, 25, 10])
y = np.array([0, 1, 2, 3, 4, 5])
a = np.array([50, 40, 30, 20, 10, 0])

size = np.random.randint(100, size=(6))

plt.scatter(a, y, s=size)
plt.show()

# you can also give specific values :

s2 = np.array([20, 30, 5, 50, 15, 20])
plt.scatter(x, y, s=s2)
plt.show()
