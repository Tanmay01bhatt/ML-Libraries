# Selecting a Random Number from the Array

# choice()

import numpy as np
from numpy import random

arr = np.array([3, 5, 8, 20])
x = random.choice(arr)
print(x)  # print any number from the given array


# Generating a new array from the given numbers using choice() with size param

y = random.choice(arr, size=(3, 4))

print(y)
