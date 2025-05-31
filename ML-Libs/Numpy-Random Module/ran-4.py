# seed() =  same seed = produces the same sequence of random numbers
# reproducible outputs / helpful in testing

import numpy as np
from numpy import random

# useful while spliting data in ml

np.random.seed(42)
print(np.random.randint(1, 25, size=5))
# same output everytime


np.random.seed(10)
print(np.random.randint(1, 25, size=5))
# diff seed diff output


# use random.default_rng(sedd=42) =  for v.large programs
