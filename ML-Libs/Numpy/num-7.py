# Copy Vs View

# View
# The new array SHARES the same data as the original
#  Very fast and memory efficient
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
v = arr.view()

v[0] = 1000
print(arr)  # [1000,2,3,4,5]

# Modifying the new affects the original array and vice versa


# Copy
# Completely Independent duplicate of the original array
# Takes more time and uses extra memory

x = np.array([1, 2, 4, 5, 6])

c = x.copy()

c[0] = 1000
print(x)  # [1,2,4,5,6]
print(c)  # [1000,2,4,5,6]

# Modifying the new does not affect the original array and vice versa


####  Common Example

a = np.array([1, 2, 3, 4, 5])
b = a
b[0] = 1000
print(a)  # [1000,2,3,4,5]

# a and b point to same array object in memory
# It is a example of view
