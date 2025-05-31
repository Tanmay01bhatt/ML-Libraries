# N-Dimentional Iterator
# allows iterations over every element of the array
# regardless of its shae or dimension

import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [8, 9]]])

for x in np.nditer(arr):
    print(x)
# Every element is individually accessed

# It is a very powerful tool used in advanced tasks.

# Iterating over multiple arrays

a = np.array([1, 2, 3, 4, 54, 5, 67])
b = np.array([10, 20, 30, 40, 50, 60, 70])

for x, y in np.nditer([a, b]):
    print(x, y)  # lentgh should be same

# Convert the datatype of elements of array

x = np.array([1, 2, 3, 4, 5])

for i in np.nditer(x, flags=["buffered"], op_dtypes=["S"]):
    #  bufferred space is required for type conversion
    print(i)


# N-Dimensional Enumerator
# to get index and valuues both

arr2 = np.array([[1, 2, 3], [4, 5, 6]])

for idx, val in np.ndenumerate(arr2):
    print(idx, val)
