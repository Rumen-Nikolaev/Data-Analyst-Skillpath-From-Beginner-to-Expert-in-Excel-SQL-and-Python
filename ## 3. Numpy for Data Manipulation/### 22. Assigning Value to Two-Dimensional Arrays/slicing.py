import numpy as np
example = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
example
array([[10, 20, 30],
       [40, 50, 60],
       [70, 80, 90]])
example[1, 1] = 100
example
array([[ 10,  20,  30],
       [ 40, 100,  60],
       [ 70,  80,  90]])
example[1, 0] = 100.6
example
array([[ 10,  20,  30],
       [100, 100,  60],
       [ 70,  80,  90]])
example[:,2] = 100
example
array([[ 10,  20, 100],
       [100, 100, 100],
       [ 70,  80, 100]])
example[0::2,0:2]
array([[10, 20],
       [70, 80]])
example[0::2,0:2] = 100
example
array([[100, 100, 100],
       [100, 100, 100],
       [100, 100, 100]])
example[0]
array([100, 100, 100])
example[0] = 10, 20, 30
example
array([[ 10,  20,  30],
       [100, 100, 100],
       [100, 100, 100]])
