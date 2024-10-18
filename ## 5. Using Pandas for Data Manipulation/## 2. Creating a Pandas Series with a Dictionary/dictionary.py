import pandas as pd
dictionary = {"ferrari" : 334.7, "porche" : 337.9, "lamborghini" : 349}
pd.Series(data = dictionary)
ferrari        334.7
porche         337.9
lamborghini    349.0
dtype: float64
variable = pd.Series(data = dictionary, index = ["porche", "bugatti", "ferrari"])
variable
porche     337.9
bugatti      NaN
ferrari    334.7
dtype: float64
