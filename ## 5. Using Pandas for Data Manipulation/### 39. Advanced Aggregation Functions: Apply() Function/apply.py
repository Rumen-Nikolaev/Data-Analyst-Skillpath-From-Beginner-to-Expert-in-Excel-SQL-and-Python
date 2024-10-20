import pandas as pd
import numpy as np
df = pd.DataFrame({'groups': ['X', 'Y', 'Z', 'X', 'Y', 'Z'],
                   'val1': [2, 15, 25, 14, 3, 91],
                   'val2': [92,245,325,254,103,961]})
df
groups	val1	val2
0	X	2	92
1	Y	15	245
2	Z	25	325
3	X	14	254
4	Y	3	103
5	Z	91	961
df.apply(np.sum)
groups    XYZXYZ
val1         150
val2        1980
dtype: object
df.apply(np.mean)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[5], line 1
----> 1 df.apply(np.mean)

File ~/myenv/lib/python3.11/site-packages/pandas/core/frame.py:10374, in DataFrame.apply(self, func, axis, raw, result_type, args, by_row, engine, engine_kwargs, **kwargs)
  10360 from pandas.core.apply import frame_apply
  10362 op = frame_apply(
  10363     self,
  10364     func=func,
   (...)
  10372     kwargs=kwargs,
  10373 )
> 10374 return op.apply().__finalize__(self, method="apply")

File ~/myenv/lib/python3.11/site-packages/pandas/core/apply.py:916, in FrameApply.apply(self)
    913 elif self.raw:
    914     return self.apply_raw(engine=self.engine, engine_kwargs=self.engine_kwargs)
--> 916 return self.apply_standard()

File ~/myenv/lib/python3.11/site-packages/pandas/core/apply.py:1063, in FrameApply.apply_standard(self)
   1061 def apply_standard(self):
   1062     if self.engine == "python":
-> 1063         results, res_index = self.apply_series_generator()
   1064     else:
   1065         results, res_index = self.apply_series_numba()

File ~/myenv/lib/python3.11/site-packages/pandas/core/apply.py:1081, in FrameApply.apply_series_generator(self)
   1078 with option_context("mode.chained_assignment", None):
   1079     for i, v in enumerate(series_gen):
   1080         # ignore SettingWithCopy here in case the user mutates
-> 1081         results[i] = self.func(v, *self.args, **self.kwargs)
   1082         if isinstance(results[i], ABCSeries):
   1083             # If we have a view on v, we need to make a copy because
   1084             #  series_generator will swap out the underlying data
   1085             results[i] = results[i].copy(deep=False)

File ~/myenv/lib/python3.11/site-packages/numpy/_core/fromnumeric.py:3902, in mean(a, axis, dtype, out, keepdims, where)
   3900         pass
   3901     else:
-> 3902         return mean(axis=axis, dtype=dtype, out=out, **kwargs)
   3904 return _methods._mean(a, axis=axis, dtype=dtype,
   3905                       out=out, **kwargs)

File ~/myenv/lib/python3.11/site-packages/pandas/core/series.py:6549, in Series.mean(self, axis, skipna, numeric_only, **kwargs)
   6541 @doc(make_doc("mean", ndim=1))
   6542 def mean(
   6543     self,
   (...)
   6547     **kwargs,
   6548 ):
-> 6549     return NDFrame.mean(self, axis, skipna, numeric_only, **kwargs)

File ~/myenv/lib/python3.11/site-packages/pandas/core/generic.py:12420, in NDFrame.mean(self, axis, skipna, numeric_only, **kwargs)
  12413 def mean(
  12414     self,
  12415     axis: Axis | None = 0,
   (...)
  12418     **kwargs,
  12419 ) -> Series | float:
> 12420     return self._stat_function(
  12421         "mean", nanops.nanmean, axis, skipna, numeric_only, **kwargs
  12422     )

File ~/myenv/lib/python3.11/site-packages/pandas/core/generic.py:12377, in NDFrame._stat_function(self, name, func, axis, skipna, numeric_only, **kwargs)
  12373 nv.validate_func(name, (), kwargs)
  12375 validate_bool_kwarg(skipna, "skipna", none_allowed=False)
> 12377 return self._reduce(
  12378     func, name=name, axis=axis, skipna=skipna, numeric_only=numeric_only
  12379 )

File ~/myenv/lib/python3.11/site-packages/pandas/core/series.py:6457, in Series._reduce(self, op, name, axis, skipna, numeric_only, filter_type, **kwds)
   6452     # GH#47500 - change to TypeError to match other methods
   6453     raise TypeError(
   6454         f"Series.{name} does not allow {kwd_name}={numeric_only} "
   6455         "with non-numeric dtypes."
   6456     )
-> 6457 return op(delegate, skipna=skipna, **kwds)

File ~/myenv/lib/python3.11/site-packages/pandas/core/nanops.py:147, in bottleneck_switch.__call__.<locals>.f(values, axis, skipna, **kwds)
    145         result = alt(values, axis=axis, skipna=skipna, **kwds)
    146 else:
--> 147     result = alt(values, axis=axis, skipna=skipna, **kwds)
    149 return result

File ~/myenv/lib/python3.11/site-packages/pandas/core/nanops.py:404, in _datetimelike_compat.<locals>.new_func(values, axis, skipna, mask, **kwargs)
    401 if datetimelike and mask is None:
    402     mask = isna(values)
--> 404 result = func(values, axis=axis, skipna=skipna, mask=mask, **kwargs)
    406 if datetimelike:
    407     result = _wrap_results(result, orig_values.dtype, fill_value=iNaT)

File ~/myenv/lib/python3.11/site-packages/pandas/core/nanops.py:720, in nanmean(values, axis, skipna, mask)
    718 count = _get_counts(values.shape, mask, axis, dtype=dtype_count)
    719 the_sum = values.sum(axis, dtype=dtype_sum)
--> 720 the_sum = _ensure_numeric(the_sum)
    722 if axis is not None and getattr(the_sum, "ndim", False):
    723     count = cast(np.ndarray, count)

File ~/myenv/lib/python3.11/site-packages/pandas/core/nanops.py:1701, in _ensure_numeric(x)
   1698 elif not (is_float(x) or is_integer(x) or is_complex(x)):
   1699     if isinstance(x, str):
   1700         # GH#44008, GH#36703 avoid casting e.g. strings to numeric
-> 1701         raise TypeError(f"Could not convert string '{x}' to numeric")
   1702     try:
   1703         x = float(x)

TypeError: Could not convert string 'XYZXYZ' to numeric
df_new = df.loc[:, "val1" : "val2"]
df_new
val1	val2
0	2	92
1	15	245
2	25	325
3	14	254
4	3	103
5	91	961
df_new.apply(np.mean)
val1     25.0
val2    330.0
dtype: float64
df_new["val2"].mean()
np.float64(330.0)
df_new.apply(np.mean, axis = 1)
0     47.0
1    130.0
2    175.0
3    134.0
4     53.0
5    526.0
dtype: float64
df.groupby("groups").apply(np.mean)
groups
X     90.5
Y     91.5
Z    350.5
dtype: float64
df2 = pd.DataFrame({'val1':[2, 4, 6, 8, 10], 'val2':['Turkey', 'UK', 'Australia', 'Philippines', 'Egypt']})
df2
val1	val2
0	2	Turkey
1	4	UK
2	6	Australia
3	8	Philippines
4	10	Egypt
def cube(x):
    return x ** 3
df.val1.apply(cube)
0         8
1      3375
2     15625
3      2744
4        27
5    753571
Name: val1, dtype: int64
df2.val2.apply(len)
0     6
1     2
2     9
3    11
4     5
Name: val2, dtype: int64
 
