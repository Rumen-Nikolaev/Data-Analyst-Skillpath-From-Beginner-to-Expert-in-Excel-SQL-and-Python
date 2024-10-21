import numpy as np
import pandas as pd
P_Dict_Sales = {"Chocolate": [70,45,65],"Biscuits":[150,90,143],"Potatoes(kg)":[45,67,38],"Carrots(kg)":[33,44,45],
                "Chips":[35,0,28],"Crackers":[0,13,45]}
P_DFrames = pd.DataFrame(P_Dict_Sales)
P_DFrames
Chocolate	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
0	70	150	45	33	35	0
1	45	90	67	44	0	13
2	65	143	38	45	28	45
P_DFrames = pd.DataFrame(P_Dict_Sales, index = ["Week 1", "Week 2", "Week 3"])
P_DFrames
Chocolate	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	70	150	45	33	35	0
Week 2	45	90	67	44	0	13
Week 3	65	143	38	45	28	45
P_DFrames["Biscuits"]
Week 1    150
Week 2     90
Week 3    143
Name: Biscuits, dtype: int64
P_DFrames.Crackers
Week 1     0
Week 2    13
Week 3    45
Name: Crackers, dtype: int64
P_DFrames.loc["Week 1"]
Chocolate        70
Biscuits        150
Potatoes(kg)     45
Carrots(kg)      33
Chips            35
Crackers          0
Name: Week 1, dtype: int64
P_DFrames.iloc[1]
Chocolate       45
Biscuits        90
Potatoes(kg)    67
Carrots(kg)     44
Chips            0
Crackers        13
Name: Week 2, dtype: int64
P_DFrames
Chocolate	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	70	150	45	33	35	0
Week 2	45	90	67	44	0	13
Week 3	65	143	38	45	28	45
P_DFrames.loc["Week 1":"Week 2",["Chocolate","Bread","Carrots(kg)"]]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In[13], line 1
----> 1 P_DFrames.loc["Week 1":"Week 2",["Chocolate","Bread","Carrots(kg)"]]

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexing.py:1184, in _LocationIndexer.__getitem__(self, key)
   1182     if self._is_scalar_access(key):
   1183         return self.obj._get_value(*key, takeable=self._takeable)
-> 1184     return self._getitem_tuple(key)
   1185 else:
   1186     # we by definition only have the 0th axis
   1187     axis = self.axis or 0

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexing.py:1377, in _LocIndexer._getitem_tuple(self, tup)
   1374 if self._multi_take_opportunity(tup):
   1375     return self._multi_take(tup)
-> 1377 return self._getitem_tuple_same_dim(tup)

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexing.py:1020, in _LocationIndexer._getitem_tuple_same_dim(self, tup)
   1017 if com.is_null_slice(key):
   1018     continue
-> 1020 retval = getattr(retval, self.name)._getitem_axis(key, axis=i)
   1021 # We should never have retval.ndim < self.ndim, as that should
   1022 #  be handled by the _getitem_lowerdim call above.
   1023 assert retval.ndim == self.ndim

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexing.py:1420, in _LocIndexer._getitem_axis(self, key, axis)
   1417     if hasattr(key, "ndim") and key.ndim > 1:
   1418         raise ValueError("Cannot index with multidimensional key")
-> 1420     return self._getitem_iterable(key, axis=axis)
   1422 # nested tuple slicing
   1423 if is_nested_tuple(key, labels):

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexing.py:1360, in _LocIndexer._getitem_iterable(self, key, axis)
   1357 self._validate_key(key, axis)
   1359 # A collection of keys
-> 1360 keyarr, indexer = self._get_listlike_indexer(key, axis)
   1361 return self.obj._reindex_with_indexers(
   1362     {axis: [keyarr, indexer]}, copy=True, allow_dups=True
   1363 )

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexing.py:1558, in _LocIndexer._get_listlike_indexer(self, key, axis)
   1555 ax = self.obj._get_axis(axis)
   1556 axis_name = self.obj._get_axis_name(axis)
-> 1558 keyarr, indexer = ax._get_indexer_strict(key, axis_name)
   1560 return keyarr, indexer

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py:6200, in Index._get_indexer_strict(self, key, axis_name)
   6197 else:
   6198     keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)
-> 6200 self._raise_if_missing(keyarr, indexer, axis_name)
   6202 keyarr = self.take(indexer)
   6203 if isinstance(key, Index):
   6204     # GH 42790 - Preserve name from an Index

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py:6252, in Index._raise_if_missing(self, key, indexer, axis_name)
   6249     raise KeyError(f"None of [{key}] are in the [{axis_name}]")
   6251 not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
-> 6252 raise KeyError(f"{not_found} not in index")

KeyError: "['Bread'] not in index"
P_DFrames[P_DFrames >= 50]
Chocolate	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	70.0	150	NaN	NaN	NaN	NaN
Week 2	NaN	90	67.0	NaN	NaN	NaN
Week 3	65.0	143	NaN	NaN	NaN	NaN
P_DFrames[(P_DFrames>=0)&(P_DFrames<50)]
Chocolate	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	NaN	NaN	45.0	33	35	0
Week 2	45.0	NaN	NaN	44	0	13
Week 3	NaN	NaN	38.0	45	28	45
P_DFrames[(P_DFrames>=100)|(P_DFrames<50)]
Chocolate	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	NaN	150.0	45.0	33	35	0
Week 2	45.0	NaN	NaN	44	0	13
Week 3	NaN	143.0	38.0	45	28	45
P_DFrames.at["Week 1","Chocolate"]
np.int64(70)
P_DFrames.iat[0,3]
np.int64(33)
P_DFrames
Chocolate	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	70	150	45	33	35	0
Week 2	45	90	67	44	0	13
Week 3	65	143	38	45	28	45
P_DFrames.at["Week 1","Chocolate"] = 66
P_DFrames
Chocolate	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	66	150	45	33	35	0
Week 2	45	90	67	44	0	13
Week 3	65	143	38	45	28	45
P_DFrames.iat[0,3] = 75
P_DFrames
Chocolate	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	66	150	45	75	35	0
Week 2	45	90	67	44	0	13
Week 3	65	143	38	45	28	45
P_DFrames.describe()
Chocolate	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
count	3.000000	3.000000	3.000000	3.000000	3.000000	3.000000
mean	58.666667	127.666667	50.000000	54.666667	21.000000	19.333333
std	11.846237	32.807519	15.132746	17.616280	18.520259	23.158872
min	45.000000	90.000000	38.000000	44.000000	0.000000	0.000000
25%	55.000000	116.500000	41.500000	44.500000	14.000000	6.500000
50%	65.000000	143.000000	45.000000	45.000000	28.000000	13.000000
75%	65.500000	146.500000	56.000000	60.000000	31.500000	29.000000
max	66.000000	150.000000	67.000000	75.000000	35.000000	45.000000
pd.set_option("precision",2)
---------------------------------------------------------------------------
OptionError                               Traceback (most recent call last)
Cell In[25], line 1
----> 1 pd.set_option("precision",2)

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\_config\config.py:274, in CallableDynamicDoc.__call__(self, *args, **kwds)
    273 def __call__(self, *args, **kwds) -> T:
--> 274     return self.__func__(*args, **kwds)

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\_config\config.py:167, in _set_option(*args, **kwargs)
    164     raise TypeError(f'_set_option() got an unexpected keyword argument "{kwarg}"')
    166 for k, v in zip(args[::2], args[1::2]):
--> 167     key = _get_single_key(k, silent)
    169     o = _get_registered_option(key)
    170     if o and o.validator:

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\_config\config.py:134, in _get_single_key(pat, silent)
    132     raise OptionError(f"No such keys(s): {repr(pat)}")
    133 if len(keys) > 1:
--> 134     raise OptionError("Pattern matched multiple keys")
    135 key = keys[0]
    137 if not silent:

OptionError: Pattern matched multiple keys
P_DFrames.describe()
Chocolate	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
count	3.000000	3.000000	3.000000	3.000000	3.000000	3.000000
mean	58.666667	127.666667	50.000000	54.666667	21.000000	19.333333
std	11.846237	32.807519	15.132746	17.616280	18.520259	23.158872
min	45.000000	90.000000	38.000000	44.000000	0.000000	0.000000
25%	55.000000	116.500000	41.500000	44.500000	14.000000	6.500000
50%	65.000000	143.000000	45.000000	45.000000	28.000000	13.000000
75%	65.500000	146.500000	56.000000	60.000000	31.500000	29.000000
max	66.000000	150.000000	67.000000	75.000000	35.000000	45.000000
P_DFrames.mean()
Chocolate        58.666667
Biscuits        127.666667
Potatoes(kg)     50.000000
Carrots(kg)      54.666667
Chips            21.000000
Crackers         19.333333
dtype: float64
P_DFrames.T
Week 1	Week 2	Week 3
Chocolate	66	45	65
Biscuits	150	90	143
Potatoes(kg)	45	67	38
Carrots(kg)	75	44	45
Chips	35	0	28
Crackers	0	13	45
P_DFrames.T.describe()
Week 1	Week 2	Week 3
count	6.000000	6.000000	6.000000
mean	61.833333	43.166667	60.666667
std	50.578322	33.283129	42.117297
min	0.000000	0.000000	28.000000
25%	37.500000	20.750000	39.750000
50%	55.500000	44.500000	45.000000
75%	72.750000	61.500000	60.000000
max	150.000000	90.000000	143.000000
P_DFrames.sort_index(ascending=False)
Chocolate	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 3	65	143	38	45	28	45
Week 2	45	90	67	44	0	13
Week 1	66	150	45	75	35	0
P_DFrames.sort_index(axis = 1)
Biscuits	Carrots(kg)	Chips	Chocolate	Crackers	Potatoes(kg)
Week 1	150	75	35	66	0	45
Week 2	90	44	0	45	13	67
Week 3	143	45	28	65	45	38
P_DFrames.sort_index(axis = 0)
Chocolate	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	66	150	45	75	35	0
Week 2	45	90	67	44	0	13
Week 3	65	143	38	45	28	45
 
