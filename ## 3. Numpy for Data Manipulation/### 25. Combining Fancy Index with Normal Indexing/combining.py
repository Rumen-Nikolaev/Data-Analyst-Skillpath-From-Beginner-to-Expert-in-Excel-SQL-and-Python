import numpy as np
example = np.arange(1,17).reshape((4,4))
example
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12],
       [13, 14, 15, 16]])
example[1, [1, 3]]
array([6, 8])
example[[0, 3], 1]
array([ 2, 14])
