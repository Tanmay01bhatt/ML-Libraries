# Random Number

# Random : something that can NOT be predicted logically

# Pseudo Random Number
# Random numbers that are generated using an algorithm
# given the same seed =  the same sequence is produced

# seed = initial value used to start the pseudo random number generator

# Generating a Random Number

from numpy import random

x = random.randint(100)
print(x)  # random value b/w 0 and 100

# Random Float

y = random.rand()
print(y)  # random nmber b/w 0 and 1.
