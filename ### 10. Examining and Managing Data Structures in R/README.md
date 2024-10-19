
# Data Structures in R: Vectors and Lists

## Introduction

In R, vectors are fundamental data structures that contain elements of the same type. There are two types of vectors:

1. **Atomic vectors**: These include six data types: logical, integer, double, character, complex, and raw.
2. **Lists**: Also known as recursive vectors, lists can contain other lists and can be heterogeneous, while atomic vectors are homogeneous.

## Vector Types

### Atomic Vectors

Atomic vectors are classified into several types:

- **Logical**
- **Integer**
- **Double** (numeric vectors)
- **Character**
- **Complex**
- **Raw**

The key difference between **double** and **integer** vectors is that double refers to double precision floating-point numbers, and the difference lies in how they are stored.

### Lists

Lists are vectors that can contain different types of elements. While atomic vectors contain only one type, lists can store heterogeneous data types.

## Creating Vectors

### Atomic Vectors

We can create an atomic vector using the `c()` (concatenate) function:

```r
atomic_vector <- c(1, 2, 3, 4, 5)
```

Values can be assigned using either the equal sign `=` or the arrow `<-`.

### Lists

A list can be created using the `list()` function:

```r
my_list <- list("a", 1, TRUE)
```

### Sequences in Vectors

To create a sequence of integers, use the colon operator `:`:

```r
seq_vector <- 1:10
```

## Checking Vector Types and Length

### Type of Vector

You can check the type of a vector using the `typeof()` function:

```r
typeof(atomic_vector)  # Returns "double"
typeof(my_list)  # Returns "list"
```

### Length of Vector

The length of a vector can be checked using the `length()` function:

```r
length(atomic_vector)  # Returns 5
length(my_list)  # Returns 3
```

You can further examine the elements within a list using `summary()`:

```r
summary(my_list)
```

## Creating Sequences with Steps

We can specify steps in a sequence using the `seq()` function. For example:

```r
sequence_vector <- seq(5, 10, by = 0.5)
```

This creates a vector starting at 5, increasing by 0.5, until it reaches 10.

### Decreasing Sequences

To create a sequence of decreasing numbers:

```r
decreasing_seq <- seq(10, 5, by = -1)
```

### Specifying Length

We can specify the length of a vector and let R calculate the step size using the `length.out` argument:

```r
length_vector <- seq(-5, 1, length.out = 8)
```

## Combining Vectors

To combine two vectors, use the `c()` function:

```r
combined_vector <- c(vector1, vector2)
```

This merges two vectors and maintains the order of elements from both.


