import numpy as np
import pandas as pd
x = np.random.randint(10, 50, size = 6)
x
array([44, 37, 12, 10, 18, 30])
y = np.random.randint(10, 50, size = 6)
z = np.random.randint(10, 50, size = 6)
t = np.random.randint(10, 50, size = 6)
dict_example = {"val1" : x, "val2" : y, "val3" : z, "val4" : t}
df = pd.DataFrame(dict_example)
df
val1	val2	val3	val4
0	44	28	34	30
1	37	26	25	34
2	12	10	44	47
3	10	47	18	33
4	18	21	21	40
5	30	43	45	26
