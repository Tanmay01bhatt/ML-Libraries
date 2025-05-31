# Permutation
# arrabgement of elemens in an array

# Shuffle =  makes changes to the org array(VIEW)

import numpy as np
from numpy import random

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
random.shuffle(arr)
print(arr)


# Permutation = returns a new re-arranged array (COPY)

arr2 = np.array([10, 20, 30, 40, 50, 60])

new_arr = random.permutation(arr2)

print(new_arr)
print(arr2)
# org remains the same
