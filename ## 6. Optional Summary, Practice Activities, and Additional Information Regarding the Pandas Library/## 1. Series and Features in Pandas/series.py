import numpy as np
import pandas as pd
P_Series = pd.Series([7,11,19,113])
P_Series
0      7
1     11
2     19
3    113
dtype: int64
P_Series_2 = pd.Series(29,range(5))
P_Series_2
0    29
1    29
2    29
3    29
4    29
dtype: int64
P_Series[3]
np.int64(113)
P_Series_3 = pd.Series(np.random.randint(1,150,20))
P_Series_3
0      73
1      27
2     125
3      23
4      77
5      24
6      13
7      60
8      46
9     121
10     59
11     33
12    139
13     24
14     51
15     27
16     71
17     11
18     91
19    124
dtype: int32
P_Series_3.max()
np.int32(139)
P_Series_3.min()
np.int32(11)
P_Series_3.mean()
np.float64(60.95)
P_Series_3.std()
np.float64(40.75662684250191)
P_Series_3.describe()
count     20.000000
mean      60.950000
std       40.756627
min       11.000000
25%       26.250000
50%       55.000000
75%       80.500000
max      139.000000
dtype: float64
P_Series_3.head()
0     73
1     27
2    125
3     23
4     77
dtype: int32
P_Series_3.head(2)
0    73
1    27
dtype: int32
P_Series_3.head(7)
0     73
1     27
2    125
3     23
4     77
5     24
6     13
dtype: int32
P_Series_3.tail()
15     27
16     71
17     11
18     91
19    124
dtype: int32
P_Series_3.tail(2)
18     91
19    124
dtype: int32
P_Series_3.tail(7)
13     24
14     51
15     27
16     71
17     11
18     91
19    124
dtype: int32
P_Series_4 = pd.Series([5,13,23,29], index = ["Joe","William","Jack","Avarell"])
P_Series_4
Joe         5
William    13
Jack       23
Avarell    29
dtype: int64
P_Series_4["Avarell"]
np.int64(29)
P_Series_4.Joe
np.int64(5)
P_Series_D = pd.Series({"One":1,"Two":2,"Three":3,"Four":4,"Five":5})
P_Series_D
One      1
Two      2
Three    3
Four     4
Five     5
dtype: int64
P_Series_S = pd.Series(["Tom","Jerry","Spike","Tyke","Nibbles","Quacker"])
P_Series_S
0        Tom
1      Jerry
2      Spike
3       Tyke
4    Nibbles
5    Quacker
dtype: object
P_Series_S.str.contains("e")
0    False
1     True
2     True
3     True
4     True
5     True
dtype: bool
P_Series_S.str.upper()
0        TOM
1      JERRY
2      SPIKE
3       TYKE
4    NIBBLES
5    QUACKER
dtype: object
Data = [1,2,3,4,5,6]
Label = ["apple","cherry","banana","orange","pear","melon"]
pd.Series(data = Data, index = Label)
apple     1
cherry    2
banana    3
orange    4
pear      5
melon     6
dtype: int64
SD_LW = pd.Series([70,63,150,45,33,35],["Chocolate","Bread","Biscuits","Potatoes(kg)","Carrots(kg)","Chips"])
SD_TW = pd.Series([45,51,90,67,44,13],["Chocolate","Bread","Biscuits","Potatoes(kg)","Carrots(kg)","Crackers"])
SD_LW
Chocolate       45
Bread           51
Biscuits        90
Potatoes(kg)    67
Carrots(kg)     44
Crackers        13
dtype: int64
SD_TW
Chocolate       45
Bread           51
Biscuits        90
Potatoes(kg)    67
Carrots(kg)     44
Crackers        13
dtype: int64
SD_LW + SD_TW
Chocolate        90
Bread           102
Biscuits        180
Potatoes(kg)    134
Carrots(kg)      88
Crackers         26
dtype: int64
 
