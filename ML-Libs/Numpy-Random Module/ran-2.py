# Generate a random array

# Int = size parameter = shape of array

# 1-D Array

from numpy import random

a = random.randint(100, size=5)
print(a)

# 2-D Array

b = random.randint(100, size=(2, 4))
print(b)

# Floats

# 1-D Array

x = random.rand(5)  # 5 elements of rang[0,1]
print(x)

# 2-D Array

y = random.rand(2, 4)
print(y)
