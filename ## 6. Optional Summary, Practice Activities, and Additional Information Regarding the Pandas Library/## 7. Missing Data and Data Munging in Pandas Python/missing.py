import pandas as pd
Plates = pd.Series({"Car_1": "YE66PUX","Car_2":"LE17SAL","Car_3":"BA64ZET","Car_4":"SA61ZY"})
Plates
Car_1    YE66PUX
Car_2    LE17SAL
Car_3    BA64ZET
Car_4     SA61ZY
dtype: object
Plates.str.match(r"\w{7}")
Car_1     True
Car_2     True
Car_3     True
Car_4    False
dtype: bool
Plates = pd.Series({"Car_1":"YE66 PUX","Car_2":"LE17 SAL","Car_3":"BA64 ZET","Car_4":"SA61 ZY"})
Plates.str.contains("[A-Z]{3}")
Car_1     True
Car_2     True
Car_3     True
Car_4    False
dtype: bool
Plates.str.match("[A-Z]{3}")
Car_1    False
Car_2    False
Car_3    False
Car_4    False
dtype: bool
Contacts = [["John Doe","johndoe@abcz.com","1111111111"],
            ["Jane Doe","janedoe@abcz.com","2222222222"],
            ["Charlie Brown","charliebrown@abcz.com","3333333333"]]
Contacts_DF = pd.DataFrame(Contacts, columns= ["Name","Email","Phone"])
Contacts_DF
Name	Email	Phone
0	John Doe	johndoe@abcz.com	1111111111
1	Jane Doe	janedoe@abcz.com	2222222222
2	Charlie Brown	charliebrown@abcz.com	3333333333
import re
def get_formatted_phone(value):
    result = re.fullmatch(r"(\d{3}){\d{3}{\d{4}",value)
    return "-".join(result.groups()) if result else value
F_Phone = Contacts_DF["Phone"].map(get_formatted_phone)
F_Phone
0    1111111111
1    2222222222
2    3333333333
Name: Phone, dtype: object
