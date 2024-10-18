import numpy as np
array = np.random.randint(0, 50, 10)
array
array([39, 48, 25,  6, 49, 42, 39,  0, 30, 26])
array.max()
49
array.argmax()
4
array2 = np.random.randint(0, 50, (4, 3))
array2
array([[ 6, 43, 27],
       [ 6, 13, 42],
       [ 6, 37, 35],
       [45, 19,  2]])
array2.max()
45
array2.argmax()
9
