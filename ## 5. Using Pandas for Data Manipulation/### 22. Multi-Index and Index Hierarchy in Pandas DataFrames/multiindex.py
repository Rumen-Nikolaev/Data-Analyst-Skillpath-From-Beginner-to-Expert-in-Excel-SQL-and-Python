import numpy as np
import pandas as pd
inside = ["class A", "class B", "class C", "class A", "class B", "class C"]
outside = ["school 1", "school 1", "school 1", "school 2", "school 2", "school 2"]
zip(outside, inside)
<zip at 0x7c6a1e51ad00>
multi_index = list(zip(outside, inside))
multi_index
[('school 1', 'class A'),
 ('school 1', 'class B'),
 ('school 1', 'class C'),
 ('school 2', 'class A'),
 ('school 2', 'class B'),
 ('school 2', 'class C')]
 hier_index = pd.MultiIndex.from_tuples(multi_index)
hier_index
MultiIndex([('school 1', 'class A'),
            ('school 1', 'class B'),
            ('school 1', 'class C'),
            ('school 2', 'class A'),
            ('school 2', 'class B'),
            ('school 2', 'class C')],
           )
np.random.seed(101)
df = pd.DataFrame(np.random.randint(70, 100, size = (6, 2)), index = hier_index, columns = ["1st_semester", "2st_semester"])
df
1st_semester	2st_semester
school 1	class A	81	87
class B	76	93
class C	99	81
school 2	class A	85	79
class B	83	78
class C	74	78
