import numpy as np
import pandas as pd
df1 = pd.DataFrame({'X': ['X0', 'X1', 'X2', 'X3'],
                    'Y': ['Y0', 'Y1', 'Y2', 'Y3'],
                    'Z': ['Z0', 'Z1', 'Z2', 'Z3'],
                    'T': ['T0', 'T1', 'T2', 'T3']}
                  )
df2 = pd.DataFrame({'X': ['X4', 'X5', 'X6', 'X7'],
                    'Y': ['Y4', 'Y5', 'Y6', 'Y7'],
                    'Z': ['Z4', 'Z5', 'Z6', 'Z7'],
                    'T': ['T4', 'T5', 'T6', 'T7']}
                  )
df3 = pd.DataFrame({'X': ['X8', 'X9', 'X10', 'X11'],
                    'Y': ['Y8', 'Y9', 'Y10', 'Y11'],
                    'Z': ['Z8', 'Z9', 'Z10', 'Z11'],
                    'T': ['T8', 'T9', 'T10', 'T11']}
                  )
df1
X	Y	Z	T
0	X0	Y0	Z0	T0
1	X1	Y1	Z1	T1
2	X2	Y2	Z2	T2
3	X3	Y3	Z3	T3
df2
X	Y	Z	T
0	X4	Y4	Z4	T4
1	X5	Y5	Z5	T5
2	X6	Y6	Z6	T6
3	X7	Y7	Z7	T7
df3
X	Y	Z	T
0	X8	Y8	Z8	T8
1	X9	Y9	Z9	T9
2	X10	Y10	Z10	T10
3	X11	Y11	Z11	T11
pd.concat([df1, df2, df3])
X	Y	Z	T
0	X0	Y0	Z0	T0
1	X1	Y1	Z1	T1
2	X2	Y2	Z2	T2
3	X3	Y3	Z3	T3
0	X4	Y4	Z4	T4
1	X5	Y5	Z5	T5
2	X6	Y6	Z6	T6
3	X7	Y7	Z7	T7
0	X8	Y8	Z8	T8
1	X9	Y9	Z9	T9
2	X10	Y10	Z10	T10
3	X11	Y11	Z11	T11
pd.concat([df1, df2, df3], ignore_index = True)
X	Y	Z	T
0	X0	Y0	Z0	T0
1	X1	Y1	Z1	T1
2	X2	Y2	Z2	T2
3	X3	Y3	Z3	T3
4	X4	Y4	Z4	T4
5	X5	Y5	Z5	T5
6	X6	Y6	Z6	T6
7	X7	Y7	Z7	T7
8	X8	Y8	Z8	T8
9	X9	Y9	Z9	T9
10	X10	Y10	Z10	T10
11	X11	Y11	Z11	T11
df1.columns
Index(['X', 'Y', 'Z', 'T'], dtype='object')
df2.columns = ["X", "Y", "Z", "A"]
df2
X	Y	Z	A
0	X4	Y4	Z4	T4
1	X5	Y5	Z5	T5
2	X6	Y6	Z6	T6
3	X7	Y7	Z7	T7
df1
X	Y	Z	T
0	X0	Y0	Z0	T0
1	X1	Y1	Z1	T1
2	X2	Y2	Z2	T2
3	X3	Y3	Z3	T3
pd.concat([df1, df2], ignore_index = True)
X	Y	Z	T	A
0	X0	Y0	Z0	T0	NaN
1	X1	Y1	Z1	T1	NaN
2	X2	Y2	Z2	T2	NaN
3	X3	Y3	Z3	T3	NaN
4	X4	Y4	Z4	NaN	T4
5	X5	Y5	Z5	NaN	T5
6	X6	Y6	Z6	NaN	T6
7	X7	Y7	Z7	NaN	T7
pd.concat([df1, df2], ignore_index = True, join = "inner")
X	Y	Z
0	X0	Y0	Z0
1	X1	Y1	Z1
2	X2	Y2	Z2
3	X3	Y3	Z3
4	X4	Y4	Z4
5	X5	Y5	Z5
6	X6	Y6	Z6
7	X7	Y7	Z7
pd.concat([df1, df2, df3], axis = 1)
X	Y	Z	T	X	Y	Z	A	X	Y	Z	T
0	X0	Y0	Z0	T0	X4	Y4	Z4	T4	X8	Y8	Z8	T8
1	X1	Y1	Z1	T1	X5	Y5	Z5	T5	X9	Y9	Z9	T9
2	X2	Y2	Z2	T2	X6	Y6	Z6	T6	X10	Y10	Z10	T10
3	X3	Y3	Z3	T3	X7	Y7	Z7	T7	X11	Y11	Z11	T11
df1 = pd.DataFrame({'X': ['X0', 'X1', 'X2', 'X3'],
                    'Y': ['Y0', 'Y1', 'Y2', 'Y3'],
                    'Z': ['Z0', 'Z1', 'Z2', 'Z3'],
                    'T': ['T0', 'T1', 'T2', 'T3']},
                   index = [1, 2, 3, 4]
                  )
df2 = pd.DataFrame({'X': ['X4', 'X5', 'X6', 'X7'],
                    'Y': ['Y4', 'Y5', 'Y6', 'Y7'],
                    'Z': ['Z4', 'Z5', 'Z6', 'Z7'],
                    'T': ['T4', 'T5', 'T6', 'T7']},
                   index = [5, 6, 7, 8]
                  )
df3 = pd.DataFrame({'X': ['X8', 'X9', 'X10', 'X11'],
                    'Y': ['Y8', 'Y9', 'Y10', 'Y11'],
                    'Z': ['Z8', 'Z9', 'Z10', 'Z11'],
                    'T': ['T8', 'T9', 'T10', 'T11']},
                   index = [9, 10, 11, 12]
                  )
df1
X	Y	Z	T
1	X0	Y0	Z0	T0
2	X1	Y1	Z1	T1
3	X2	Y2	Z2	T2
4	X3	Y3	Z3	T3
df2
X	Y	Z	T
5	X4	Y4	Z4	T4
6	X5	Y5	Z5	T5
7	X6	Y6	Z6	T6
8	X7	Y7	Z7	T7
df3
X	Y	Z	T
9	X8	Y8	Z8	T8
10	X9	Y9	Z9	T9
11	X10	Y10	Z10	T10
12	X11	Y11	Z11	T11
pd.concat([df1, df2, df3], axis = 1)
X	Y	Z	T	X	Y	Z	T	X	Y	Z	T
1	X0	Y0	Z0	T0	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
2	X1	Y1	Z1	T1	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
3	X2	Y2	Z2	T2	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
4	X3	Y3	Z3	T3	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
5	NaN	NaN	NaN	NaN	X4	Y4	Z4	T4	NaN	NaN	NaN	NaN
6	NaN	NaN	NaN	NaN	X5	Y5	Z5	T5	NaN	NaN	NaN	NaN
7	NaN	NaN	NaN	NaN	X6	Y6	Z6	T6	NaN	NaN	NaN	NaN
8	NaN	NaN	NaN	NaN	X7	Y7	Z7	T7	NaN	NaN	NaN	NaN
9	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	X8	Y8	Z8	T8
10	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	X9	Y9	Z9	T9
11	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	X10	Y10	Z10	T10
12	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	X11	Y11	Z11	T11
pd.concat([df1, df2, df3], axis = 1, join = "inner")
X	Y	Z	T	X	Y	Z	T	X	Y	Z	T
