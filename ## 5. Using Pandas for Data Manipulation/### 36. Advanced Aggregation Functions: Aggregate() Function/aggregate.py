import pandas as pd
import numpy as np
df = pd.DataFrame({'groups': ['X', 'Y', 'Z', 'X', 'Y', 'Z'],
                   'val1': [2, 15, 25, 14, 3, 91],
                   'val2': [92, 245, 325, 254, 103, 961]})
df
groups	val1	val2
0	X	2	92
1	Y	15	245
2	Z	25	325
3	X	14	254
4	Y	3	103
5	Z	91	961
df.groupby("groups").mean()
val1	val2
groups		
X	8.0	173.0
Y	9.0	174.0
Z	58.0	643.0
df.groupby("groups").aggregate(["mean", np.median, min, "sum"])
df.groupby("groups").aggregate({"vail1" : "mean", "val2" : "median"})
