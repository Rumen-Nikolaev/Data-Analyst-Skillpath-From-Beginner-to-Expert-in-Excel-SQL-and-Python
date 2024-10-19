pie(x, labels, radius, main, col, clockwise)

x <- c(30,40,10,20)
labels <- c("Scifi", "Comedy", ".Action", "Romance")
pie(x,labels)
pie(x,labels, main="Movie Types",
    col=rainbow(length(x)))
legend("topright", labels, cex=0.5,
       fill=rainbow(length(x)))


install.packages("plotrix")
labels3d <- c("Scifi", "Comedy", ".Action", "Romance")
pie3D(x, labels=labels3d, explode=0.4,
      main="Pie Chart of Countries")

barplot(H,xlab,ylab,main, names.arg,col)
barplot(x)
x <- c(32,38,10,20)
labels <- c("Scifi","Comedy","Action","Romance")
barplot(x, names.arg = labels, 
        xlab = "Type", 
        ylab = "Popularity", 
        col = "orange", 
        main = "Movie Types", 
        border = "blue")

# Movie types and categories of moviegoers
movietypes <- c("Scifi", "Comedy", "Action", "Romance")
moviegoer <- c("men", "women", "children")

# Correctly create a 4x3 matrix (4 movie types and 3 categories)
matrixvalues <- matrix(c(12, 5, 8, 
                         11, 10, 4, 
                         18, 7, 9, 
                         4, 15, 2), 
                       nrow = 4, ncol = 3, byrow = TRUE)

# Create the barplot
barplot(matrixvalues, 
        main = "Moviegoer", 
        names.arg = movietypes, 
        xlab = "Types", 
        ylab = "Filmgoer", 
        col = rainbow(ncol(matrixvalues))) # Use ncol to get the number of columns

barplot(matrixvalues,main="Moviegoer",
        names.arg=movietypes, xlab="Types", ylab="Filmgoer",
        col=rannbow(length(x)))

legend("topright", movigoer, cex=0.55, fill=rainbow(length(x)))

dev.off()

legend("topright",movigoer, cex=0.55, fill=rainbow(length(x)),
       bg="lightblue")

library(MASS)
str(Cars93)
names(Cars93)
boxplot(Cars93$MPG.city)
summary(Cars93$MPG.city)
boxplot(Cars93$MPG.city, main="93 Model Cars City MPG",
        xlab="Miles per Gallon", ylab="93 Model Cars",
        col="skyblue", border="red", horizontal = TRUE,
        notch=TRUE)
boxplot(Cars93$MPG.city, Cars93$EngineSize)
boxplot(Cars93$MPG.city ~ Cars93$Type)
