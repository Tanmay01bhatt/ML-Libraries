# Reshape
# Conditions:
# The total number of elements must match
# total no. of elements = product of dimentions

# 1D to 2D

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
arr2 = arr.reshape(2, 3)
print(arr2)
print(arr2.ndim)

# We can't reshpape it into(4,4) , sice  4x4 = 16 and total elements = 6


# 1D to 3D

arr3 = arr.reshape(2, 3, 1)
print(arr3)
print(arr3.ndim)

# Reshape returns a VIEW of org array NOT a copy


# UNKNOWN DIMENSION
# We are allowed 1 unknown dimension
# Using '-1' = numpy will automatically calculate that dimension

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

b = a.reshape(3, 1, -1)

print(b.ndim)
c = a.reshape(1, -1)
print(c.ndim)


# Flattening = Multi- dimensional to 1-D array

x = np.array([[1, 2, 3], [4, 5, 6]])
flat = x.flatten()
y = x.reshape(-1)
print(flat)
print(y)
d = x.ravel()
print(d)


# ravel() and reshape(-1) = View
# flatten() =Copy
