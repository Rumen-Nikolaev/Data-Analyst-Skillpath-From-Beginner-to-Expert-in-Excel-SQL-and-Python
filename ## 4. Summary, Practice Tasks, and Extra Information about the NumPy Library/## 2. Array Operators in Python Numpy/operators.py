import numpy as np
Numbers_1 = np.arange(1,10,2)
Numbers_Rand = np.random.randint(1,20,5)
Numbers_1
array([1, 3, 5, 7, 9])
Numbers_Rand
array([16,  6,  6, 18,  7])
Numbers_1 + Numbers_Rand
array([17,  9, 11, 25, 16])
Numbers_1 * Numbers_Rand
array([ 16,  18,  30, 126,  63])
Numbers_1 / 3
array([0.33333333, 1.        , 1.66666667, 2.33333333, 3.        ])
Numbers_1 += 5
Numbers_Rand += 3
Numbers_1
array([ 6,  8, 10, 12, 14])
Numbers_Rand
array([19,  9,  9, 21, 10])
np.sqrt(Numbers_1)
array([2.44948974, 2.82842712, 3.16227766, 3.46410162, 3.74165739])
np.sqrt(Numbers_Rand)
array([4.35889894, 3.        , 3.        , 4.58257569, 3.16227766])
S_1 = np.arange(1,10,2)
S_2 = np.arange(1,11,3)
S_1
array([1, 3, 5, 7, 9])
S_2
array([ 1,  4,  7, 10])
