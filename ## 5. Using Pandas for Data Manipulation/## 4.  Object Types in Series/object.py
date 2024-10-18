import pandas as pd
pd.Series(["world", 100, 5.8, False])
0    world
1      100
2      5.8
3    False
dtype: object
example = pd.Series(["world", 100, 5.8, False])
example[0]
'world'
print(type(example[0]))
<class 'str'>
print(type(example[1]))
print(type(example[2]))
print(type(example[3]))
<class 'int'>
<class 'float'>
<class 'bool'>
pd.Series([sum, type, max])
0    <built-in function sum>
1             <class 'type'>
2    <built-in function max>
dtype: object
