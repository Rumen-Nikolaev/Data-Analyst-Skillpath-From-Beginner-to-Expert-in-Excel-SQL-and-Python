import numpy as np
import pandas as pd
x = np.random.randint(10, 50, size = 6)
y = np.random.randint(10, 50, size = 6)
z = np.random.randint(10, 50, size = 6)
t = np.random.randint(10, 50, size = 6)

dict_example = {"val1":x, "val2":y, "val3":z, "val4":t}

df = pd.DataFrame(dict_example)
df
val1	val2	val3	val4
0	17	46	24	37
1	41	48	14	25
2	38	35	18	22
3	16	21	49	49
4	44	34	13	37
5	42	43	42	46
df.head()
val1	val2	val3	val4
0	17	46	24	37
1	41	48	14	25
2	38	35	18	22
3	16	21	49	49
4	44	34	13	37
df.head(3)
val1	val2	val3	val4
0	17	46	24	37
1	41	48	14	25
2	38	35	18	22
df.tail(3)
val1	val2	val3	val4
3	16	21	49	49
4	44	34	13	37
5	42	43	42	46
df.columns
Index(['val1', 'val2', 'val3', 'val4'], dtype='object')
[i for i in df.columns]
['val1', 'val2', 'val3', 'val4']
df
val1	val2	val3	val4
0	17	46	24	37
1	41	48	14	25
2	38	35	18	22
3	16	21	49	49
4	44	34	13	37
5	42	43	42	46
df.columns = ["new1", "new2", "new3", "new4"]
df
new1	new2	new3	new4
0	17	46	24	37
1	41	48	14	25
2	38	35	18	22
3	16	21	49	49
4	44	34	13	37
5	42	43	42	46
df.values
array([[17, 46, 24, 37],
       [41, 48, 14, 25],
       [38, 35, 18, 22],
       [16, 21, 49, 49],
       [44, 34, 13, 37],
       [42, 43, 42, 46]])
type(df.values)
numpy.ndarray
type(df)
pandas.core.frame.DataFrame
df.shape
(6, 4)
df.ndim
2
df.size
24
