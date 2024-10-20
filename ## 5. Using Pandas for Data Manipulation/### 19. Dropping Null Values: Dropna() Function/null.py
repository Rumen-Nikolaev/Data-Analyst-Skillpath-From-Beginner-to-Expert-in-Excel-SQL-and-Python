import numpy as np
import pandas as pd
df = pd.DataFrame({'VAL1':[2,4, np.nan, 6, np.nan, 8, 10],
                  'VAL2':[123, np.nan, 456, np.nan, 789, 246, 357],
                   'VAL3':['France','Greece','USA','Japan','Sweden','Norway','Turkey']})
df
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	NaN	Greece
2	NaN	456.0	USA
3	6.0	NaN	Japan
4	NaN	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
df.dropna()
VAL1	VAL2	VAL3
0	2.0	123.0	France
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
df.dropna(axis = 1)
VAL3
0	France
1	Greece
2	USA
3	Japan
4	Sweden
5	Norway
6	Turkey
df["VAL4"] = np.nan
df
VAL1	VAL2	VAL3	VAL4
0	2.0	123.0	France	NaN
1	4.0	NaN	Greece	NaN
2	NaN	456.0	USA	NaN
3	6.0	NaN	Japan	NaN
4	NaN	789.0	Sweden	NaN
5	8.0	246.0	Norway	NaN
6	10.0	357.0	Turkey	NaN
df.dropna(how = "all")
VAL1	VAL2	VAL3	VAL4
0	2.0	123.0	France	NaN
1	4.0	NaN	Greece	NaN
2	NaN	456.0	USA	NaN
3	6.0	NaN	Japan	NaN
4	NaN	789.0	Sweden	NaN
5	8.0	246.0	Norway	NaN
6	10.0	357.0	Turkey	NaN
df.dropna(how = "all", axis = 1)
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	NaN	Greece
2	NaN	456.0	USA
3	6.0	NaN	Japan
4	NaN	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
df
VAL1	VAL2	VAL3	VAL4
0	2.0	123.0	France	NaN
1	4.0	NaN	Greece	NaN
2	NaN	456.0	USA	NaN
3	6.0	NaN	Japan	NaN
4	NaN	789.0	Sweden	NaN
5	8.0	246.0	Norway	NaN
6	10.0	357.0	Turkey	NaN
df.dropna(how = "all", axis = 1, inplace = True)
df
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	NaN	Greece
2	NaN	456.0	USA
3	6.0	NaN	Japan
4	NaN	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
