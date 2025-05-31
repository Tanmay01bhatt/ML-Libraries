# Split
import numpy as np

# np.split() = splits the array equally

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
s1 = np.split(arr, 3)  # split into 3 equal arrays
print(s1)
# Raises an exception if it can't divide equally

# np.array_split() = will ALWAYS split the array

sp = np.array_split(arr, 4)
print(sp)


# 2-D Arrays

arr2 = np.array([[1, 2, 3, 4, 5], [10, 20, 30, 40, 50]])

sp2 = np.array_split(arr2, 3, axis=1)
sp3 = np.array_split(arr2, 3, axis=0)

print(sp2)
print("\n", sp3)
