import numpy as np
variable = np.array([0, 1, 2, 3, 7, 5, 6, 9, 8, 9])
variable
array([0, 1, 2, 3, 7, 5, 6, 9, 8, 9])
variable[4] = 4
variable[7] = 7
variable
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
variable[0:5] = 10
variable
array([10, 10, 10, 10, 10,  5,  6,  7,  8,  9])
variable[5:]
array([5, 6, 7, 8, 9])
variable[5:] = 20, 30, 40, 50, 60
variable
array([10, 10, 10, 10, 10, 20, 30, 40, 50, 60])
