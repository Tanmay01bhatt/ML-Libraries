# Random Data Distribution
# using choice()

# ques:- Generate a 1-D array containing a 100 values , where each value has to be 3,5,7 or 9.
# P(3) = 0.1  ||  P(5) = 0.3 || P(7)= 0.6 || P(9) = 0

from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=100)
print(x)


# 2-D Array with 3 rows and 5 cols

y = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(y)
