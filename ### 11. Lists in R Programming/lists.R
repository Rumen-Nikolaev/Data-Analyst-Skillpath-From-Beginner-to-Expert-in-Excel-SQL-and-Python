#Lists

list <- list(a=1,b=2L,c="a",d=4.5,e="bc")
print(list)

str(list)

list2 <- list(list(a=1,2,3), list(b="a","b","c"),list(c=4L,5L,6L))
str(list2)

x <- list(c("a","b","c"),c(1,2,3))
str(x)

x2 <- list(c("x","y","z"),list(5,6,7,list(8,9,10)))

var1 <- list(x=1:5,y="a character",z=list(8/4,8/2))
var1[1:2]

var1[3]

var1[1:3]
var1[[1:3]]

class(var1["x"])
class(var1[["x"]])

var1[3][2]
var1[[3]][[2]]


var1[[x]]
var1$x
