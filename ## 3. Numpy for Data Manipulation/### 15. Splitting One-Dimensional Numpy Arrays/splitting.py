import numpy as np
array = np.array([1, 3, 5, 50, 50, 2, 4, 6])
np.split(array, [3, 5])
[array([1, 3, 5]), array([50, 50]), array([2, 4, 6])]
x, y, z = np.split(array, [3, 5])
x
array([1, 3, 5])
y
array([50, 50])
z
array([2, 4, 6])
np.split(array, 4)
[array([1, 3]), array([ 5, 50]), array([50,  2]), array([4, 6])]
