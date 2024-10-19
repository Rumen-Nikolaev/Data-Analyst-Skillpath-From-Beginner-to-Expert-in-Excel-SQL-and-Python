
# Arrays in R

An array is essentially a multidimensional vector. The components must all be of the same type. Individual elements of the components inside an array are accessed in a similar fashion using square brackets.

A vector has only one dimension, but an array with two dimensions is called a matrix. Anything with more than two dimensions is simply called an array. A vector can be used by R as an array only if it has a dimension vector as its `dim` attribute.

## Example: Creating a 3D Array

Suppose `X` is a vector of 12 elements:

```R
X <- 1:12
dim(X) <- c(2, 3, 2)
```

This gives the `dim` attribute that allows it to be treated as a `2 x 3 x 2` array. Here:
- The first element is the row index.
- The second element is the column index.
- The last one is the outer dimension.

This is a three-dimensional array because it is a `2 x 3 x 2` array. The multiplication of these dimensions (2 * 3 * 2) gives us the length of the `X` variable, which corresponds to 12.

## Accessing Elements of the Array

Individual elements of an array can be referenced by giving the name of the array followed by the subscript in square brackets, separated by commas. However, if any index position is given an empty index vector, then the full range of that subscript is selected.

For example:

```R
X[,,] # Display all elements of the 3D array
```

This code means that we want to see all the values within the three dimensions. The output shows two different matrices, and above each matrix, there are two adjacent commas, followed by `1` and `2`, respectively. Two commas along with a number (`1`) means that the first matrix represents all the values that are in the first part of the third dimension. The second matrix is simply the other part of the third dimension. 

Since we assigned the value of `2` for the third dimension, there will be only two different matrices representing each part of the dimension.

## Example: Accessing Specific Elements

We can also reference specific elements. For instance, the first code:

```R
X[1,1,1]
```

Refers to the value within the first row, first column, and the first part of the third dimension, which is simply the value `1`.

We can check this with a logical operator:

```R
X[1,1,1] == 1 # TRUE
```

Similarly, if we want to access the value in the second row, third column, and the second part of the third dimension:

```R
X[2,3,2] == 12 # TRUE
```

## Accessing Entire Rows or Columns

What if we want to see all the values in the first row, no matter what their positions are in the other dimensions? If we choose the first row and leave the other two index positions empty:

```R
X[1,,]
```

This will return all the values in the first row. The result will be:

```
[1] 1 3 5 7 9 11
```

These are the elements of the first row within the vector.

