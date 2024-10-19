
# Working with Lists in R

In R, an **atomic vector** cannot contain a mix of different data types. If you need a mix of multiple types, you should use a **list**.

### Creating a List
Lists are created using the `list()` function. Here's an example:
```r
my_list <- list(1:5, "Hello", TRUE)
```

### Examining the Structure of a List
You can examine the structure of the list (rather than its content) using the `str()` function:
```r
str(my_list)
```

### Adding Sub-lists
Lists can contain **sub-lists**. Here’s an example of a list with sub-lists:
```r
sub_list <- list(list(1:5), list("a", "b"), list(TRUE, FALSE))
str(sub_list)
```

### Combining Lists and Vectors
A list can combine **atomic vectors** and **sub-lists**:
```r
combined_list <- list(c(1, 2, 3), list("A", "B"), list(5.5, 6.7))
str(combined_list)
```

### Subsetting a List
You can extract elements from a list using **single** or **double** brackets:
- **Single brackets (`[]`)**: Extract a sublist.
- **Double brackets (`[[]]`)**: Extract specific elements inside the list.

#### Example:
```r
# Single bracket - extracts a sublist
my_list[1]

# Double bracket - extracts a specific element
my_list[[1]]
```

### Differences Between Single and Double Brackets
- Single brackets return **sub-lists**.
- Double brackets return **individual elements**.

#### Example of extracting:
```r
# Create a list
variable1 <- list(x = 1:5, y = "Hello", z = list(2, 4))

# Single bracket - extracts the first sublist
variable1[1] 

# Double bracket - extracts the first element of the first sublist
variable1[[1]]
```

### Extracting a Specific Element from a Sublist
To extract an element from a sublist, use nested double brackets:
```r
# Extract the second element of the third component (which is a sublist)
variable1[[3]][[2]]
```

### Using Dollar Sign (`$`)
The dollar sign (`$`) is a shorthand for accessing list components by name:
```r
variable1$x  # Returns the elements of x without using quotes
```

