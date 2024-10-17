# Python Functions: A Guide

## Overview

Functions are an essential building block in programming, allowing us to reuse code and structure complex operations. In Python, functions can simplify tasks and enable code reuse across different parts of a program. This document introduces Python functions, the return statement, and lambda expressions.

## What is a Function?

A function is a block of code that performs a specific task. Instead of writing complex code multiple times, you can encapsulate it within a function and call that function whenever needed.

### Key Features:
- A function is only executed when called.
- You can pass data, known as parameters, into a function.
- Functions can return values after completing their tasks.

For example, the built-in `print()` function in Python is used to print values to the screen.

### Why Use Functions?

Functions make code more organized and reusable. By combining complex steps into a single function, you can easily call that function whenever needed, making your code more efficient and maintainable.

## Defining a Function

In Python, a function is defined using the `def` keyword. You also need to specify a name for the function and optionally provide parameters.

### Example:

```python
def sum(a, b):
    """Returns the sum of two numbers."""
    print(a + b)

# Call the function
sum(4, 5)  # Output: 9
