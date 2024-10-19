#Vector Basics

#Creating a vector

atomic_vector=c(1,2,3,4,5)

#creating a list

list <- list("a", TRUE, 1:10)

typeof(atomic_vector)
typeof(list)

#length of a vector

length(atomic_vector)
length(list)

summary(list)

vec <- seq(from=5, to=10, by=0.5)
print(vec)
(vec <- seq(from=5, to=10, by=0.5))

(vec <- seq(from=10, to=5, by=-0.5))
(vec2 <- seq(from=-5, to=1, length.out=8))
(vec_comb <- c(vec,vec2))
