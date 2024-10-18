import pandas as pd
example = pd.Series([10, 20, 30, 40, 50, 60, 70])
example
0    10
1    20
2    30
3    40
4    50
5    60
6    70
dtype: int64
example.axes
[RangeIndex(start=0, stop=7, step=1)]
example.dtype
dtype('int64')
example.size
7
example.ndim
1
example.head()
0    10
1    20
2    30
3    40
4    50
dtype: int64
example.head(3)
0    10
1    20
2    30
dtype: int64
example.tail()
2    30
3    40
4    50
5    60
6    70
dtype: int64
