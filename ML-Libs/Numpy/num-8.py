# Shape
# Size along ecah dimension

import numpy as np

a1 = np.array([1, 2, 4, 5, 6])

print(a1.shape)  # (5,) = 1D array with 5 elements

a2 = np.array([[1, 2, 3], [4, 5, 6]])

print(a2.shape)  # (2,3) = rows x cols

a3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(a3.shape)  # (2,2,3) = 2 arrays of 2 rows and 3 columns
# or 2 depth , 2 rows ,3 cols
