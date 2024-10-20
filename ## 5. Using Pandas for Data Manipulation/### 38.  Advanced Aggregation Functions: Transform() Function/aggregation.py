import pandas as pd
import numpy as np
df = pd.DataFrame({'groups': ['X', 'Y', 'Z', 'X', 'Y', 'Z'],
                   'val1': [2, 15, 25, 14, 3, 91],
                   'val2': [92,245,325,254,103,961]})
df
groups	val1	val2
0	X	2	92
1	Y	15	245
2	Z	25	325
3	X	14	254
4	Y	3	103
5	Z	91	961
df_new = df.loc[:, "val1":"val2"]
df_new
val1	val2
0	2	92
1	15	245
2	25	325
3	14	254
4	3	103
5	91	961
def normalize(x):
    return (x - x.min()) / (x.max() - x.min())
df_new.transform(normalize)
val1	val2
0	0.000000	0.000000
1	0.146067	0.176064
2	0.258427	0.268124
3	0.134831	0.186421
4	0.011236	0.012658
5	1.000000	1.000000
df_new.loc[1, "val1"]
np.int64(15)
(df_new.loc[1, "val1"] - df["val1"].min()) / (df["val1"].max()- df["val1"].min())
np.float64(0.14606741573033707)
df_new
val1	val2
0	2	92
1	15	245
2	25	325
3	14	254
4	3	103
5	91	961
df_new.transform(lambda a : np.sin(a))
val1	val2
0	0.909297	-0.779466
1	0.650288	-0.044213
2	-0.132352	-0.988036
3	0.990607	0.451999
4	0.141120	0.622989
5	0.105988	-0.321537
np.sin(df_new.val2)
0   -0.779466
1   -0.044213
2   -0.988036
3    0.451999
4    0.622989
5   -0.321537
Name: val2, dtype: float64
 
