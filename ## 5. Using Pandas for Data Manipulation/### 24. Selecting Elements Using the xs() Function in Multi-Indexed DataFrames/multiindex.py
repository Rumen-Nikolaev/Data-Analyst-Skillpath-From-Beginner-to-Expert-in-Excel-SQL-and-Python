import numpy as np
import pandas as pd
inside = ["class A", "class B", "class C", "class A", "class B", "class B"]
outside = ['school1', 'school1', 'school1', 'school2', 'school2', 'school2']

multi_index = list(zip(outside, inside))

hier_index = pd.MultiIndex.from_tuples(multi_index)

np.random.seed(101)
df = pd.DataFrame(np.random.randint(70, 100, size = (6, 2)), index = hier_index, columns = ["1st_semester", "2st_semester"])

df.index.names = ["schools", "classes"]
df
1st_semester	2st_semester
schools	classes		
school1	class A	81	87
class B	76	93
class C	99	81
school2	class A	85	79
class B	83	78
class B	74	78
df.xs("school2")
1st_semester	2st_semester
classes		
class A	85	79
class B	83	78
class B	74	78
df.xs(("school2", "class A"))
1st_semester	2st_semester
schools	classes		
school2	class A	85	79
df
1st_semester	2st_semester
schools	classes		
school1	class A	81	87
class B	76	93
class C	99	81
school2	class A	85	79
class B	83	78
class B	74	78
df.xs(("school2", "class A"), level = [0, 1])
1st_semester	2st_semester
schools	classes		
school2	class A	85	79
df.xs("class A", level = "classes")
1st_semester	2st_semester
schools		
school1	81	87
school2	85	79
df.xs("class A", level = 1)
1st_semester	2st_semester
schools		
school1	81	87
school2	85	79
