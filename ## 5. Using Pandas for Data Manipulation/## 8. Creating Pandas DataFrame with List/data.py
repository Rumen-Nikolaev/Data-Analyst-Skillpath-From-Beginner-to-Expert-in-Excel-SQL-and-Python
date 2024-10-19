import pandas as pd
list_example = [5, 10, 15, 20, 25]
list_example
[5, 10, 15, 20, 25]
pd.DataFrame(data = list_example, columns = ["values"], dtype = "float")
values
0	5.0
1	10.0
2	15.0
3	20.0
4	25.0
