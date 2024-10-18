import numpy as np
N_Array_1 = np.random.randint(1,30,8)
N_Array_1
array([22, 21, 12, 22, 12, 25,  4, 11])
N_Array_1[3]
22
 N_Array_1[2:7]
array([12, 22, 12, 25,  4])
N_Array_1[:3]
array([22, 21, 12])
N_Array_2 = np.arange(1,7)
N_Array_2
array([1, 2, 3, 4, 5, 6])
N_Array_2 [:3] = 7
N_Array_2
array([7, 7, 7, 4, 5, 6])
N_Array_3 = np.random.randint(1,100,20)
N_Array_3
array([98,  7, 68, 49,  5, 35, 97,  7, 44, 47, 63,  7, 39, 81, 67,  3, 62,
       41, 78, 46])
N_Array_3 = N_Array_3.reshape(5,4)
N_Array_3
array([[98,  7, 68, 49],
       [ 5, 35, 97,  7],
       [44, 47, 63,  7],
       [39, 81, 67,  3],
       [62, 41, 78, 46]])
N_Array_3[4]
array([62, 41, 78, 46])
N_Array_3[3,0]
39
N_Array_3[:2]
array([[98,  7, 68, 49],
       [ 5, 35, 97,  7]])
N_Array_3[:,2:4]
array([[68, 49],
       [97,  7],
       [63,  7],
       [67,  3],
       [78, 46]])
N_Array_3[:,(2,3)]
array([[68, 49],
       [97,  7],
       [63,  7],
       [67,  3],
       [78, 46]])
N_Array_4 = np.arange(1,7)
N_Array_4
array([1, 2, 3, 4, 5, 6])
N_Array_4_SC = N_Array_4.view()
N_Array_4_SC
array([1, 2, 3, 4, 5, 6])
N_Array_4[3]*=7
N_Array_4
array([ 1,  2,  3, 28,  5,  6])
N_Array_4_SC
array([ 1,  2,  3, 28,  5,  6])
N_Array_4_SC[2] += 5
N_Array_4_SC
array([ 1,  2,  8, 28,  5,  6])
N_Array_4_SC
array([ 1,  2,  8, 28,  5,  6])
N_Array_4_SC = N_Array_4.copy()
N_Array_4_DC
array([ 1,  2,  8, 28,  5,  6])
N_Array_4_DC[1] -= 5
N_Array_4_DC
array([ 1, -3,  8, 28,  5,  6])
N_Array_4
array([ 1,  2,  8, 28,  5,  6])
N_Array_4_SC
array([ 1,  2,  8, 28,  5,  6])
