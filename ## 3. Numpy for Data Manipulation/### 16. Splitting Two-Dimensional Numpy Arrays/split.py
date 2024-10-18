import numpy as np
array = np.arange(20).reshape(5, 4)
array
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19]])
np.split(array, [1, 3])
[array([[0, 1, 2, 3]]),
 array([[ 4,  5,  6,  7],
        [ 8,  9, 10, 11]]),
 array([[12, 13, 14, 15],
        [16, 17, 18, 19]])]
x, y, z = np.split(array, [1, 3])
x
array([[0, 1, 2, 3]])
y
array([[ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
z
array([[12, 13, 14, 15],
       [16, 17, 18, 19]])
np.split(array, [1, 3], axis = 1)
[array([[ 0],
        [ 4],
        [ 8],
        [12],
        [16]]),
 array([[ 1,  2],
        [ 5,  6],
        [ 9, 10],
        [13, 14],
        [17, 18]]),
 array([[ 3],
        [ 7],
        [11],
        [15],
        [19]])]
array
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19]])
np.hsplit(array, 4)
[array([[ 0],
        [ 4],
        [ 8],
        [12],
        [16]]),
 array([[ 1],
        [ 5],
        [ 9],
        [13],
        [17]]),
 array([[ 2],
        [ 6],
        [10],
        [14],
        [18]]),
 array([[ 3],
        [ 7],
        [11],
        [15],
        [19]])]
np.hsplit(array, [1, 3])
[array([[ 0],
        [ 4],
        [ 8],
        [12],
        [16]]),
 array([[ 1,  2],
        [ 5,  6],
        [ 9, 10],
        [13, 14],
        [17, 18]]),
 array([[ 3],
        [ 7],
        [11],
        [15],
        [19]])]
array
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19]])
np.vsplit(array, 5)
[array([[0, 1, 2, 3]]),
 array([[4, 5, 6, 7]]),
 array([[ 8,  9, 10, 11]]),
 array([[12, 13, 14, 15]]),
 array([[16, 17, 18, 19]])]
np.split(array, [2, 4])
[array([[0, 1, 2, 3],
        [4, 5, 6, 7]]),
 array([[ 8,  9, 10, 11],
        [12, 13, 14, 15]]),
 array([[16, 17, 18, 19]])]
