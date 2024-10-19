import numpy as np
import pandas as pd
array_example = np.random.randint(0, 50, (4, 4))
array_example
array([[ 2, 42, 42, 13],
       [ 1, 20, 13,  1],
       [ 3, 16, 11, 39],
       [ 5, 42, 47, 46]])
df = pd.DataFrame(array_example, index = ["a", "b", "c", "d"], columns = ["val1", "val2", "val3", "val4"])
df
val1	val2	val3	val4
a	2	42	42	13
b	1	20	13	1
c	3	16	11	39
d	5	42	47	46
