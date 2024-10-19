
# Atomic Vector Types in R

There are three common types of atomic vectors in R: logical, numeric, and character vectors.

## Logical Vectors
Logical vectors can take only `FALSE`, `TRUE`, and `NA` values. They are usually constructed with comparison operators, but you can also create them by hand with the `c()` function.

Example:
```r
logic <- c(1*2 == 8, 2*2 == 8, 3*2 == 8, 4*2 == 8)
print(logic)
# Output: [1] FALSE FALSE FALSE TRUE
```

The fourth element is `TRUE`, meaning that only 4 multiplied by 2 equals 8.

To check the type of the new variable:
```r
typeof(logic)
# Output: "logical"
```

## Numeric Vectors
Numeric vectors consist of integer and double numbers. By default, numbers are classified as double in R. To convert a double into an integer, simply place an `L` next to the number.

Example:
```r
numeric_vector <- c(1.0, 2.0, 3.0, 4.0)
print(typeof(numeric_vector))
# Output: "double"
```

Convert double to integer:
```r
integer_vector <- c(1L, 2L, 3L, 4L)
print(typeof(integer_vector))
# Output: "integer"
```

## Character Vectors
Character vectors are composed of string-type elements. Each element of a character vector is a piece of text.

Example:
```r
x <- c("apple", "banana", "cherry")
print(typeof(x))
# Output: "character"
```

To find out how many characters are in each text, use the `nchar()` function:
```r
nchar(x)
# Output: [1] 5 6 6
```

## Extracting Elements
You can extract the first or last elements of a vector using the `head()` and `tail()` functions.

Example:
```r
letters_vector <- letters
head(letters_vector, 3)
# Output: [1] "a" "b" "c"

tail(letters_vector, 3)
# Output: [1] "x" "y" "z"
```
