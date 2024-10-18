import numpy as np
import pandas as pd
example = np.array([1, 3.3, 5, 7.2, 9])
labels = np.array(["a", "b", "c", "d", "e"])
variable = pd.Series(data = example, index = labels)
variable
a    1.0
b    3.3
c    5.0
d    7.2
e    9.0
dtype: float64
