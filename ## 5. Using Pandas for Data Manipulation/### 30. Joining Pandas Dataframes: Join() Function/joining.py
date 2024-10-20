import pandas as pd
import numpy as np
df1 = pd.DataFrame({'X': ['X0', 'X1', 'X2'],
                    'Y': ['Y0', 'Y1', 'Y2']},
                   index = ['A0', 'A1', 'A2'])

df2 = pd.DataFrame({'Z': ['Z0', 'Z1', 'Z2'],
                    'T': ['T0', 'T1', 'T2']},
                   index = ['A0', 'A1', 'A2'])
df1
Z	T
A0	Z0	T0
A1	Z1	T1
A2	Z2	T2
df2
Z	T
A0	Z0	T0
A1	Z1	T1
A2	Z2	T2
df1.join(df2)
X	Y	Z	T
A0	X0	Y0	Z0	T0
A1	X1	Y1	Z1	T1
A2	X2	Y2	Z2	T2
df1.join(df2, how = "inner")
X	Y	Z	T
A0	X0	Y0	Z0	T0
A1	X1	Y1	Z1	T1
A2	X2	Y2	Z2	T2
df1.join(df2, how = "outer")
X	Y	Z	T
A0	X0	Y0	Z0	T0
A1	X1	Y1	Z1	T1
A2	X2	Y2	Z2	T2
df1.join(df2, how = "right")
X	Y	Z	T
A0	X0	Y0	Z0	T0
A1	X1	Y1	Z1	T1
A2	X2	Y2	Z2	T2
df3 = pd.DataFrame({'key': ['X0', 'X2', 'X3', 'X4', 'X5', 'X6'],
                    'Y': ['Y0', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6']})

df4 = pd.DataFrame({'key': ['X0', 'X2', 'X3'],
                    'Z': ['Z0', 'Z2', 'Z3']})
df3
key	Y
0	X0	Y0
1	X2	Y2
2	X3	Y3
3	X4	Y4
4	X5	Y5
5	X6	Y6
df4
key	Z
0	X0	Z0
1	X2	Z2
2	X3	Z3
df3.join(df4, lsuffix = "left", rsuffix = "right")
keyleft	Y	keyright	Z
0	X0	Y0	X0	Z0
1	X2	Y2	X2	Z2
2	X3	Y3	X3	Z3
3	X4	Y4	NaN	NaN
4	X5	Y5	NaN	NaN
5	X6	Y6	NaN	NaN
df3.join(df4, lsuffix = "left", rsuffix = "right", how = "inner")
keyleft	Y	keyright	Z
0	X0	Y0	X0	Z0
1	X2	Y2	X2	Z2
2	X3	Y3	X3	Z3
df3.set_index("key")
Y
key	
X0	Y0
X2	Y2
X3	Y3
X4	Y4
X5	Y5
X6	Y6
df3.set_index("key").join(df4.set_index("key"))
Y	Z
key		
X0	Y0	Z0
X2	Y2	Z2
X3	Y3	Z3
X4	Y4	NaN
X5	Y5	NaN
X6	Y6	NaN
