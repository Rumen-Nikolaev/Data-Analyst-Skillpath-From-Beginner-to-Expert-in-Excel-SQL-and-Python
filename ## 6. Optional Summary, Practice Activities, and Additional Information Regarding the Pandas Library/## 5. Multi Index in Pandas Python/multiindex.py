import numpy as np
import pandas as pd
Outer_Index = ["Group1","Group1","Group1","Group2","Group2","Group2","Group3","Group3","Group3",]
Inner_Index = ["Index1","Index2","Index3","Index1","Index2","Index3","Index1","Index2","Index3",] 
list(zip(Outer_Index,Inner_Index))
[('Group1', 'Index1'),
 ('Group1', 'Index2'),
 ('Group1', 'Index3'),
 ('Group2', 'Index1'),
 ('Group2', 'Index2'),
 ('Group2', 'Index3'),
 ('Group3', 'Index1'),
 ('Group3', 'Index2'),
 ('Group3', 'Index3')]
Hierarchy = list(zip(Outer_Index,Inner_Index))
Hierarchy
[('Group1', 'Index1'),
 ('Group1', 'Index2'),
 ('Group1', 'Index3'),
 ('Group2', 'Index1'),
 ('Group2', 'Index2'),
 ('Group2', 'Index3'),
 ('Group3', 'Index1'),
 ('Group3', 'Index2'),
 ('Group3', 'Index3')]
Hierarchy = pd.MultiIndex.from_tuples(Hierarchy)
Hierarchy
MultiIndex([('Group1', 'Index1'),
            ('Group1', 'Index2'),
            ('Group1', 'Index3'),
            ('Group2', 'Index1'),
            ('Group2', 'Index2'),
            ('Group2', 'Index3'),
            ('Group3', 'Index1'),
            ('Group3', 'Index2'),
            ('Group3', 'Index3')],
           )
Hierarchy.levels
FrozenList([['Group1', 'Group2', 'Group3'], ['Index1', 'Index2', 'Index3']])
Hierarchy.labels
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[11], line 1
----> 1 Hierarchy.labels

AttributeError: 'MultiIndex' object has no attribute 'labels'
Hierarchy.codes
FrozenList([[0, 0, 0, 1, 1, 1, 2, 2, 2], [0, 1, 2, 0, 1, 2, 0, 1, 2]])
R_Value = np.random.randint(1,300,45)
R_Value = R_Value.reshape(9,5)
R_Value
array([[273, 295, 161,  54,  70],
       [ 44, 295, 134, 262, 118],
       [165, 165, 248, 262, 249],
       [265,   5, 139, 274,  71],
       [ 97, 205,  61,   2, 192],
       [ 79, 134, 258, 242,  12],
       [  1, 107, 290, 105, 192],
       [202, 175, 123,  53,  35],
       [ 38, 247,  73, 145,  80]], dtype=int32)
DF_1 = pd.DataFrame(R_Value, Hierarchy, columns=["Column 1","Column 2","Column 3","Column 4","Column 5"])
DF_1
Column 1	Column 2	Column 3	Column 4	Column 5
Group1	Index1	273	295	161	54	70
Index2	44	295	134	262	118
Index3	165	165	248	262	249
Group2	Index1	265	5	139	274	71
Index2	97	205	61	2	192
Index3	79	134	258	242	12
Group3	Index1	1	107	290	105	192
Index2	202	175	123	53	35
Index3	38	247	73	145	80
DF_1["Column 2"]
Group1  Index1    295
        Index2    295
        Index3    165
Group2  Index1      5
        Index2    205
        Index3    134
Group3  Index1    107
        Index2    175
        Index3    247
Name: Column 2, dtype: int32
DF_1.loc["Group2"]
Column 1	Column 2	Column 3	Column 4	Column 5
Index1	265	5	139	274	71
Index2	97	205	61	2	192
Index3	79	134	258	242	12
DF_1.loc[["Group1","Group2"]]
Column 1	Column 2	Column 3	Column 4	Column 5
Group1	Index1	273	295	161	54	70
Index2	44	295	134	262	118
Index3	165	165	248	262	249
Group2	Index1	265	5	139	274	71
Index2	97	205	61	2	192
Index3	79	134	258	242	12
DF_1.loc["Group2"].loc["Index3"]
Column 1     79
Column 2    134
Column 3    258
Column 4    242
Column 5     12
Name: Index3, dtype: int32
DF_1.index.names = ["Groups","Indexes"]
DF_1
Column 1	Column 2	Column 3	Column 4	Column 5
Groups	Indexes					
Group1	Index1	273	295	161	54	70
Index2	44	295	134	262	118
Index3	165	165	248	262	249
Group2	Index1	265	5	139	274	71
Index2	97	205	61	2	192
Index3	79	134	258	242	12
Group3	Index1	1	107	290	105	192
Index2	202	175	123	53	35
Index3	38	247	73	145	80
DF_1.xs("Group2")
Column 1	Column 2	Column 3	Column 4	Column 5
Indexes					
Index1	265	5	139	274	71
Index2	97	205	61	2	192
Index3	79	134	258	242	12
DF_1.xs("Index1",level = "Indexes")
Column 1	Column 2	Column 3	Column 4	Column 5
Groups					
Group1	273	295	161	54	70
Group2	265	5	139	274	71
Group3	1	107	290	105	192
DF_1
Column 1	Column 2	Column 3	Column 4	Column 5
Groups	Indexes					
Group1	Index1	273	295	161	54	70
Index2	44	295	134	262	118
Index3	165	165	248	262	249
Group2	Index1	265	5	139	274	71
Index2	97	205	61	2	192
Index3	79	134	258	242	12
Group3	Index1	1	107	290	105	192
Index2	202	175	123	53	35
Index3	38	247	73	145	80
 
