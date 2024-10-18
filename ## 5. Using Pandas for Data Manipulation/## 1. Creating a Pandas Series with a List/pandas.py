import pandas as pd
pd.Series([10, 20, 30, 40, 50])
0    10
1    20
2    30
3    40
4    50
dtype: int64
list_data = [2, 4, 6, 8, 10]
list_index = ["a", "b", "c", "d", "e"]
variable = pd.Series(data = list_data, index = list_index, dtype = "float")
variable
a     2.0
b     4.0
c     6.0
d     8.0
e    10.0
dtype: float64
