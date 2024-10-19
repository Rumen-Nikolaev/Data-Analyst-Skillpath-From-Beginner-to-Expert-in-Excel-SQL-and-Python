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
df.loc["C":"H", "VAL2":"VAL4"]
VAL2	VAL3	VAL4
C	15	22	39
D	39	44	18
E	22	41	33
F	18	46	29
G	17	20	49
H	28	17	49
df.iloc[2:8, 1:4]
VAL2	VAL3	VAL4
C	15	22	39
D	39	44	18
E	22	41	33
F	18	46	29
G	17	20	49
H	28	17	49
df.iloc[2:8, 1:4].loc["E":"F", ["VAL3"]]
VAL3
E	41
F	46
