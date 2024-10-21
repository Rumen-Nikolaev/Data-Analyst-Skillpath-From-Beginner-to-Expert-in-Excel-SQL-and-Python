import numpy as np
import pandas as pd
Array_1 = np.array([[10,20,np.nan,12],[5,np.nan,np.nan,14],[21,np.nan,10,11],[17,13,10,np.nan]])
Data_Frame_1 = pd.DataFrame(Array_1,
                            index = ["Index1","Index2","Index3","Index3"],
                            columns = ["Column1","Column2","Column3","Column4"])
Data_Frame_1
Column1	Column2	Column3	Column4
Index1	10.0	20.0	NaN	12.0
Index2	5.0	NaN	NaN	14.0
Index3	21.0	NaN	10.0	11.0
Index3	17.0	13.0	10.0	NaN
Data_Frame_1.isna()
Column1	Column2	Column3	Column4
Index1	False	False	True	False
Index2	False	True	True	False
Index3	False	True	False	False
Index3	False	False	False	True
Data_Frame_1["Column2"].isna()
Index1    False
Index2     True
Index3     True
Index3    False
Name: Column2, dtype: bool
Data_Frame_1.notna()
Column1	Column2	Column3	Column4
Index1	True	True	False	True
Index2	True	False	False	True
Index3	True	False	True	True
Index3	True	True	True	False
Data_Frame_1
Column1	Column2	Column3	Column4
Index1	10.0	20.0	NaN	12.0
Index2	5.0	NaN	NaN	14.0
Index3	21.0	NaN	10.0	11.0
Index3	17.0	13.0	10.0	NaN
Data_Frame_1["Column2"].notna()
Index1     True
Index2    False
Index3    False
Index3     True
Name: Column2, dtype: bool
Data_Frame_1.dropna(axis=0)
Column1	Column2	Column3	Column4
Data_Frame_1.dropna(axis=1)
Column1
Index1	10.0
Index2	5.0
Index3	21.0
Index3	17.0
Data_Frame_1
Column1	Column2	Column3	Column4
Index1	10.0	20.0	NaN	12.0
Index2	5.0	NaN	NaN	14.0
Index3	21.0	NaN	10.0	11.0
Index3	17.0	13.0	10.0	NaN
Data_Frame_1.dropna(thresh=3)
Column1	Column2	Column3	Column4
Index1	10.0	20.0	NaN	12.0
Index3	21.0	NaN	10.0	11.0
Index3	17.0	13.0	10.0	NaN
Data_Frame_1
Column1	Column2	Column3	Column4
Index1	10.0	20.0	NaN	12.0
Index2	5.0	NaN	NaN	14.0
Index3	21.0	NaN	10.0	11.0
Index3	17.0	13.0	10.0	NaN
Data_Frame_1["Column2"].sum()
np.float64(33.0)
Data_Frame_1["Column2"].mean()
np.float64(16.5)
Data_Frame_1.sum()
Column1    53.0
Column2    33.0
Column3    20.0
Column4    37.0
dtype: float64
Data_Frame_1.mean()
Column1    13.250000
Column2    16.500000
Column3    10.000000
Column4    12.333333
dtype: float64
Data_Frame_1.sum().sum()
np.float64(143.0)
Data_Frame_1.mean().mean()
np.float64(13.020833333333334)
 
