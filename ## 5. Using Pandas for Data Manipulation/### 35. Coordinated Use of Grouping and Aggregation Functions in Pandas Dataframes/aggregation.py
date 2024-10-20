import pandas as pd
import seaborn as sns

df = sns.load_dataset("planets")
df.head()
method	number	orbital_period	mass	distance	year
0	Radial Velocity	1	269.300	7.10	77.40	2006
1	Radial Velocity	1	874.774	2.21	56.95	2008
2	Radial Velocity	1	763.000	2.60	19.84	2011
3	Radial Velocity	1	326.030	19.40	110.62	2007
4	Radial Velocity	1	516.220	10.50	119.47	2009
df["method"].value_counts()
method
Radial Velocity                  553
Transit                          397
Imaging                           38
Microlensing                      23
Eclipse Timing Variations          9
Pulsar Timing                      5
Transit Timing Variations          4
Orbital Brightness Modulation      3
Astrometry                         2
Pulsation Timing Variations        1
Name: count, dtype: int64
df["method"].unique()
array(['Radial Velocity', 'Imaging', 'Eclipse Timing Variations',
       'Transit', 'Astrometry', 'Transit Timing Variations',
       'Orbital Brightness Modulation', 'Microlensing', 'Pulsar Timing',
       'Pulsation Timing Variations'], dtype=object)
df["method"].nunique()
10
df["distance"].value_counts()
distance
780.00    7
6.80      6
39.39     6
303.00    6
613.00    6
         ..
45.01     1
117.37    1
86.88     1
136.80    1
22.04     1
Name: count, Length: 552, dtype: int64
df["distance"].value_counts(dropna = False)
distance
NaN       227
780.00      7
303.00      6
12.83       6
6.80        6
         ... 
125.00      1
455.00      1
255.00      1
170.00      1
180.00      1
Name: count, Length: 553, dtype: int64
df.distance.isnull().sum()
np.int64(227)
df.head()
method	number	orbital_period	mass	distance	year
0	Radial Velocity	1	269.300	7.10	77.40	2006
1	Radial Velocity	1	874.774	2.21	56.95	2008
2	Radial Velocity	1	763.000	2.60	19.84	2011
3	Radial Velocity	1	326.030	19.40	110.62	2007
4	Radial Velocity	1	516.220	10.50	119.47	2009
df.groupby("method")
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x7dd654290450>
df.groupby("method").mean()
number	orbital_period	mass	distance	year
method					
Astrometry	1.000000	631.180000	NaN	17.875000	2011.500000
Eclipse Timing Variations	1.666667	4751.644444	5.125000	315.360000	2010.000000
Imaging	1.315789	118247.737500	NaN	67.715937	2009.131579
Microlensing	1.173913	3153.571429	NaN	4144.000000	2009.782609
Orbital Brightness Modulation	1.666667	0.709307	NaN	1180.000000	2011.666667
Pulsar Timing	2.200000	7343.021201	NaN	1200.000000	1998.400000
Pulsation Timing Variations	1.000000	1170.000000	NaN	NaN	2007.000000
Radial Velocity	1.721519	823.354680	2.630699	51.600208	2007.518987
Transit	1.954660	21.102073	1.470000	599.298080	2011.236776
Transit Timing Variations	2.250000	79.783500	NaN	1104.333333	2012.500000
df.groupby("method")["distance"]
<pandas.core.groupby.generic.SeriesGroupBy object at 0x7dd652b82b10>
df.groupby("method")["distance"].mean()
method
Astrometry                         17.875000
Eclipse Timing Variations         315.360000
Imaging                            67.715937
Microlensing                     4144.000000
Orbital Brightness Modulation    1180.000000
Pulsar Timing                    1200.000000
Pulsation Timing Variations              NaN
Radial Velocity                    51.600208
Transit                           599.298080
Transit Timing Variations        1104.333333
Name: distance, dtype: float64
df.groupby("method")[["distance"]].mean()
distance
method	
Astrometry	17.875000
Eclipse Timing Variations	315.360000
Imaging	67.715937
Microlensing	4144.000000
Orbital Brightness Modulation	1180.000000
Pulsar Timing	1200.000000
Pulsation Timing Variations	NaN
Radial Velocity	51.600208
Transit	599.298080
Transit Timing Variations	1104.333333
df.head()
method	number	orbital_period	mass	distance	year
0	Radial Velocity	1	269.300	7.10	77.40	2006
1	Radial Velocity	1	874.774	2.21	56.95	2008
2	Radial Velocity	1	763.000	2.60	19.84	2011
3	Radial Velocity	1	326.030	19.40	110.62	2007
4	Radial Velocity	1	516.220	10.50	119.47	2009
df.groupby("year")[["number"]].sum()
number
year	
1989	1
1992	6
1994	3
1995	1
1996	15
1997	1
1998	11
1999	24
2000	27
2001	15
2002	46
2003	35
2004	41
2005	64
2006	43
2007	65
2008	120
2009	131
2010	193
2011	354
2012	258
2013	277
2014	117
df[df["year"] == 1992]
method	number	orbital_period	mass	distance	year
941	Pulsar Timing	3	25.2620	NaN	NaN	1992
942	Pulsar Timing	3	66.5419	NaN	NaN	1992
