String_1 = "1234567"
List_1 = [1,2,3,4,5,6,7]
Tuples_1 = (1,2,3,4,5,6,7)
Dict_1 = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7}
Set_1 = {1,2,3,4,5,6,7}
String_1[2]
'3'
List_1[3]
4
Tuples_1[1]
2
String_1[-2]
'6'
List_1[-3]
5
Tuples_1[-1]
7
String_1[2:5]
'345'
List_1[:3]
[1, 2, 3]
Tuples_1[-2:4]
()
len(String_1)
7
len(List_1)
7
len(Tuples_1)
7
len(Set_1)
7
String_1 += "8"
List_1.append(8)
Set_1.add(8)
Dict_1["eight"]=8
String_1
'12345678'
List_1
[1, 2, 3, 4, 5, 6, 7, 8]
Set_1
{1, 2, 3, 4, 5, 6, 7, 8}
Dict_1
{'one': 1,
 'two': 2,
 'three': 3,
 'four': 4,
 'five': 5,
 'six': 6,
 'seven': 7,
 'eight': 8}
List_1.pop(6)
7
Dict_1.pop("eight")
8
List_1
[1, 2, 3, 4, 5, 6]
Dict_1
{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7}
String_2 = "London"
List_2 = ["L","o","n","d","o","n"]
Tuples_2 = ("L","o","n","d","o","n")
String_2.count("n")
2
List_2.count("n")
2
Tuples_2.count("n")
2
Set_2 = {10,11,12}
Dict_2 = {"nine":9, "ten":10,"eleven":11}
Set_1.update(Set_2)
Dict_1.update(Dict_2)
Set_1
{1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12}
Dict_1
{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7}
