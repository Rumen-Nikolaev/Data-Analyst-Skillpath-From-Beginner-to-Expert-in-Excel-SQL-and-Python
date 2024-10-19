import numpy as np
import pandas as pd
df = pd.DataFrame({'VAL1':[2, 4, np.nan, 6, np.nan, 8, 10],
                   'VAL2':[123, np.nan, 456, np.nan, 789, 246, 357],
                   'VAL3':['France', 'Greece', 'USA', 'Japan', 'Sweden', 'Norway', 'Turkey']})
df
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	NaN	Greece
2	NaN	456.0	USA
3	6.0	NaN	Japan
4	NaN	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
df.isnull()
VAL1	VAL2	VAL3
0	False	False	False
1	False	True	False
2	True	False	False
3	False	True	False
4	True	False	False
5	False	False	False
6	False	False	False
df.isnull().sum()
VAL1    2
VAL2    2
VAL3    0
dtype: int64
len(df)
7
df.isnull().sum() / len(df) * 100
VAL1    28.571429
VAL2    28.571429
VAL3     0.000000
dtype: float64
df.notnull()
VAL1	VAL2	VAL3
0	True	True	True
1	True	False	True
2	False	True	True
3	True	False	True
4	False	True	True
5	True	True	True
6	True	True	True
df.notnull().sum()
VAL1    5
VAL2    5
VAL3    7
dtype: int64
df.notnull().sum().sum()
np.int64(17)
df["VAL1"].notnull()
0     True
1     True
2    False
3     True
4    False
5     True
6     True
Name: VAL1, dtype: bool
df[df["VAL1"].notnull()]
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	NaN	Greece
3	6.0	NaN	Japan
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
df
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	NaN	Greece
2	NaN	456.0	USA
3	6.0	NaN	Japan
4	NaN	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
df.isnull().any()
VAL1     True
VAL2     True
VAL3    False
dtype: bool
df.isnull().any(axis = 1)
0    False
1     True
2     True
3     True
4     True
5    False
6    False
dtype: bool
condition = df.isnull().any(axis = 1)
df[condition]
VAL1	VAL2	VAL3
1	4.0	NaN	Greece
2	NaN	456.0	USA
3	6.0	NaN	Japan
4	NaN	789.0	Sweden
df[~condition]
VAL1	VAL2	VAL3
0	2.0	123.0	France
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
df.notnull().all()
VAL1    False
VAL2    False
VAL3     True
dtype: bool
df.notnull().all(axis = 1)
0     True
1    False
2    False
3    False
4    False
5     True
6     True
dtype: bool
