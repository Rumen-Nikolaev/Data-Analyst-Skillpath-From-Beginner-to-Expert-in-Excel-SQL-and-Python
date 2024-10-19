#atomic vector types in R

#logical vectors

#FALSE, TRUE, NA

logic <- 1:4*2==8

typeof(logic)

#numeric vectors

v <- c(1,2,3,4,5)
typeof(v)

v2 <- c(1L,2L,3L,4L,5L)
typeof(v2)

x <- c("apple", "orange", "banana")
typeof(x)
length(x)
nchar(x)

head(letters,3)
tail(letters,3)
