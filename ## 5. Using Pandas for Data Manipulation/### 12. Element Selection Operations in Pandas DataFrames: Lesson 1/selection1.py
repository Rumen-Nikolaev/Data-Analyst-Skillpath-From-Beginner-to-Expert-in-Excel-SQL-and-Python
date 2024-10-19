import numpy as np
import pandas as pd
 
np.random.seed(101)
df = pd.DataFrame(data = np.random.randn(6, 5), index = "A B C D E F".split(), columns = ["VAL1 VAL2 VAL3 VAL4 VAL5".split()])
df
VAL1	VAL2	VAL3	VAL4	VAL5
A	2.706850	0.628133	0.907969	0.503826	0.651118
B	-0.319318	-0.848077	0.605965	-2.018168	0.740122
C	0.528813	-0.589001	0.188695	-0.758872	-0.933237
D	0.955057	0.190794	1.978757	2.605967	0.683509
E	0.302665	1.693723	-1.706086	-1.159119	-0.134841
F	0.390528	0.166905	0.184502	0.807706	0.072960
df["VAL1"]
VAL1
A	2.706850
B	-0.319318
C	0.528813
D	0.955057
E	0.302665
F	0.390528
df.VAL1
VAL1
A	2.706850
B	-0.319318
C	0.528813
D	0.955057
E	0.302665
F	0.390528
df["VAL1"].values
array([[ 2.70684984],
       [-0.31931804],
       [ 0.52881349],
       [ 0.95505651],
       [ 0.30266545],
       [ 0.39052784]])
df[["VAL1"]]
VAL1
A	2.706850
B	-0.319318
C	0.528813
D	0.955057
E	0.302665
F	0.390528
df[["VAL1"]]["B":"D"]
VAL1
B	-0.319318
C	0.528813
D	0.955057
df[["VAL1"]][1:4]
VAL1
B	-0.319318
C	0.528813
D	0.955057
