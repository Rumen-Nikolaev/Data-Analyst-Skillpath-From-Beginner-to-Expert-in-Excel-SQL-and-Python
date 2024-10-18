# Creating Arrays from Scratch with NumPy

This guide demonstrates how to create arrays from scratch using built-in functions from NumPy.

## Understanding NumPy Arrays

A NumPy array is a data structure similar to lists, dictionaries, or tuples. Previously, arrays were created by providing values to a function. Now, arrays can be created without any input values; the function generates the arrays directly.

## Creating Arrays with Built-in Functions

### 1. Using the `zeros` Function

The `zeros` function creates an array filled with zeros of a specified size. The size is defined as a tuple, and the function generates an array according to this size.

#### Example: Creating a One-Dimensional Array

```python
import numpy as np

# Create a one-dimensional array of zeros with 5 elements
array1D = np.zeros(5)
print(array1D)  # Output: [0. 0. 0. 0. 0.]
