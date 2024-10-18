import numpy as np
array = np.arange(1, 11)
array
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
array > 5
array([False, False, False, False, False,  True,  True,  True,  True,
        True])
array[array > 5]
array([ 6,  7,  8,  9, 10])
condition = array <= 4
array[condition]
array([1, 2, 3, 4])
new_condition = (array != 8) & (array >= 6)
array[new_condition]
array([ 6,  7,  9, 10])
