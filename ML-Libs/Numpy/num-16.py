# Sorting

# np.sort() = COPY not view

import numpy as np

# 1-D Array

arr = np.array([3, 1, 55, 6, 2, 9, 100])
sor = np.sort(arr)
print(arr)


# 2-D Array

arr2 = np.array([[30, 12, 41], [19, 76, 2]])

row = np.sort(arr2, axis=0)
print(row)

col = np.sort(arr2, axis=1)
print(col)
