import numpy as np
import pandas as pd
df1 = pd.DataFrame({'employee': ['Julia', 'Marie', 'Adam', 'Nicole'],
                    'department': ['Data Science', 'Web Development', 'Data Science', 'Cyber Security'],
                    'Year': ['2005', '2008', '2011', '2002']})

df2 = pd.DataFrame({'employee': ['Nicole', 'Adam', 'Julia', 'Marie'],
                    'country': ['Canada', 'England', 'USA', 'Germany'],
                    'salary': ['22000', '16000', '20000', '17500']})
df1
employee	department	Year
0	Julia	Data Science	2005
1	Marie	Web Development	2008
2	Adam	Data Science	2011
3	Nicole	Cyber Security	2002
df2
employee	country	salary
0	Nicole	Canada	22000
1	Adam	England	16000
2	Julia	USA	20000
3	Marie	Germany	17500
pd.concat([df1, df2])
employee	department	Year	country	salary
0	Julia	Data Science	2005	NaN	NaN
1	Marie	Web Development	2008	NaN	NaN
2	Adam	Data Science	2011	NaN	NaN
3	Nicole	Cyber Security	2002	NaN	NaN
0	Nicole	NaN	NaN	Canada	22000
1	Adam	NaN	NaN	England	16000
2	Julia	NaN	NaN	USA	20000
3	Marie	NaN	NaN	Germany	17500
pd.concat([df1, df2], axis = 1)
employee	department	Year	employee	country	salary
0	Julia	Data Science	2005	Nicole	Canada	22000
1	Marie	Web Development	2008	Adam	England	16000
2	Adam	Data Science	2011	Julia	USA	20000
3	Nicole	Cyber Security	2002	Marie	Germany	17500
pd.merge(df1, df2)
employee	department	Year	country	salary
0	Julia	Data Science	2005	USA	20000
1	Marie	Web Development	2008	Germany	17500
2	Adam	Data Science	2011	England	16000
3	Nicole	Cyber Security	2002	Canada	22000
pd.merge(df1, df2, on = "employee")
employee	department	Year	country	salary
0	Julia	Data Science	2005	USA	20000
1	Marie	Web Development	2008	Germany	17500
2	Adam	Data Science	2011	England	16000
3	Nicole	Cyber Security	2002	Canada	22000
pd.merge(df1, df2, on = "employee", how = "left")
employee	department	Year	country	salary
0	Julia	Data Science	2005	USA	20000
1	Marie	Web Development	2008	Germany	17500
2	Adam	Data Science	2011	England	16000
3	Nicole	Cyber Security	2002	Canada	22000
pd.merge(df1, df2, on = "employee", how = "right")
employee	department	Year	country	salary
0	Nicole	Cyber Security	2002	Canada	22000
1	Adam	Data Science	2011	England	16000
2	Julia	Data Science	2005	USA	20000
3	Marie	Web Development	2008	Germany	17500
