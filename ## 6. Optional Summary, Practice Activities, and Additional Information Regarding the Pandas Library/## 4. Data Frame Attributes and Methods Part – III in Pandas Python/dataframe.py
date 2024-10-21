import numpy as np
import pandas as pd
P_Dict_Sale = {"Chocolate":[70,45,65,35,65,60,44],
                "Bread":[63,51,59,46,55,71,39],
                "Biscuits":[150,90,143,87,79,56,135],
                "Potatoes(kg)":[45,67,38,33,41,29,27],
                "Carrots(kg)":[33,44,45,41,46,39,51],
                "Chips":[35,0,28,70,36,43,0],
                "Crackers":[0,13,45,39,47,46,51]}
P_DFrames = pd.DataFrame(P_Dict_Sale)
P_DFrames = pd.DataFrame(P_Dict_Sale, index = ["Week 1","Week 2","Week 3","Week 4","Week 5","Week 6","Week 7"])
P_DFrames
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	70	63	150	45	33	35	0
Week 2	45	51	90	67	44	0	13
Week 3	65	59	143	38	45	28	45
Week 4	35	46	87	33	41	70	39
Week 5	65	55	79	41	46	36	47
Week 6	60	71	56	29	39	43	46
Week 7	44	39	135	27	51	0	51
P_DFrames.head()
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	70	63	150	45	33	35	0
Week 2	45	51	90	67	44	0	13
Week 3	65	59	143	38	45	28	45
Week 4	35	46	87	33	41	70	39
Week 5	65	55	79	41	46	36	47
P_DFrames.head(3)
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	70	63	150	45	33	35	0
Week 2	45	51	90	67	44	0	13
Week 3	65	59	143	38	45	28	45
P_DFrames.head(6)
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	70	63	150	45	33	35	0
Week 2	45	51	90	67	44	0	13
Week 3	65	59	143	38	45	28	45
Week 4	35	46	87	33	41	70	39
Week 5	65	55	79	41	46	36	47
Week 6	60	71	56	29	39	43	46
P_DFrames.tail()
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 3	65	59	143	38	45	28	45
Week 4	35	46	87	33	41	70	39
Week 5	65	55	79	41	46	36	47
Week 6	60	71	56	29	39	43	46
Week 7	44	39	135	27	51	0	51
P_DFrames.tail(2)
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 6	60	71	56	29	39	43	46
Week 7	44	39	135	27	51	0	51
P_DFrames.tail(7)
Chocolate	Bread	Biscuits	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	70	63	150	45	33	35	0
Week 2	45	51	90	67	44	0	13
Week 3	65	59	143	38	45	28	45
Week 4	35	46	87	33	41	70	39
Week 5	65	55	79	41	46	36	47
Week 6	60	71	56	29	39	43	46
Week 7	44	39	135	27	51	0	51
P_DFrames.insert(3, "Onions(kg)",[25,33,31,36,44,19,27])
P_DFrames
Chocolate	Bread	Biscuits	Onions(kg)	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	70	63	150	25	45	33	35	0
Week 2	45	51	90	33	67	44	0	13
Week 3	65	59	143	31	38	45	28	45
Week 4	35	46	87	36	33	41	70	39
Week 5	65	55	79	44	41	46	36	47
Week 6	60	71	56	19	29	39	43	46
Week 7	44	39	135	27	27	51	0	51
P_DFrames["Potatoes(kg)"] = P_DFrames["Potatoes(kg)"] / 10
P_DFrames
Chocolate	Bread	Biscuits	Onions(kg)	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	70	63	150	25	4.5	33	35	0
Week 2	45	51	90	33	6.7	44	0	13
Week 3	65	59	143	31	3.8	45	28	45
Week 4	35	46	87	36	3.3	41	70	39
Week 5	65	55	79	44	4.1	46	36	47
Week 6	60	71	56	19	2.9	39	43	46
Week 7	44	39	135	27	2.7	51	0	51
P_DFrames["Carrots(kg)"] = P_DFrames["Carrots(kg)"]+5
P_DFrames
Chocolate	Bread	Biscuits	Onions(kg)	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	70	63	150	25	4.5	38	35	0
Week 2	45	51	90	33	6.7	49	0	13
Week 3	65	59	143	31	3.8	50	28	45
Week 4	35	46	87	36	3.3	46	70	39
Week 5	65	55	79	44	4.1	51	36	47
Week 6	60	71	56	19	2.9	44	43	46
Week 7	44	39	135	27	2.7	56	0	51
P_DFrames["Onions(kg)"] += 5
P_DFrames
Chocolate	Bread	Biscuits	Onions(kg)	Potatoes(kg)	Carrots(kg)	Chips	Crackers
Week 1	70	63	150	30	4.5	38	35	0
Week 2	45	51	90	38	6.7	49	0	13
Week 3	65	59	143	36	3.8	50	28	45
Week 4	35	46	87	41	3.3	46	70	39
Week 5	65	55	79	49	4.1	51	36	47
Week 6	60	71	56	24	2.9	44	43	46
Week 7	44	39	135	32	2.7	56	0	51
P_DFrames["Chocolate"].value_counts()
Chocolate
65    2
70    1
45    1
35    1
60    1
44    1
Name: count, dtype: int64
 
