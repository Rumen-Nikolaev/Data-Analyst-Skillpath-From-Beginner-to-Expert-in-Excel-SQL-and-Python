import numpy as np
import pandas as pd
inside = ["class A", "class B", "class C", "class A", "class B", "class C"]
outside = ['school1', 'school1', 'school1', 'school2', 'school2', 'school2']

multi_index = list(zip(outside, inside))

hier_index = pd.MultiIndex.from_tuples(multi_index)

np.random.seed(101)
df = pd.DataFrame(np.random.randint(70, 100, size = (6, 2)), index = hier_index, columns = ["1st_semester", "2st_semester"])
df
1st_semester	2st_semester
school1	class A	81	87
class B	76	93
class C	99	81
school2	class A	85	79
class B	83	78
class C	74	78
df["1st_semester"]
school1  class A    81
         class B    76
         class C    99
school2  class A    85
         class B    83
         class C    74
Name: 1st_semester, dtype: int64
df[["1st_semester"]]
1st_semester
school1	class A	81
class B	76
class C	99
school2	class A	85
class B	83
class C	74
df[["2st_semester"]]
2st_semester
school1	class A	87
class B	93
class C	81
school2	class A	79
class B	78
class C	78
df
1st_semester	2st_semester
school1	class A	81	87
class B	76	93
class C	99	81
school2	class A	85	79
class B	83	78
class C	74	78
df.loc["school1"]
1st_semester	2st_semester
class A	81	87
class B	76	93
class C	99	81
df.loc["school1"].loc["class B"]
1st_semester    76
2st_semester    93
Name: class B, dtype: int64
df.loc["school1"].loc[["class B"]]
1st_semester	2st_semester
class B	76	93
df
1st_semester	2st_semester
school1	class A	81	87
class B	76	93
class C	99	81
school2	class A	85	79
class B	83	78
class C	74	78
df.index
MultiIndex([('school1', 'class A'),
            ('school1', 'class B'),
            ('school1', 'class C'),
            ('school2', 'class A'),
            ('school2', 'class B'),
            ('school2', 'class C')],
           )
df.index.names
FrozenList([None, None])
df.index.names = ["schools", "classes"]
df
1st_semester	2st_semester
schools	classes		
school1	class A	81	87
class B	76	93
class C	99	81
school2	class A	85	79
class B	83	78
class C	74	78
