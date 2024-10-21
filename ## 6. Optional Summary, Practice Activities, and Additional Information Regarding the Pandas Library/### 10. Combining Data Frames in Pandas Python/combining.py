import numpy as np
import pandas as pd
Sales_1 = {"Chocolate":[70,45,65,35],
           "Bread":[63,51,59,46],
           "Biscuits": [150,90,143,87],
           "Potatoes(kg)":[45,67,38,33],
           "Carrots(kg)":[33,44,45,41],
           "Chips":[35,0,28,70],
           "Crackers":[0,13,45,39]}
DF_Month_1 = pd.DataFrame(Sales_1, index = ["Week 1","Week 2","Week 3","Week 4"])
DF_Month_1
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	70	63	150	45	33	35	0
Week 2	45	51	90	67	44	0	13
Week 3	65	59	143	38	45	28	45
Week 4	35	46	87	33	41	70	39
Sales_2 = {"Chocolate":[40,35,60,44],
           "Bread":[23,57,39,71],
           "Biscuits": [50,70,45,56],
           "Potatoes(kg)":[25,61,33,41],
           "Carrots(kg)":[53,47,44,39],
           "Chips":[35,13,28,36],
           "Crackers":[27,13,45,47]}
DF_Month_2 = pd.DataFrame(Sales_2, index = ["Week 1","Week 2","Week 3","Week 4"])
DF_Month_2
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	40	23	50	25	53	35	27
Week 2	35	57	70	61	47	13	13
Week 3	60	39	45	33	44	28	45
Week 4	44	71	56	41	39	36	47
DF_Month_3 = pd.DataFrame(Sales_1, index = ["Week 1","Week 2","Week 3","Week 4"])
DF_Month_3
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	70	63	150	45	33	35	0
Week 2	45	51	90	67	44	0	13
Week 3	65	59	143	38	45	28	45
Week 4	35	46	87	33	41	70	39
All_Sales = pd.concat([DF_Month_1,DF_Month_2,DF_Month_3])
All_Sales
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	70	63	150	45	33	35	0
Week 2	45	51	90	67	44	0	13
Week 3	65	59	143	38	45	28	45
Week 4	35	46	87	33	41	70	39
Week 1	40	23	50	25	53	35	27
Week 2	35	57	70	61	47	13	13
Week 3	60	39	45	33	44	28	45
Week 4	44	71	56	41	39	36	47
Week 1	70	63	150	45	33	35	0
Week 2	45	51	90	67	44	0	13
Week 3	65	59	143	38	45	28	45
Week 4	35	46	87	33	41	70	39
All_sales_keys = pd.concat([DF_Month_1,DF_Month_2,DF_Month_3],keys = ["Month1","Month2","Month3"])
All_sales_keys
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Month1	Week 1	70	63	150	45	33	35	0
Week 2	45	51	90	67	44	0	13
Week 3	65	59	143	38	45	28	45
Week 4	35	46	87	33	41	70	39
Month2	Week 1	40	23	50	25	53	35	27
Week 2	35	57	70	61	47	13	13
Week 3	60	39	45	33	44	28	45
Week 4	44	71	56	41	39	36	47
Month3	Week 1	70	63	150	45	33	35	0
Week 2	45	51	90	67	44	0	13
Week 3	65	59	143	38	45	28	45
Week 4	35	46	87	33	41	70	39
All_sales_keys.loc["Month 2"]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py:3805, in Index.get_loc(self, key)
   3804 try:
-> 3805     return self._engine.get_loc(casted_key)
   3806 except KeyError as err:

File index.pyx:167, in pandas._libs.index.IndexEngine.get_loc()

File index.pyx:196, in pandas._libs.index.IndexEngine.get_loc()

File pandas\\_libs\\hashtable_class_helper.pxi:7081, in pandas._libs.hashtable.PyObjectHashTable.get_item()

File pandas\\_libs\\hashtable_class_helper.pxi:7089, in pandas._libs.hashtable.PyObjectHashTable.get_item()

KeyError: 'Month 2'

The above exception was the direct cause of the following exception:

KeyError                                  Traceback (most recent call last)
Cell In[18], line 1
----> 1 All_sales_keys.loc["Month 2"]

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexing.py:1191, in _LocationIndexer.__getitem__(self, key)
   1189 maybe_callable = com.apply_if_callable(key, self.obj)
   1190 maybe_callable = self._check_deprecated_callable_usage(key, maybe_callable)
-> 1191 return self._getitem_axis(maybe_callable, axis=axis)

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexing.py:1431, in _LocIndexer._getitem_axis(self, key, axis)
   1429 # fall thru to straight lookup
   1430 self._validate_key(key, axis)
-> 1431 return self._get_label(key, axis=axis)

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexing.py:1381, in _LocIndexer._get_label(self, label, axis)
   1379 def _get_label(self, label, axis: AxisInt):
   1380     # GH#5567 this will fail if the label is not present in the axis.
-> 1381     return self.obj.xs(label, axis=axis)

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\generic.py:4293, in NDFrame.xs(self, key, axis, level, drop_level)
   4290     index = self.index
   4292 if isinstance(index, MultiIndex):
-> 4293     loc, new_index = index._get_loc_level(key, level=0)
   4294     if not drop_level:
   4295         if lib.is_integer(loc):
   4296             # Slice index must be an integer or None

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\multi.py:3290, in MultiIndex._get_loc_level(self, key, level)
   3288         return indexer, maybe_mi_droplevels(indexer, ilevels)
   3289 else:
-> 3290     indexer = self._get_level_indexer(key, level=level)
   3291     if (
   3292         isinstance(key, str)
   3293         and self.levels[level]._supports_partial_string_indexing
   3294     ):
   3295         # check to see if we did an exact lookup vs sliced
   3296         check = self.levels[level].get_loc(key)

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\multi.py:3391, in MultiIndex._get_level_indexer(self, key, level, indexer)
   3388         return slice(i, j, step)
   3390 else:
-> 3391     idx = self._get_loc_single_level_index(level_index, key)
   3393     if level > 0 or self._lexsort_depth == 0:
   3394         # Desired level is not sorted
   3395         if isinstance(idx, slice):
   3396             # test_get_loc_partial_timestamp_multiindex

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\multi.py:2980, in MultiIndex._get_loc_single_level_index(self, level_index, key)
   2978     return -1
   2979 else:
-> 2980     return level_index.get_loc(key)

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py:3812, in Index.get_loc(self, key)
   3807     if isinstance(casted_key, slice) or (
   3808         isinstance(casted_key, abc.Iterable)
   3809         and any(isinstance(x, slice) for x in casted_key)
   3810     ):
   3811         raise InvalidIndexError(key)
-> 3812     raise KeyError(key) from err
   3813 except TypeError:
   3814     # If we have a listlike key, _check_indexing_error will raise
   3815     #  InvalidIndexError. Otherwise we fall through and re-raise
   3816     #  the TypeError.
   3817     self._check_indexing_error(key)

KeyError: 'Month 2'
All_sales_keys = pd.concat([DF_Month_1,DF_Month_2,DF_Month_3],keys=["Month 1","Month 2","Month 3"],axis = 0)
All_sales_keys
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Month 1	Week 1	70	63	150	45	33	35	0
Week 2	45	51	90	67	44	0	13
Week 3	65	59	143	38	45	28	45
Week 4	35	46	87	33	41	70	39
Month 2	Week 1	40	23	50	25	53	35	27
Week 2	35	57	70	61	47	13	13
Week 3	60	39	45	33	44	28	45
Week 4	44	71	56	41	39	36	47
Month 3	Week 1	70	63	150	45	33	35	0
Week 2	45	51	90	67	44	0	13
Week 3	65	59	143	38	45	28	45
Week 4	35	46	87	33	41	70	39
All_sales_keys = pd.concat([DF_Month_1,DF_Month_2,DF_Month_3],keys=["Month 1","Month 2","Month 3"],axis = 1)
All_sales_keys
Month 1	Month 2	Month 3
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers	Chocolate	Bread	Biscuits	...	Carrots(kg)	Chips	Crackers	Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	70	63	150	45	33	35	0	40	23	50	...	53	35	27	70	63	150	45	33	35	0
Week 2	45	51	90	67	44	0	13	35	57	70	...	47	13	13	45	51	90	67	44	0	13
Week 3	65	59	143	38	45	28	45	60	39	45	...	44	28	45	65	59	143	38	45	28	45
Week 4	35	46	87	33	41	70	39	44	71	56	...	39	36	47	35	46	87	33	41	70	39
4 rows × 21 columns

DF_Month_2 = pd.DataFrame(Sales_2, index = ["Week 4","Week 5","Week 6","Week 7"])
All_sales_keys = pd.concat([DF_Month_1,DF_Month_2,DF_Month_3],keys = ["Month 1","Month 2","Month 3"], axis = 0)
All_sales_keys
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Month 1	Week 1	70	63	150	45	33	35	0
Week 2	45	51	90	67	44	0	13
Week 3	65	59	143	38	45	28	45
Week 4	35	46	87	33	41	70	39
Month 2	Week 4	40	23	50	25	53	35	27
Week 5	35	57	70	61	47	13	13
Week 6	60	39	45	33	44	28	45
Week 7	44	71	56	41	39	36	47
Month 3	Week 1	70	63	150	45	33	35	0
Week 2	45	51	90	67	44	0	13
Week 3	65	59	143	38	45	28	45
Week 4	35	46	87	33	41	70	39
All_sales_keys = pd.concat([DF_Month_1,DF_Month_2,DF_Month_3],keys = ["Month 1","Month 2","Month 3"], axis = 1)
All_sales_keys
Month 1	Month 2	Month 3
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers	Chocolate	Bread	Biscuits	...	Carrots(kg)	Chips	Crackers	Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	70.0	63.0	150.0	45.0	33.0	35.0	0.0	NaN	NaN	NaN	...	NaN	NaN	NaN	70.0	63.0	150.0	45.0	33.0	35.0	0.0
Week 2	45.0	51.0	90.0	67.0	44.0	0.0	13.0	NaN	NaN	NaN	...	NaN	NaN	NaN	45.0	51.0	90.0	67.0	44.0	0.0	13.0
Week 3	65.0	59.0	143.0	38.0	45.0	28.0	45.0	NaN	NaN	NaN	...	NaN	NaN	NaN	65.0	59.0	143.0	38.0	45.0	28.0	45.0
Week 4	35.0	46.0	87.0	33.0	41.0	70.0	39.0	40.0	23.0	50.0	...	53.0	35.0	27.0	35.0	46.0	87.0	33.0	41.0	70.0	39.0
Week 5	NaN	NaN	NaN	NaN	NaN	NaN	NaN	35.0	57.0	70.0	...	47.0	13.0	13.0	NaN	NaN	NaN	NaN	NaN	NaN	NaN
Week 6	NaN	NaN	NaN	NaN	NaN	NaN	NaN	60.0	39.0	45.0	...	44.0	28.0	45.0	NaN	NaN	NaN	NaN	NaN	NaN	NaN
Week 7	NaN	NaN	NaN	NaN	NaN	NaN	NaN	44.0	71.0	56.0	...	39.0	36.0	47.0	NaN	NaN	NaN	NaN	NaN	NaN	NaN
7 rows × 21 columns

Sales_2 = {"Chocolate":[40,35,60,44],
           "Bread":[23,57,39,71],
           "Biscuits": [50,70,45,56],
           "Potatoes(kg)":[25,61,33,41],
           "Carrots(kg)":[53,47,44,39],
           "Chips":[35,13,28,36],
           "Crackers":[27,13,45,47]}
DF_Month_2 = pd.DataFrame(Sales_2, index = ["Week 1","Week 2","Week 3","Week 4"])
All_sales_keys = pd.concat([DF_Month_1,DF_Month_2,DF_Month_3],keys=["Month 1","Month 2","Month 3"])
All_sales_keys
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Month 1	Week 1	70	63	150	45	33	35	0
Week 2	45	51	90	67	44	0	13
Week 3	65	59	143	38	45	28	45
Week 4	35	46	87	33	41	70	39
Month 2	Week 1	40	23	50	25	53	35	27
Week 2	35	57	70	61	47	13	13
Week 3	60	39	45	33	44	28	45
Week 4	44	71	56	41	39	36	47
Month 3	Week 1	70	63	150	45	33	35	0
Week 2	45	51	90	67	44	0	13
Week 3	65	59	143	38	45	28	45
Week 4	35	46	87	33	41	70	39
All_sales_keys = pd.concat([DF_Month_1,DF_Month_2,DF_Month_3],keys = ["Month 1","Month 2","Month 3"], axis = 1)
All_sales_keys
Month 1	Month 2	Month 3
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers	Chocolate	Bread	Biscuits	...	Carrots(kg)	Chips	Crackers	Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	70	63	150	45	33	35	0	40	23	50	...	53	35	27	70	63	150	45	33	35	0
Week 2	45	51	90	67	44	0	13	35	57	70	...	47	13	13	45	51	90	67	44	0	13
Week 3	65	59	143	38	45	28	45	60	39	45	...	44	28	45	65	59	143	38	45	28	45
Week 4	35	46	87	33	41	70	39	44	71	56	...	39	36	47	35	46	87	33	41	70	39
4 rows × 21 columns

W_A_DF = DF_Month_1.append([DF_Month_2,DF_Month_3])
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
~\AppData\Local\Temp\ipykernel_18228\640564367.py in ?()
----> 1 W_A_DF = DF_Month_1.append([DF_Month_2,DF_Month_3])

~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\generic.py in ?(self, name)
   6295             and name not in self._accessors
   6296             and self._info_axis._can_hold_identifiers_and_holds_name(name)
   6297         ):
   6298             return self[name]
-> 6299         return object.__getattribute__(self, name)

AttributeError: 'DataFrame' object has no attribute 'append'
W_A_DF
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[36], line 1
----> 1 W_A_DF

NameError: name 'W_A_DF' is not defined
 
