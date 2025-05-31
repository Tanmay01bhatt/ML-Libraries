# Datatypes

# In python we have 5: int str float bool complex

# In numpy we have 11 : i - int , u - unsigned int , f - float , c - complex , b - boolean , S - string(byte) , U - unicode string , O - object , V - void(fixed chunk of memory) , m - timedelta , M - datetime

# 1 - Checking the datatype of an array
# dtype = attribute


import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)  # int64


arr2 = np.array(["apple", "banana", "cherry"])
print(arr2.dtype)
# <U6 = U - unicode string of max len = 6


# 2- Creating an array with a specific datatype

x = np.array([1, 2, 3, 4, 5, 6], dtype="S")
print(x)  # converted to byte string

# any can be used = i u b f c S U O V m M

y = np.array([1, 2, 3, 4, 5, 6], dtype="i4")
print(y.dtype)  # int32  /  i4 = 4 bytes integer
