import numpy as np
import pandas as pd
np.random.seed(101)

array = np.random.randint(10, 50, (10, 5))
df = pd.DataFrame(data = array, index = "A B C D E F G H I J".split(), columns = "VAL1 VAL2 VAL3 VAL4 VAL5".split())
df
VAL1	VAL2	VAL3	VAL4	VAL5
A	41	21	27	16	33
B	21	19	23	14	38
C	10	15	22	39	29
D	18	39	44	18	29
E	20	22	41	33	10
F	19	18	46	29	45
G	38	17	20	49	48
H	19	28	17	49	25
I	10	22	27	21	25
J	43	39	34	46	29
df > 20
VAL1	VAL2	VAL3	VAL4	VAL5
A	True	True	True	False	True
B	True	False	True	False	True
C	False	False	True	True	True
D	False	True	True	False	True
E	False	True	True	True	False
F	False	False	True	True	True
G	True	False	False	True	True
H	False	True	False	True	True
I	False	True	True	True	True
J	True	True	True	True	True
df[df > 20]
VAL1	VAL2	VAL3	VAL4	VAL5
A	41.0	21.0	27.0	NaN	33.0
B	21.0	NaN	23.0	NaN	38.0
C	NaN	NaN	22.0	39.0	29.0
D	NaN	39.0	44.0	NaN	29.0
E	NaN	22.0	41.0	33.0	NaN
F	NaN	NaN	46.0	29.0	45.0
G	38.0	NaN	NaN	49.0	48.0
H	NaN	28.0	NaN	49.0	25.0
I	NaN	22.0	27.0	21.0	25.0
J	43.0	39.0	34.0	46.0	29.0
df["VAL1"] < 20
A    False
B    False
C     True
D     True
E    False
F     True
G    False
H     True
I     True
J    False
Name: VAL1, dtype: bool
df[df["VAL1"] < 20]
VAL1	VAL2	VAL3	VAL4	VAL5
C	10	15	22	39	29
D	18	39	44	18	29
F	19	18	46	29	45
H	19	28	17	49	25
I	10	22	27	21	25
df[df["VAL1"] < 20]["VAL2"]
C    15
D    39
F    18
H    28
I    22
Name: VAL2, dtype: int64
df[df["VAL1"] < 20]["VAL2"]
C    15
D    39
F    18
H    28
I    22
Name: VAL2, dtype: int64
df[df["VAL1"] < 20][["VAL2"]]
VAL2
C	15
D	39
F	18
H	28
I	22
df[df["VAL1"] < 20][["VAL2", "VAL5"]]
VAL2	VAL5
C	15	29
D	39	29
F	18	45
H	28	25
I	22	25
df
VAL1	VAL2	VAL3	VAL4	VAL5
A	41	21	27	16	33
B	21	19	23	14	38
C	10	15	22	39	29
D	18	39	44	18	29
E	20	22	41	33	10
F	19	18	46	29	45
G	38	17	20	49	48
H	19	28	17	49	25
I	10	22	27	21	25
J	43	39	34	46	29
df[(df["VAL1"] > 20) & (df["VAL4"] < 18)]
VAL1	VAL2	VAL3	VAL4	VAL5
A	41	21	27	16	33
B	21	19	23	14	38
df[(df < 35) | (df["VAL5"] > 20)]
VAL1	VAL2	VAL3	VAL4	VAL5
A	NaN	21.0	27.0	16.0	33.0
B	21.0	19.0	23.0	14.0	NaN
C	10.0	15.0	22.0	NaN	29.0
D	18.0	NaN	NaN	18.0	29.0
E	20.0	22.0	NaN	33.0	10.0
F	19.0	18.0	NaN	29.0	NaN
G	NaN	17.0	20.0	NaN	NaN
H	19.0	28.0	17.0	NaN	25.0
I	10.0	22.0	27.0	21.0	25.0
J	NaN	NaN	34.0	NaN	29.0
df
VAL1	VAL2	VAL3	VAL4	VAL5
A	41	21	27	16	33
B	21	19	23	14	38
C	10	15	22	39	29
D	18	39	44	18	29
E	20	22	41	33	10
F	19	18	46	29	45
G	38	17	20	49	48
H	19	28	17	49	25
I	10	22	27	21	25
J	43	39	34	46	29
df.loc[df.VAL2 > 25, ["VAL2", "VAL3", "VAL5"]]
VAL2	VAL3	VAL5
D	39	44	29
H	28	17	25
J	39	34	29
