# Exploring NumPy Array Properties

In this guide, we will examine the properties of NumPy arrays using various functions.

## Functions to Explore

1. **ndim**: This function gives us information about the number of dimensions of the array. It can return:
   - 1 for one-dimensional arrays
   - 2 for two-dimensional arrays
   - 3 for three-dimensional arrays
   - And more!

2. **shape**: This function allows us to learn the size of the array. For example, it can return shapes like:
   - (3, 3) for a 3x3 matrix
   - (4, 2) for a 4x2 matrix
   - It also provides information about the size in a specific way.

3. **size**: This function gives us the total number of elements in the array.

4. **dtype**: This function returns the data type of the NumPy array, such as integer or float.

## Example Code

Now let's put these functions into practice.

1. First, import NumPy:
   ```python
   import numpy as np
