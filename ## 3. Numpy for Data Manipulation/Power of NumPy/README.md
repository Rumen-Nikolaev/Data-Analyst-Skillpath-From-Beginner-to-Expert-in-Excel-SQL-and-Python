
# NumPy Basics and Practical Usage

This document introduces the basic usage of `NumPy` in Python, specifically its practical advantage in numerical operations and efficiency. We will also explore list manipulation with Python’s built-in tools, compare it with `NumPy`, and demonstrate how to perform array operations efficiently.

## Prerequisites

- Python installed
- `NumPy` library installed (`pip install numpy`)

## Getting Started

### 1. Python's `range()` Function

In Python, the `range()` function generates a sequence of numbers. For example, to generate numbers from `0` to `4` (excluding `5`):

```python
print(list(range(0, 5)))
```

Output:

```
[0, 1, 2, 3, 4]
```

You can also specify a step parameter:

```python
print(list(range(0, 10, 2)))
```

Output:

```
[0, 2, 4, 6, 8]
```

### 2. Creating Lists in Python

Let’s create two lists, `list1` and `list2`, containing odd and even numbers, respectively:

```python
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
```

### 3. Multiplying Two Lists

Attempting to multiply two lists directly results in an error:

```python
result = list1 * list2
```

Output:

```
TypeError: can't multiply sequence by non-int of type 'list'
```

### 4. Correct Approach: Using a Loop

To multiply corresponding elements of two lists manually, we can use a loop:

```python
new_list = []
for i in range(len(list1)):
    new_list.append(list1[i] * list2[i])
print(new_list)
```

Output:

```
[2, 12, 30, 56, 90]
```

### 5. Introducing `NumPy` for Efficiency

`NumPy` makes operations like these much simpler and faster. First, import the `NumPy` library:

```python
import numpy as np
```

### 6. Converting Lists to `NumPy` Arrays

To work with arrays in `NumPy`, convert the lists into `NumPy` arrays:

```python
x = np.array(list1)
y = np.array(list2)
```

### 7. Multiplying Arrays

With `NumPy`, multiplying two arrays is straightforward:

```python
result = x * y
print(result)
```

Output:

```
[ 2 12 30 56 90]
```

## Conclusion

Using `NumPy` is significantly more efficient when performing numerical operations on arrays. While traditional Python lists require loops and manual indexing, `NumPy` handles these operations with simpler and faster array manipulation.
