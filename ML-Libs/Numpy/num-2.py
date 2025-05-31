import numpy as np

# Dimensions
# Level of array depth
# nested arrays = arrays having arrays as thier elements

# ndim() = finds the number of dimensions


# 0-D = Scalar = only 1 element

arr0 = np.array(40)
print(arr0.ndim)


# 1-D = linear or basic array

arr1 = np.array([1, 2, 3, 4, 5])
print(arr1.ndim)
print(arr1[1])  # 2

# 2-D = matrix or Second order tensor

mat = np.array([[2, 4, 6], [3, 5, 7]])
print(mat.ndim)
print(mat[1][2])  # 7


# 3-D = has 2-D array as its elements / 3rd order tensor

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr3.ndim)
print(arr3[1][0][1])  # 8


# Higher dimension Arrays

arr5 = np.array([1, 2, 3, 4, 5], ndmin=5)
print(arr5.ndim)
