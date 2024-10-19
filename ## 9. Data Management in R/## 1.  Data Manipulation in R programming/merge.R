getwd()
setwd("/home/rumen10/Documents")

# We can merge two data frames by using the merge() function

data1 <- read.csv2("test_data.csv")
print(data1)

data2 <- read.csv2("test_data2.csv")
pritn(data2)

data=rbind(data1,data2)

#The merge() function allows four ways of combining data:

# 1- Natural joins - keep only rows that match from the data frames (all=FALSE)

dataMerge <- merge(data1, data2, all=FALSE)
print(dataMerge)
# 2- Full Outer Join - keep all rows from both data frames (all=TRUE)

dataMerge <- merge(data1, data2,all=TRUE)
print(dataMerge)

# 3- Left Join - Include all the rows of your data frame x and only those
# from y that match (x=TRUE)

dataMerge <- merge(data1,data2,all.x=TRUE)
print(dataMerge)

# 4- Right Join - Include all the rows of your data frame y and only those
# from x that match (y=TRUE)

dataMerge <- merge(data1,data2, all.y=TRUE)
print(dataMerge)
