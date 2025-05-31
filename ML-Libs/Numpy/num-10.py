# Iteration/Loops
import numpy as np

# 1-D array

arr = np.array([1, 2, 3, 4, 5, 6])
for x in arr:
    print(x, end="")

# Using index
print()

len1 = len(arr)
for i in range(0, len1):
    print(arr[i], end="")

print()
# 2-D array

arr2 = np.array([[1, 2, 3, 4], [4, 5, 6, 7]])

# row by row
for x in arr2:
    print(x)
    break  # 1st row

# by each element
print()

for x in arr2:
    for y in x:
        print(y, end="")
        break  # 1st element
    break  # outer loop
print()

# by index

row, col = arr2.shape
for i in range(row):
    for j in range(col):
        print(arr2[i][j], end=" ")

print()

# 3-D Array

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# row by row

for x in arr3:
    print(x)
    break

print()
# elemnt by element

for x in arr3:
    for y in x:
        for z in y:
            print(z)
            break  # first element of each row

# using index
print()

depth, row, col = arr3.shape

for i in range(depth):
    for j in range(row):
        for k in range(col):
            print(arr3[i][j][k], end=" ")
