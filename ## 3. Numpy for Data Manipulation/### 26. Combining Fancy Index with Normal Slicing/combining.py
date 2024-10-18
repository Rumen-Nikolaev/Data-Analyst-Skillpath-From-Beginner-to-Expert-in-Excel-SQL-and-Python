import numpy as np
example = np.arange(1,17).reshape((4,4))
example
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12],
       [13, 14, 15, 16]])
example[0:, [1, 2]]
array([[ 2,  3],
       [ 6,  7],
       [10, 11],
       [14, 15]])
example[1:3, [1, 2]]
array([[ 6,  7],
       [10, 11]])
