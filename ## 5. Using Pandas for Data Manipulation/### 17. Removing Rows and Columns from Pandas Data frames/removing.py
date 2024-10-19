import numpy as np
import pandas as pd
x = np.arange(0, 28).reshape(7, 4)
df = pd.DataFrame(data = x, columns = ["VAL1", "VAL2", "VAL3", "VAL4"])
df
VAL1	VAL2	VAL3	VAL4
0	0	1	2	3
1	4	5	6	7
2	8	9	10	11
3	12	13	14	15
4	16	17	18	19
5	20	21	22	23
6	24	25	26	27
df.drop(["VAL3", "VAL4"], axis = 1)
VAL1	VAL2
0	0	1
1	4	5
2	8	9
3	12	13
4	16	17
5	20	21
6	24	25
df
VAL1	VAL2	VAL3	VAL4
0	0	1	2	3
1	4	5	6	7
2	8	9	10	11
3	12	13	14	15
4	16	17	18	19
5	20	21	22	23
6	24	25	26	27
df.drop(["VAL3", "VAL4"], axis = 1, inplace = True)
df
VAL1	VAL2
0	0	1
1	4	5
2	8	9
3	12	13
4	16	17
5	20	21
6	24	25
df.drop([2, 5], axis = 0, inplace = True)
df
VAL1	VAL2
0	0	1
1	4	5
3	12	13
4	16	17
6	24	25
