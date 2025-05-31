# Slicing

# 1-D Array

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(arr[1:5])  # 2,3,4,5
print(arr[4:])  # 5,6,7,8,9,10
print(arr[:4])  # 1,2,3,4
print(arr[-3:-1])  # 8,9
print(arr[1:5:2])  # 2,4
print(arr[::2])  # 1,3,5,7,9

mat = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(mat[1, 1:4])  # 7,8,9
print(mat[0:2, 1])  # 2,7
print(mat[0:2, 1:4])  # 2,3,4  7,8,9
