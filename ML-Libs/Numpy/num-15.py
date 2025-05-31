# Searching
import numpy as np

# 1 - where() = Finds the index where the condition(use arr name(ref)) is true.

arr = np.array([1, 4, 3, 4, 5, 6, 4, 8])
x = np.where(arr == 4)
print(x)

y = np.where(arr % 2 == 0)
print(y)


# 2 - searchsorted() =finds the index where the value nedds to be inserted to maintain order.
# usually used on a sorted array
# it performs binary search to find index.

arr2 = np.array([6, 7, 8, 9, 10])
u = np.searchsorted(arr2, 7)
print(u)

# by default the left most index is returned.
# to change that:
v = np.searchsorted(arr2, 7, side="right")
print(v)

# multiple values

z = np.searchsorted(arr2, [6, 9, 10])
print(z)


# To get Values = use Bollean Indexing (arrar cond inside arr[])

a2 = np.array([19, 20, 30, 40, 50])
print(a2[a2 > 25])
