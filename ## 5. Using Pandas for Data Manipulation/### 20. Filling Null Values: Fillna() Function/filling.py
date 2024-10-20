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
df.fillna(100000)
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	100000.0	Greece
2	100000.0	456.0	USA
3	6.0	100000.0	Japan
4	100000.0	789.0	Sweden
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
df["VAL1"].fillna(10000)
0        2.0
1        4.0
2    10000.0
3        6.0
4    10000.0
5        8.0
6       10.0
Name: VAL1, dtype: float64
df
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	NaN	Greece
2	NaN	456.0	USAimport numpy as np
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
df.fillna(100000)
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	100000.0	Greece
2	100000.0	456.0	USA
3	6.0	100000.0	Japan
4	100000.0	789.0	Sweden
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
df["VAL1"].fillna(10000)
0        2.0
1        4.0
2    10000.0
3        6.0
4    10000.0
5        8.0
6       10.0
Name: VAL1, dtype: float64
df
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	NaN	Greece
2	NaN	456.0	USA
3	6.0	NaN	Japan
4	NaN	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
df.mean()
/tmp/ipykernel_14141/3698961737.py:1: FutureWarning: The default value of numeric_only in DataFrame.mean is deprecated. In a future version, it will default to False. In addition, specifying 'numeric_only=None' is deprecated. Select only valid columns or specify the value of numeric_only to silence this warning.
  df.mean()
VAL1      6.0
VAL2    394.2
dtype: float64
df.fillna(df.mean())
/tmp/ipykernel_14141/634187881.py:1: FutureWarning: The default value of numeric_only in DataFrame.mean is deprecated. In a future version, it will default to False. In addition, specifying 'numeric_only=None' is deprecated. Select only valid columns or specify the value of numeric_only to silence this warning.
  df.fillna(df.mean())
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	394.2	Greece
2	6.0	456.0	USA
3	6.0	394.2	Japan
4	6.0	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
df.fillna({"VAL1":100000, "VAL2":200000})
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	200000.0	Greece
2	100000.0	456.0	USA
3	6.0	200000.0	Japan
4	100000.0	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
df["VAL1"].fillna(df["VAL2"].mean())
0      2.0
1      4.0
2    394.2
3      6.0
4    394.2
5      8.0
6     10.0
Name: VAL1, dtype: float64
df
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	NaN	Greece
2	NaN	456.0	USA
3	6.0	NaN	Japan
4	NaN	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
df["VAL3"][0::2]
0    France
2       USA
4    Sweden
6    Turkey
Name: VAL3, dtype: object
df
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	NaN	Greece
2	NaN	456.0	USA
3	6.0	NaN	Japan
4	NaN	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
df["VAL3"].fillna("Turkey")
0    France
1    Greece
2       USA
3     Japan
4    Sweden
5    Norway
6    Turkey
Name: VAL3, dtype: object
df.fillna(method = "ffill")
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	123.0	Greece
2	4.0	456.0	USA
3	6.0	456.0	Japan
4	6.0	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
df.fillna(method = "pad")
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	123.0	Greece
2	4.0	456.0	USA
3	6.0	456.0	Japan
4	6.0	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
df.fillna(method = "bfill")
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	456.0	Greece
2	6.0	456.0	USA
3	6.0	789.0	Japan
4	8.0	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
df.fillna(method = "backfill")
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	456.0	Greece
2	6.0	456.0	USA
3	6.0	789.0	Japan
4	8.0	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
3	6.0	NaN	Japan
4	NaN	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
df.mean()
/tmp/ipykernel_14141/3698961737.py:1: FutureWarning: The default value of numeric_only in DataFrame.mean is deprecated. In a future version, it will default to False. In addition, specifying 'numeric_only=None' is deprecated. Select only valid columns or specify the value of numeric_only to silence this warning.
  df.mean()
VAL1      6.0
VAL2    394.2
dtype: float64
df.fillna(df.mean())
/tmp/ipykernel_14141/634187881.py:1: FutureWarning: The default value of numeric_only in DataFrame.mean is deprecated. In a future version, it will default to False. In addition, specifying 'numeric_only=None' is deprecated. Select only valid columns or specify the value of numeric_only to silence this warning.
  df.fillna(df.mean())
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	394.2	Greece
2	6.0	456.0	USA
3	6.0	394.2	Japan
4	6.0	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
df.fillna({"VAL1":100000, "VAL2":200000})
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	200000.0	Greece
2	100000.0	456.0	USA
3	6.0	200000.0	Japan
4	100000.0	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
df["VAL1"].fillna(df["VAL2"].mean())
0      2.0
1      4.0
2    394.2
3      6.0
4    394.2
5      8.0
6     10.0
Name: VAL1, dtype: float64
df
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	NaN	Greece
2	NaN	456.0	USA
3	6.0	NaN	Japan
4	NaN	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
df["VAL3"][0::2]
0    France
2       USA
4    Sweden
6    Turkey
Name: VAL3, dtype: object
df
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	NaN	Greece
2	NaN	456.0	USA
3	6.0	NaN	Japan
4	NaN	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
df["VAL3"].fillna("Turkey")
0    France
1    Greece
2       USA
3     Japan
4    Sweden
5    Norway
6    Turkey
Name: VAL3, dtype: object
df.fillna(method = "ffill")
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	123.0	Greece
2	4.0	456.0	USA
3	6.0	456.0	Japan
4	6.0	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
df.fillna(method = "pad")
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	123.0	Greece
2	4.0	456.0	USA
3	6.0	456.0	Japan
4	6.0	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
df.fillna(method = "bfill")
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	456.0	Greece
2	6.0	456.0	USA
3	6.0	789.0	Japan
4	8.0	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
df.fillna(method = "backfill")
VAL1	VAL2	VAL3
0	2.0	123.0	France
1	4.0	456.0	Greece
2	6.0	456.0	USA
3	6.0	789.0	Japan
4	8.0	789.0	Sweden
5	8.0	246.0	Norway
6	10.0	357.0	Turkey
