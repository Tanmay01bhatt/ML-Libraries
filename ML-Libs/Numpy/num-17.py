# Filtering Arrays = using the array name given by you
# getting some new elements out an org array and forming a new array with them.

import numpy as np

arr = np.array([10, 20, 40, 30, 60, 70])
filter1 = arr > 30
fil_Arr = arr[filter1]
print(fil_Arr)

# OR
print(arr[arr > 30])

# Multiple Conditions use ()

f2 = (arr > 20) & (arr < 60)
a2 = arr[f2]
print(a2)


# Lengthy Way
filter_arr = []
for x in arr:
    if x > 30:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

new_arr = arr[filter_arr]  # bool values
print(new_arr)
