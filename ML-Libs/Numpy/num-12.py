# Joining numpy arrays-1

# 0 = rows
# 1 = cols

# Concatenate = joins at axis end

import numpy as np

a = np.array([[1, 2], [3, 4]])  # 2x2
b = np.array([[5, 6]])  # 2x1

c = np.concatenate((a, b), axis=0)  # row by row each array in sequence
print(c)

n = np.array([[5, 6], [7, 8]])  # 2x1


d = np.concatenate((a, n), axis=1)  # col by col array wise
print(d)
