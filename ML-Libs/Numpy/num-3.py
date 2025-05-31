import numpy as np

# Combining lower order tensors to create higher ones.

# 0-D
a = np.array(1)
b = np.array(2)

# 1D = 0D + 0D

v = np.array([a, b])
print(v.ndim)

# 2D = 1D + 1D

m = np.array([v, v])
print(m.ndim)

# 3D = 2D + 2D

t = np.array([m, m])
print(t.ndim)

# 4D = 3D + 3D
x = np.array([t, t])
print(x.ndim)

# 5D = 4D + 4D

y = np.array([x, x])
print(y.ndim)
