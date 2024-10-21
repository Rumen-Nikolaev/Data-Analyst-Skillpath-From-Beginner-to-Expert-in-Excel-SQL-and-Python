import numpy as np
import pandas as pd
Array_1 = np.array([[10,20,np.nan,12],[5,np.nan,np.nan,14],[21,np.nan,10,11],[17,13,10,np.nan]])
Data_Frame_1 = pd.DataFrame(Array_1, 
                            index = ["Index1","Index2","Index3","Index4"],
                            columns = ["Column1","Column2","Column3","Column4"])
Data_Frame_1
Column1	Column2	Column3	Column4
Index1	10.0	20.0	NaN	12.0
Index2	5.0	NaN	NaN	14.0
Index3	21.0	NaN	10.0	11.0
Index4	17.0	13.0	10.0	NaN
Data_Frame_1.fillna(0)
Column1	Column2	Column3	Column4
Index1	10.0	20.0	0.0	12.0
Index2	5.0	0.0	0.0	14.0
Index3	21.0	0.0	10.0	11.0
Index4	17.0	13.0	10.0	0.0
Data_Frame_2 = Data_Frame_1.fillna(0)
Data_Frame_2
Column1	Column2	Column3	Column4
Index1	10.0	20.0	0.0	12.0
Index2	5.0	0.0	0.0	14.0
Index3	21.0	0.0	10.0	11.0
Index4	17.0	13.0	10.0	0.0
Data_Frame_1.fillna(method = "bfill")
C:\Users\shocw\AppData\Local\Temp\ipykernel_19692\2922647.py:1: FutureWarning: DataFrame.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.
  Data_Frame_1.fillna(method = "bfill")
Column1	Column2	Column3	Column4
Index1	10.0	20.0	10.0	12.0
Index2	5.0	13.0	10.0	14.0
Index3	21.0	13.0	10.0	11.0
Index4	17.0	13.0	10.0	NaN
Data_Frame_1.fillna( method = "ffill")
C:\Users\shocw\AppData\Local\Temp\ipykernel_19692\3817669269.py:1: FutureWarning: DataFrame.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.
  Data_Frame_1.fillna( method = "ffill")
Column1	Column2	Column3	Column4
Index1	10.0	20.0	NaN	12.0
Index2	5.0	20.0	NaN	14.0
Index3	21.0	20.0	10.0	11.0
Index4	17.0	13.0	10.0	11.0
Data_Frame_1
Column1	Column2	Column3	Column4
Index1	10.0	20.0	NaN	12.0
Index2	5.0	NaN	NaN	14.0
Index3	21.0	NaN	10.0	11.0
Index4	17.0	13.0	10.0	NaN
Data_Frame_1.fillna(value = 99)
Column1	Column2	Column3	Column4
Index1	10.0	20.0	99.0	12.0
Index2	5.0	99.0	99.0	14.0
Index3	21.0	99.0	10.0	11.0
Index4	17.0	13.0	10.0	99.0
Values = {"Column1": 22, "Column2": 33, "Column3": 44, "Column4": 55}
Data_Frame_1.fillna(value=Values)
Column1	Column2	Column3	Column4
Index1	10.0	20.0	44.0	12.0
Index2	5.0	33.0	44.0	14.0
Index3	21.0	33.0	10.0	11.0
Index4	17.0	13.0	10.0	55.0
Data_Frame_1
Column1	Column2	Column3	Column4
Index1	10.0	20.0	NaN	12.0
Index2	5.0	NaN	NaN	14.0
Index3	21.0	NaN	10.0	11.0
Index4	17.0	13.0	10.0	NaN
Data_Frame_1.fillna(50,limit = 1)
Column1	Column2	Column3	Column4
Index1	10.0	20.0	50.0	12.0
Index2	5.0	50.0	NaN	14.0
Index3	21.0	NaN	10.0	11.0
Index4	17.0	13.0	10.0	50.0
Data_Frame_1
Column1	Column2	Column3	Column4
Index1	10.0	20.0	NaN	12.0
Index2	5.0	NaN	NaN	14.0
Index3	21.0	NaN	10.0	11.0
Index4	17.0	13.0	10.0	NaN
Data_Frame_1.replace(to_replace=10.0, value = "Ten")
Column1	Column2	Column3	Column4
Index1	Ten	20.0	NaN	12.0
Index2	5.0	NaN	NaN	14.0
Index3	21.0	NaN	Ten	11.0
Index4	17.0	13.0	Ten	NaN
Data_Frame_3 = pd.DataFrame({"UK":["London","Plymouth","Doublin","Portsmouth"],
                             "USA": ["Boston","Pitssburgh","Houston","Fort Worth"],
                             "FR": ["Avignon","Le Mans", "Dijon", "Paris"]})
Data_Frame_3
UK	USA	FR
0	London	Boston	Avignon
1	Plymouth	Pitssburgh	Le Mans
2	Doublin	Houston	Dijon
3	Portsmouth	Fort Worth	Paris
Data_Frame_3.replace(to_replace=r"^L", value= "45", regex = True)
UK	USA	FR
0	45ondon	Boston	Avignon
1	Plymouth	Pitssburgh	45e Mans
2	Doublin	Houston	Dijon
3	Portsmouth	Fort Worth	Paris
Data_Frame_3.replace(to_replace=r"L.*", value = "45",regex = "True")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
~\AppData\Local\Temp\ipykernel_19692\4222597366.py in ?()
----> 1 Data_Frame_3.replace(to_replace=r"L.*", value = "45",regex = "True")

~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\generic.py in ?(self, to_replace, value, inplace, limit, regex, method)
   7972                         stacklevel=2,
   7973                     )
   7974 
   7975         if not is_bool(regex) and to_replace is not None:
-> 7976             raise ValueError("'to_replace' must be 'None' if 'regex' is not a bool")
   7977 
   7978         if value is lib.no_default or method is not lib.no_default:
   7979             # GH#36984 if the user explicitly passes value=None we want to

ValueError: 'to_replace' must be 'None' if 'regex' is not a bool
Data_Frame_1
Column1	Column2	Column3	Column4
Index1	10.0	20.0	NaN	12.0
Index2	5.0	NaN	NaN	14.0
Index3	21.0	NaN	10.0	11.0
Index4	17.0	13.0	10.0	NaN
Data_Frame_1.interpolate(method = "linear", limit_direction="forward")
Column1	Column2	Column3	Column4
Index1	10.0	20.000000	NaN	12.0
Index2	5.0	17.666667	NaN	14.0
Index3	21.0	15.333333	10.0	11.0
Index4	17.0	13.000000	10.0	11.0
Data_Frame_1.interpolate(method = "linear", limit_direction="backward")
Column1	Column2	Column3	Column4
Index1	10.0	20.000000	10.0	12.0
Index2	5.0	17.666667	10.0	14.0
Index3	21.0	15.333333	10.0	11.0
Index4	17.0	13.000000	10.0	NaN
 
