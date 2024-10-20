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
df5 = pd.DataFrame({'member': ['George', 'Marie', 'Nicole', 'Donald'],
                    'family_member': ['4', '5', '1', '3']})
df5
member	family_member
0	George	4
1	Marie	5
2	Nicole	1
3	Donald	3
pd.merge(df3, df5, left_on = "employee", right_on = "member")
employee	department	Year	country	salary	member	family_member
0	Marie	Web Development	2008	Germany	17500	Marie	5
1	Nicole	Cyber Security	2002	Canada	22000	Nicole	1
pd.merge(df3, df5, left_on = "employee", right_on = "member", how = "outer")
employee	department	Year	country	salary	member	family_member
0	Adam	Data Science	2011	England	16000	NaN	NaN
1	NaN	NaN	NaN	NaN	NaN	Donald	3
2	NaN	NaN	NaN	NaN	NaN	George	4
3	Julia	Data Science	2005	USA	20000	NaN	NaN
4	Marie	Web Development	2008	Germany	17500	Marie	5
5	Nicole	Cyber Security	2002	Canada	22000	Nicole	1
pd.merge(df3, df5, left_on = "employee", right_on = "member", how = "left")
employee	department	Year	country	salary	member	family_member
0	Julia	Data Science	2005	USA	20000	NaN	NaN
1	Marie	Web Development	2008	Germany	17500	Marie	5
2	Adam	Data Science	2011	England	16000	NaN	NaN
3	Nicole	Cyber Security	2002	Canada	22000	Nicole	1
pd.merge(df3, df5, left_on = "employee", right_on = "member", how = "right")
employee	department	Year	country	salary	member	family_member
0	NaN	NaN	NaN	NaN	NaN	George	4
1	Marie	Web Development	2008	Germany	17500	Marie	5
2	Nicole	Cyber Security	2002	Canada	22000	Nicole	1
3	NaN	NaN	NaN	NaN	NaN	Donald	3
