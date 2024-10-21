import numpy as np
import pandas as pd
P_Dict_Sales = {"Chocolate": [70,45,65],"Bread":[63,51,59],"Biscuits":[150,90,45],"Potatoes(kg)":[45,67,38],
                "Carrots(kg)":[33,44,45],"Chips":[35,0,28],"Crackers":[0,13,45]}
P_DFrames = pd.DataFrame(P_Dict_Sales)
P_DFrames = pd.DataFrame(P_Dict_Sales, index = ["Week 1","Week 2","Week 3"])
P_DFrames
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	70	63	150	45	33	35	0
Week 2	45	51	90	67	44	0	13
Week 3	65	59	45	38	45	28	45
P_DFrames["Onions(kg)"] = [35,49,27]
P_DFrames
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers	Onions(kg)
Week 1	70	63	150	45	33	35	0	35
Week 2	45	51	90	67	44	0	13	49
Week 3	65	59	45	38	45	28	45	27
New_Row = {"Chocolate": 77, "Bread": 69, "Biscuits": 105, "Potatoes(kg)": 33, "Carrots(kg)": 57,
           "Chips": 44, "Crackers": 30, "Onions(kg)": 30}
P_DFrames = P_DFrames.append(New_Row, ignore_index = True)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
~\AppData\Local\Temp\ipykernel_10456\950151997.py in ?()
----> 1 P_DFrames = P_DFrames.append(New_Row, ignore_index = True)

~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\generic.py in ?(self, name)
   6295             and name not in self._accessors
   6296             and self._info_axis._can_hold_identifiers_and_holds_name(name)
   6297         ):
   6298             return self[name]
-> 6299         return object.__getattribute__(self, name)

AttributeError: 'DataFrame' object has no attribute 'append'
P_DFrames
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers	Onions(kg)
Week 1	70	63	150	45	33	35	0	35
Week 2	45	51	90	67	44	0	13	49
Week 3	65	59	45	38	45	28	45	27
New_Row_2 = {"Chocolate": 77, "Bread": 69, "Biscuits": 105, "Potatoes(kg)": 33, "Carrots(kg)": 57,
           "Chips": 44, "Crackers": 30, "Onions(kg)": 30}
P_DFrames = P_DFrames.append(New_Row_2, ignore_index = False)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
~\AppData\Local\Temp\ipykernel_10456\607768106.py in ?()
----> 1 P_DFrames = P_DFrames.append(New_Row_2, ignore_index = False)

~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\generic.py in ?(self, name)
   6295             and name not in self._accessors
   6296             and self._info_axis._can_hold_identifiers_and_holds_name(name)
   6297         ):
   6298             return self[name]
-> 6299         return object.__getattribute__(self, name)

AttributeError: 'DataFrame' object has no attribute 'append'
P_DFrames = pd.DataFrame(P_Dict_Sales, index = ["Week 1", "Week 2", "Week 3"])
P_DFrames
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	70	63	150	45	33	35	0
Week 2	45	51	90	67	44	0	13
Week 3	65	59	45	38	45	28	45
N_R = pd.Series(data = {"Chocolate": 55, "Bread": 43, "Biscuits": 77, "Potatoes(kg)": 54, "Carrots(kg)": 55,
           "Chips": 23, "Crackers": 33, "Onions(kg)": 39}, name = "Week 4")
P_DFrames = P_DFrames.append(N_R, ignore_index = False)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
~\AppData\Local\Temp\ipykernel_10456\362533181.py in ?()
----> 1 P_DFrames = P_DFrames.append(N_R, ignore_index = False)

~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\generic.py in ?(self, name)
   6295             and name not in self._accessors
   6296             and self._info_axis._can_hold_identifiers_and_holds_name(name)
   6297         ):
   6298             return self[name]
-> 6299         return object.__getattribute__(self, name)

AttributeError: 'DataFrame' object has no attribute 'append'
P_DFrames
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	70	63	150	45	33	35	0
Week 2	45	51	90	67	44	0	13
Week 3	65	59	45	38	45	28	45
del P_DFrames["Chips"]
P_DFrames
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Crackers
Week 1	70	63	150	45	33	0
Week 2	45	51	90	67	44	13
Week 3	65	59	45	38	45	45
P_DFrames.pop("Potatoes(kg)")
Week 1    45
Week 2    67
Week 3    38
Name: Potatoes(kg), dtype: int64
P_DFrames
Chocolate	Bread	Biscuits	Carrots(kg)	Crackers
Week 1	70	63	150	33	0
Week 2	45	51	90	44	13
Week 3	65	59	45	45	45
P_DFrames = P_DFrames.drop(["Crackers"], axis = 1)
P_DFrames
Chocolate	Bread	Biscuits	Carrots(kg)
Week 1	70	63	150	33
Week 2	45	51	90	44
Week 3	65	59	45	45
P_DFrames = P_DFrames.drop(["Week 4"], axis = 0)
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In[27], line 1
----> 1 P_DFrames = P_DFrames.drop(["Week 4"], axis = 0)

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py:5581, in DataFrame.drop(self, labels, axis, index, columns, level, inplace, errors)
   5433 def drop(
   5434     self,
   5435     labels: IndexLabel | None = None,
   (...)
   5442     errors: IgnoreRaise = "raise",
   5443 ) -> DataFrame | None:
   5444     """
   5445     Drop specified labels from rows or columns.
   5446 
   (...)
   5579             weight  1.0     0.8
   5580     """
-> 5581     return super().drop(
   5582         labels=labels,
   5583         axis=axis,
   5584         index=index,
   5585         columns=columns,
   5586         level=level,
   5587         inplace=inplace,
   5588         errors=errors,
   5589     )

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\generic.py:4788, in NDFrame.drop(self, labels, axis, index, columns, level, inplace, errors)
   4786 for axis, labels in axes.items():
   4787     if labels is not None:
-> 4788         obj = obj._drop_axis(labels, axis, level=level, errors=errors)
   4790 if inplace:
   4791     self._update_inplace(obj)

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\generic.py:4830, in NDFrame._drop_axis(self, labels, axis, level, errors, only_slice)
   4828         new_axis = axis.drop(labels, level=level, errors=errors)
   4829     else:
-> 4830         new_axis = axis.drop(labels, errors=errors)
   4831     indexer = axis.get_indexer(new_axis)
   4833 # Case for non-unique axis
   4834 else:

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py:7070, in Index.drop(self, labels, errors)
   7068 if mask.any():
   7069     if errors != "ignore":
-> 7070         raise KeyError(f"{labels[mask].tolist()} not found in axis")
   7071     indexer = indexer[~mask]
   7072 return self.delete(indexer)

KeyError: "['Week 4'] not found in axis"
P_DFrames
Chocolate	Bread	Biscuits	Carrots(kg)
Week 1	70	63	150	33
Week 2	45	51	90	44
Week 3	65	59	45	45
 
