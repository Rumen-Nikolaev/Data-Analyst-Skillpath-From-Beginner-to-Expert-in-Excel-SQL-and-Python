import pandas as pd
import numpy as np
Covid_Data = {"Country":["Japan","Malatsia","Spain","Singapore","Italy","Morocco","Germany","Egypt","USA","Canada","Brazil"],
              "Continent":["Asia","Asia","Europe","Asia","Europe","Africa","Europe","Africa","America","America","America"],
              "Case": [455,93,430,138,5883,2,795,48,213,57,19],
              "Death": ["Yes","No","Yes","No","Yes","No","No","No","Yes","No","No"],
              "Death_C": [6,0,5,0,234,0,0,0,11,0,0]}
DF_Cov = pd.DataFrame(Covid_Data)
DF_Cov
Country	Continent	Case	Death	Death_C
0	Japan	Asia	455	Yes	6
1	Malatsia	Asia	93	No	0
2	Spain	Europe	430	Yes	5
3	Singapore	Asia	138	No	0
4	Italy	Europe	5883	Yes	234
5	Morocco	Africa	2	No	0
6	Germany	Europe	795	No	0
7	Egypt	Africa	48	No	0
8	USA	America	213	Yes	11
9	Canada	America	57	No	0
10	Brazil	America	19	No	0
DF_Cov_G = DF_Cov.groupby("Continent")
DF_Cov_G
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x000002B2AC8ADD30>
DF_Cov_G.groups
{'Africa': [5, 7], 'America': [8, 9, 10], 'Asia': [0, 1, 3], 'Europe': [2, 4, 6]}
for i, j in DF_Cov_G:
    print(i)
    print(j)
Africa
   Country Continent  Case Death  Death_C
5  Morocco    Africa     2    No        0
7    Egypt    Africa    48    No        0
America
   Country Continent  Case Death  Death_C
8      USA   America   213   Yes       11
9   Canada   America    57    No        0
10  Brazil   America    19    No        0
Asia
     Country Continent  Case Death  Death_C
0      Japan      Asia   455   Yes        6
1   Malatsia      Asia    93    No        0
3  Singapore      Asia   138    No        0
Europe
   Country Continent  Case Death  Death_C
2    Spain    Europe   430   Yes        5
4    Italy    Europe  5883   Yes      234
6  Germany    Europe   795    No        0
DF_Cov_G.get_group("Europe")
Country	Continent	Case	Death	Death_C
2	Spain	Europe	430	Yes	5
4	Italy	Europe	5883	Yes	234
6	Germany	Europe	795	No	0
DF_Cov_G.size()
Continent
Africa     2
America    3
Asia       3
Europe     3
dtype: int64
DF_Cov_M = DF_Cov.groupby(["Continent", "Death"])
DF_Cov_M.size()
Continent  Death
Africa     No       2
America    No       2
           Yes      1
Asia       No       2
           Yes      1
Europe     No       1
           Yes      2
dtype: int64
for i,j in DF_Cov_M:
    print(i)
    print(j)
('Africa', 'No')
   Country Continent  Case Death  Death_C
5  Morocco    Africa     2    No        0
7    Egypt    Africa    48    No        0
('America', 'No')
   Country Continent  Case Death  Death_C
9   Canada   America    57    No        0
10  Brazil   America    19    No        0
('America', 'Yes')
  Country Continent  Case Death  Death_C
8     USA   America   213   Yes       11
('Asia', 'No')
     Country Continent  Case Death  Death_C
1   Malatsia      Asia    93    No        0
3  Singapore      Asia   138    No        0
('Asia', 'Yes')
  Country Continent  Case Death  Death_C
0   Japan      Asia   455   Yes        6
('Europe', 'No')
   Country Continent  Case Death  Death_C
6  Germany    Europe   795    No        0
('Europe', 'Yes')
  Country Continent  Case Death  Death_C
2   Spain    Europe   430   Yes        5
4   Italy    Europe  5883   Yes      234
DF_Cov_M.aggregate(np.sum)
Country	Case	Death_C
Continent	Death			
Africa	No	MoroccoEgypt	50	0
America	No	CanadaBrazil	76	0
Yes	USA	213	11
Asia	No	MalatsiaSingapore	231	0
Yes	Japan	455	6
Europe	No	Germany	795	0
Yes	SpainItaly	6313	239
DF_Cov_M.agg(np.sum)
Country	Case	Death_C
Continent	Death			
Africa	No	MoroccoEgypt	50	0
America	No	CanadaBrazil	76	0
Yes	USA	213	11
Asia	No	MalatsiaSingapore	231	0
Yes	Japan	455	6
Europe	No	Germany	795	0
Yes	SpainItaly	6313	239
DF_Cov_G.agg(np.mean)
