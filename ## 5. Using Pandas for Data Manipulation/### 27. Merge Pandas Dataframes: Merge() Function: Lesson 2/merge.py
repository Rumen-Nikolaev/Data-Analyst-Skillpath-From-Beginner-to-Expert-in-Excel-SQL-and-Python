import numpy as np
import pandas as pd
df1 = pd.DataFrame({'employee': ['Julia', 'Marie', 'Adam', 'Nicole'],
                    'department': ['Data Science', 'Web Development', 'Data Science', 'Cyber Security'],
                    'Year': ['2005', '2008', '2011', '2002']})

df2 = pd.DataFrame({'employee': ['Nicole', 'Adam', 'Julia', 'Marie'],
                    'country': ['Canada', 'England', 'USA', 'Germany'],
                    'salary': ['22000', '16000', '20000', '17500']})
df3 = pd.DataFrame({'manager': ['Abraham', "Joseph", "Kayra"],
                    'department': ['Web Development', 'Cyber Security', 'Data Science']})
df3
manager	department
0	Abraham	Web Development
1	Joseph	Cyber Security
2	Kayra	Data Science
df4 = pd.merge(df1, df2)
df4
employee	department	Year	country	salary
0	Julia	Data Science	2005	USA	20000
1	Marie	Web Development	2008	Germany	17500
2	Adam	Data Science	2011	England	16000
3	Nicole	Cyber Security	2002	Canada	22000
pd.merge(df4, df3, on = "department", how = "right")
employee	department	Year	country	salary	manager
0	Marie	Web Development	2008	Germany	17500	Abraham
1	Nicole	Cyber Security	2002	Canada	22000	Joseph
2	Julia	Data Science	2005	USA	20000	Kayra
3	Adam	Data Science	2011	England	16000	Kayra
df5 = pd.merge(df4, df3, on = "department", how = "right")
df6 = pd.DataFrame({'department': ['Web Development', 'Web Development', 'Cyber Security', 'Cyber Security',
                                   'Data Science', 'Data Science'],
                    'prog_lang': ['HTML', 'CSS', 'C++', 'SQL', 'PYTHON', 'R'],})
df6
department	prog_lang
0	Web Development	HTML
1	Web Development	CSS
2	Cyber Security	C++
3	Cyber Security	SQL
4	Data Science	PYTHON
5	Data Science	R
pd.merge(df5, df6)
employee	department	Year	country	salary	manager	prog_lang
0	Marie	Web Development	2008	Germany	17500	Abraham	HTML
1	Marie	Web Development	2008	Germany	17500	Abraham	CSS
2	Nicole	Cyber Security	2002	Canada	22000	Joseph	C++
3	Nicole	Cyber Security	2002	Canada	22000	Joseph	SQL
4	Julia	Data Science	2005	USA	20000	Kayra	PYTHON
5	Julia	Data Science	2005	USA	20000	Kayra	R
6	Adam	Data Science	2011	England	16000	Kayra	PYTHON
7	Adam	Data Science	2011	England	16000	Kayra	R
