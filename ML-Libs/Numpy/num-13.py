# Joining numpy arrays-2

# Stack = join along axis

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

c = np.stack((a, b), axis=0)
print(c)

d = np.stack((a, b), axis=1)
print(d)


# Stack along rows = hstack()

x = np.hstack((a, b))
print(x)

# Stack along cols = vstack()

y = np.vstack((a, b))
print(y)

# Stack in depth : dstack() = increases a dimension i.e axis will always be +1 not 0 and 1

z = np.dstack((a, b))
print(z)
