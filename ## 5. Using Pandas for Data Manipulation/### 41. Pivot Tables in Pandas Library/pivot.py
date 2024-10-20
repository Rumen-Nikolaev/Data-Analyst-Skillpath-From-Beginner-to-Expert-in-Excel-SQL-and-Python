import pandas as pd
import seaborn as sns
import numpy as np
df = sns.load_dataset("titanic")
df.head()
survived	pclass	sex	age	sibsp	parch	fare	embarked	class	who	adult_male	deck	embark_town	alive	alone
0	0	3	male	22.0	1	0	7.2500	S	Third	man	True	NaN	Southampton	no	False
1	1	1	female	38.0	1	0	71.2833	C	First	woman	False	C	Cherbourg	yes	False
2	1	3	female	26.0	0	0	7.9250	S	Third	woman	False	NaN	Southampton	yes	True
3	1	1	female	35.0	1	0	53.1000	S	First	woman	False	C	Southampton	yes	False
4	0	3	male	35.0	0	0	8.0500	S	Third	man	True	NaN	Southampton	no	True
df.groupby("sex")[["survived"]].mean()
survived
sex	
female	0.742038
male	0.188908
df.groupby(["sex", "embark_town"])[["survived"]].mean()
survived
sex	embark_town	
female	Cherbourg	0.876712
Queenstown	0.750000
Southampton	0.689655
male	Cherbourg	0.305263
Queenstown	0.073171
Southampton	0.174603
df.groupby(["sex", "embark_town"])[["survived"]].mean().unstack()
survived
embark_town	Cherbourg	Queenstown	Southampton
sex			
female	0.876712	0.750000	0.689655
male	0.305263	0.073171	0.174603
df.pivot_table("survived", index = "sex", columns = "embark_town")
embark_town	Cherbourg	Queenstown	Southampton
sex			
female	0.876712	0.750000	0.689655
male	0.305263	0.073171	0.174603
df.pivot_table("survived", index = "sex", columns = "embark_town", aggfunc = ["sum", "mean", "std"])
sum	mean	std
embark_town	Cherbourg	Queenstown	Southampton	Cherbourg	Queenstown	Southampton	Cherbourg	Queenstown	Southampton
sex									
female	64	27	140	0.876712	0.750000	0.689655	0.331042	0.439155	0.463778
male	29	3	77	0.305263	0.073171	0.174603	0.462962	0.263652	0.380058
df.pivot_table("survived", index = ["sex", "class"], columns = "embark_town", aggfunc = ["sum", "mean", "std"])
	sum	mean	std
embark_town	Cherbourg	Queenstown	Southampton	Cherbourg	Queenstown	Southampton	Cherbourg	Queenstown	Southampton
sex	class									
female	First	42	1	46	0.976744	1.000000	0.958333	0.152499	NaN	0.201941
Second	7	2	61	1.000000	1.000000	0.910448	0.000000	0.000000	0.287694
Third	15	24	33	0.652174	0.727273	0.375000	0.486985	0.452267	0.486897
male	First	17	0	28	0.404762	0.000000	0.354430	0.496796	NaN	0.481397
Second	2	0	15	0.200000	0.000000	0.154639	0.421637	NaN	0.363439
Third	10	3	34	0.232558	0.076923	0.128302	0.427463	0.269953	0.335058
