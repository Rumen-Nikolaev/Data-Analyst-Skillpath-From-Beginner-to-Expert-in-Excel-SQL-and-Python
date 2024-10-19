
# Graphs and Charts in R

## Pie Chart

A pie chart represents values as slices of a circle with different colors. The slices are labeled, and the numbers corresponding to each slice are also represented in the chart.

Before creating graphs and charts, it is recommended to reset your graphics device. Subsequent plots will use default graphics settings, and to reset your graphics device, call the following code from the console:

```r
dev.off()
```

### Basic Syntax for Pie Chart

The `pie()` function in R is used to create pie charts. It takes positive numbers as a vector input, and additional parameters are used to control labels, colors, titles, etc.

#### Syntax:

```r
pie(x, labels, radius, main, col, clockwise)
```

- `x`: A vector containing numeric values used in the pie chart.
- `labels`: Descriptions of the slices.
- `radius`: Radius of the circle, a value between -1 and 1.
- `main`: Title of the chart.
- `col`: Color palette.
- `clockwise`: Logical value, indicating if slices are drawn clockwise or counterclockwise.

#### Example:

```r
# Data for the graph
x <- c(10, 20, 30, 40)
labels <- c("A", "B", "C", "D")

# Basic pie chart
pie(x, labels)

# Adding a title and using a rainbow color palette
pie(x, labels, main = "Pie Chart Example", col = rainbow(length(x)))

# Adding a legend
legend("topright", labels, fill = rainbow(length(x)))
```

### 3D Pie Chart

To create a 3D pie chart, you can use the `plotrix` package, which has the `pie3D()` function.

#### Example:

```r
# Install and load the plotrix package
install.packages("plotrix")
library(plotrix)

# Data for the chart
x <- c(10, 20, 30, 40)
labels <- c("A", "B", "C", "D")

# 3D pie chart
pie3D(x, labels = labels, explode = 0.1, main = "3D Pie Chart Example")
```

## Bar Chart

A bar chart represents data using rectangular bars. The length of the bar is proportional to the value of the variable. You can create vertical or horizontal bars using the `barplot()` function.

#### Syntax:

```r
barplot(height, names.arg, xlab, ylab, main, col)
```

- `height`: A vector or matrix containing numeric values.
- `names.arg`: Labels under each bar.
- `xlab`: Label for the x-axis.
- `ylab`: Label for the y-axis.
- `main`: Title of the bar chart.
- `col`: Colors for the bars.

#### Example:

```r
# Data for the chart
x <- c(10, 20, 30, 40)
names <- c("A", "B", "C", "D")

# Basic bar chart
barplot(x, names.arg = names)

# Bar chart with title and colors
barplot(x, names.arg = names, main = "Bar Chart Example", col = rainbow(length(x)))
```

### Grouped and Stacked Bar Charts

Using matrices as input, you can create grouped and stacked bar charts.

#### Example:

```r
# Data for the chart
movies <- matrix(c(10, 20, 15, 25), nrow = 2)

# Grouped bar chart
barplot(movies, beside = TRUE, col = c("red", "blue"), main = "Grouped Bar Chart")

# Stacked bar chart
barplot(movies, col = c("red", "blue"), main = "Stacked Bar Chart")
```

## Box Plot

A box plot (or whisker plot) is used to represent the distribution of a set of data. The `boxplot()` function is used for this.

#### Syntax:

```r
boxplot(x, main, xlab, ylab, col)
```

- `x`: A numeric vector or list of numeric vectors.
- `main`: Title of the box plot.
- `xlab`: Label for the x-axis.
- `ylab`: Label for the y-axis.
- `col`: Color for the box.

#### Example:

```r
# Data for the box plot
data(mtcars)

# Basic box plot
boxplot(mpg ~ cyl, data = mtcars, main = "MPG Box Plot", xlab = "Number of Cylinders", ylab = "Miles per Gallon", col = "lightblue")
```

## Histogram

Histograms represent the distribution of numerical data. The `hist()` function is used to create histograms.

#### Syntax:

```r
hist(x, main, xlab, col, breaks, freq)
```

- `x`: A numeric vector.
- `main`: Title of the histogram.
- `xlab`: Label for the x-axis.
- `col`: Color for the bars.
- `breaks`: Number of breaks in the histogram.
- `freq`: If `TRUE`, counts are plotted. If `FALSE`, probability density is plotted.

#### Example:

```r
# Data for the histogram
data(mtcars)

# Basic histogram
hist(mtcars$mpg, main = "Histogram of MPG", xlab = "Miles per Gallon", col = "lightgreen", breaks = 10)
```

## Line Chart

A line chart connects a series of data points with line segments. The `plot()` function is used to create line charts.

#### Syntax:

```r
plot(x, y, type, xlab, ylab, main, col)
```

- `x`: A vector of x coordinates.
- `y`: A vector of y coordinates.
- `type`: Type of plot. Use "l" for lines, "p" for points, and "o" for both.
- `xlab`: Label for the x-axis.
- `ylab`: Label for the y-axis.
- `main`: Title of the chart.
- `col`: Color of the lines and points.

#### Example:

```r
# Data for the line chart
x <- 1:10
y <- x^2

# Basic line chart
plot(x, y, type = "o", main = "Line Chart Example", xlab = "X Values", ylab = "Y Values", col = "blue")
```

## Scatter Plot

Scatter plots represent the relationship between two variables. The `plot()` function can be used to create scatter plots.

#### Syntax:

```r
plot(x, y, main, xlab, ylab, pch, col)
```

- `x`: A vector of x coordinates.
- `y`: A vector of y coordinates.
- `main`: Title of the scatter plot.
- `xlab`: Label for the x-axis.
- `ylab`: Label for the y-axis.
- `pch`: Plotting symbol.
- `col`: Color of the points.

#### Example:

```r
# Data for the scatter plot
data(mtcars)

# Basic scatter plot
plot(mtcars$wt, mtcars$mpg, main = "Scatter Plot Example", xlab = "Weight", ylab = "Miles per Gallon", pch = 19, col = "red")
```

### 3D Scatter Plot

You can create 3D scatter plots using the `scatterplot3d` package.

#### Example:

```r
# Install and load scatterplot3d package
install.packages("scatterplot3d")
library(scatterplot3d)

# Data for 3D scatter plot
x <- mtcars$wt
y <- mtcars$mpg
z <- mtcars$hp

# 3D scatter plot
scatterplot3d(x, y, z, main = "3D Scatter Plot Example", pch = 19, color = "blue")
```


