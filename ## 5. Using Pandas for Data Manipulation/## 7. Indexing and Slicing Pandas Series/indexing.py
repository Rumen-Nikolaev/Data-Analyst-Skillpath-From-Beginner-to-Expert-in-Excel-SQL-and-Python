import pandas as pd
example = pd.Series(["+90", "+49", "+33", "+39", "+46", "+47"], index = ["Turkey", "Germany", "France", "Italy", "Sweden", "Norway"])
example
Turkey     +90
Germany    +49
France     +33
Italy      +39
Sweden     +46
Norway     +47
dtype: object
example["Germany"]
'+49'
example[1]
/tmp/ipykernel_43195/3334167894.py:1: FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`
  example[1]
'+49'
example[1]
/tmp/ipykernel_43195/3334167894.py:1: FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`
  example[1]
'+49'
example["France" : "Sweden"]
France    +33
Italy     +39
Sweden    +46
dtype: object
example[2:5]
France    +33
Italy     +39
Sweden    +46
dtype: object
example[2:5:2]
France    +33
Sweden    +46
dtype: object
example[["Norway", "Turkey"]]
Norway    +47
Turkey    +90
dtype: object
