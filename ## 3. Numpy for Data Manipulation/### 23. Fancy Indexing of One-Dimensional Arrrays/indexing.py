import numpy as np
fancy = np.arange(0, 50, 5)
fancy
array([ 0,  5, 10, 15, 20, 25, 30, 35, 40, 45])
fancy[1]
5
fancy[3]
15
fancy[5]
25
[fancy[1], fancy[3], fancy[5]]
[5, 15, 25]
indexes = [1, 3, 5]
fancy[indexes]
array([ 5, 15, 25])
array = np.array([1, 3, 5])
array
array([1, 3, 5])
fancy[array]
array([ 5, 15, 25])
