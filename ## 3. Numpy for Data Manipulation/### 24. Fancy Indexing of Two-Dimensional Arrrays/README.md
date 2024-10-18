# Fancy Indexing and Two-Dimensional Arrays

This document demonstrates how to use **fancy indexing** in Python with **NumPy** and how to work with two-dimensional arrays.

## Getting Started

1. First, import the necessary library:

    ```python
    import numpy as np
    ```

2. Create a **two-dimensional array** of zeros (10x10 matrix):

    ```python
    array = np.zeros((10, 10), dtype=int)
    ```

3. Let's fill each row of the array with its index value:

    ```python
    rows = array.shape[0]  # Get the number of rows
    for i in range(rows):
        array[i] = i
    ```

4. To check the final array:

    ```python
    print(array)
    ```

The array will be filled as:

