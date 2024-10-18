import numpy as np
array = np.random.randint(20, 70, 10)
array
array([26, 64, 45, 60, 44, 31, 60, 50, 30, 52])
array.min()
26
array.argmin()
0
array2 = np.random.randint(20, 70, (5, 3))
array2
array([[67, 66, 67],
       [32, 64, 32],
       [51, 69, 35],
       [26, 22, 26],
       [44, 53, 26]])
array2.min()
22
array2.argmin()
10
