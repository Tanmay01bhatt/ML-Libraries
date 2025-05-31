# 3 - Converting the datatype of an existing array = astype()

import numpy as np

arr = np.array([1.12, 3.32, 4.56, 6.89, 9.76])

arr2 = arr.astype("i")
print(arr2)
print(arr2.dtype)  # int32

arr3 = arr.astype(int)
print(arr3.dtype)  # int64


x = np.array([3.45, 0, 0.56, 1, 0.0, 5.66])

y = x.astype(bool)
print(y)  # True, False, True, True, False, True
