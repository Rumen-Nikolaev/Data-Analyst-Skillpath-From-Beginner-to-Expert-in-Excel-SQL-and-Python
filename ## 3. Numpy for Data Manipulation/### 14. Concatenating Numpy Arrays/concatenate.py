import numpy as np
array1 = np.array([1, 2, 3, 4])
array2 = np.array([5, 6, 7, 8])
np.concatenate([array1, array2])
array([1, 2, 3, 4, 5, 6, 7, 8])
array3 = np.arange(1, 7).reshape((2, 3))
array3
array([[1, 2, 3],
       [4, 5, 6]])
array4 = np.array([[7, 8, 9], [10, 11, 12]])
array4
array([[ 7,  8,  9],
       [10, 11, 12]])
np.concatenate([array3, array4])
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [ 7,  8,  9],
       [10, 11, 12]])
np.concatenate([array3, array4], axis = 1)
array([[ 1,  2,  3,  7,  8,  9],
       [ 4,  5,  6, 10, 11, 12]])
array5 = np.arange(1, 11).reshape(5, 2)
array5
array([[ 1,  2],
       [ 3,  4],
       [ 5,  6],
       [ 7,  8],
       [ 9, 10]])
