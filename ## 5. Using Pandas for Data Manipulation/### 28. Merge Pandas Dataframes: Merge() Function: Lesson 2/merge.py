import numpy as np
import pandas as pd
df1 = pd.DataFrame({'employee': ['Julia', 'Marie', 'Adam', 'Nicole'],
                    'department': ['Data Science', 'Web Development', 'Data Science', 'Cyber Security'],
                    'Year': ['2005', '2008', '2011', '2002']})

df2 = pd.DataFrame({'employee': ['Nicole', 'Adam', 'Julia', 'Marie'],
                    'country': ['Canada', 'England', 'USA', 'Germany'],
                    'salary': ['22000', '16000', '20000', '17500']})

df3 = pd.merge(df1, df2)
df3
employee	department	Year	country	salary
0	Julia	Data Science	2005	USA	20000
1	Marie	Web Development	2008	Germany	17500
2	Adam	Data Science	2011	England	16000
3	Nicole	Cyber Security	2002	Canada	22000
df4 = pd.DataFrame({'employee': ['Julia', 'Alex', 'Adam', 'Kayra'],
                    'department': ['Data Science', 'Web Development', 'Data Science', 'Cyber Security'],
                    'university': ['harvard', 'hamburg', 'oxford', 'metu']})
df4
employee	department	university
0	Julia	Data Science	harvard
1	Alex	Web Development	hamburg
2	Adam	Data Science	oxford
3	Kayra	Cyber Security	metu
pd.merge(df3, df4, on = ["employee", "department"])
employee	department	Year	country	salary	university
0	Julia	Data Science	2005	USA	20000	harvard
1	Adam	Data Science	2011	England	16000	oxford
pd.merge(df3, df4, on = ["employee", "department"], how = "outer")
employee	department	Year	country	salary	university
0	Adam	Data Science	2011	England	16000	oxford
1	Alex	Web Development	NaN	NaN	NaN	hamburg
2	Julia	Data Science	2005	USA	20000	harvard
3	Kayra	Cyber Security	NaN	NaN	NaN	metu
4	Marie	Web Development	2008	Germany	17500	NaN
5	Nicole	Cyber Security	2002	Canada	22000	NaN
pd.merge(df3, df4, on = ["employee", "department"], how = "left")
employee	department	Year	country	salary	university
0	Julia	Data Science	2005	USA	20000	harvard
1	Marie	Web Development	2008	Germany	17500	NaN
2	Adam	Data Science	2011	England	16000	oxford
3	Nicole	Cyber Security	2002	Canada	22000	NaN
pd.merge(df3, df4, on = ["employee", "department"], how = "right")
employee	department	Year	country	salary	university
0	Julia	Data Science	2005	USA	20000	harvard
1	Alex	Web Development	NaN	NaN	NaN	hamburg
2	Adam	Data Science	2011	England	16000	oxford
3	Kayra	Cyber Security	NaN	NaN	NaN	metu
