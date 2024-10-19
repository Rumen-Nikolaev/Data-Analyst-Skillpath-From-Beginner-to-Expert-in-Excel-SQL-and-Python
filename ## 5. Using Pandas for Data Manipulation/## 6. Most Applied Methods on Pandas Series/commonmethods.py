import pandas as pd
variable = pd.Series([8, 3, 6, 5, 1], index = ["b", "d", "c", "a", "e"])
variable
b    8
d    3
c    6
a    5
e    1
dtype: int64
new_variable = variable.sort_index()
variable
b    8
d    3
c    6
a    5
e    1
dtype: int64
new_variable
a    5
b    8
c    6
d    3
e    1
dtype: int64
new_variable2 = variable.sort_values()
new_variable2
e    1
d    3
a    5
c    6
b    8
dtype: int64
variable
b    8
d    3
c    6
a    5
e    1
dtype: int64
variable.isin([6, 1])
b    False
d    False
c     True
a    False
e     True
dtype: bool
variable[variable.isin([6, 1])]
c    6
e    1
dtype: int64
variable.values
array([8, 3, 6, 5, 1])
[i for i in variable.values]
[np.int64(8), np.int64(3), np.int64(6), np.int64(5), np.int64(1)]
variable.index
Index(['b', 'd', 'c', 'a', 'e'], dtype='object')
[i for i in variable.index]
['b', 'd', 'c', 'a', 'e']
variable.items
<bound method Series.items of b    8
d    3
c    6
a    5
e    1
dtype: int64>
variable.items()
<zip at 0x78e5035916c0>
list(variable.items())
[('b', 8), ('d', 3), ('c', 6), ('a', 5), ('e', 1)]
for index, value in variable.items():
    print(index, "-", value)
b - 8
d - 3
c - 6
a - 5
e - 1
