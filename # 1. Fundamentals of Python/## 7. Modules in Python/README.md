# Python Modules: Introduction and Usage

## Overview

In Python, a module is a file containing Python code. Modules allow us to organize our code and reuse functions, classes, and variables across different projects. This document introduces the concept of modules and demonstrates how to use them efficiently in Python.

## What is a Module?

A module is a Python file that can define:
- Functions
- Classes
- Variables

It can also include runnable code. By using modules, you can improve the efficiency and organization of your programs, reusing code instead of rewriting functions or classes every time.

## Why Use Modules?

Modules make it easier to manage large programs by breaking them into smaller, reusable components. By integrating a module, you can use its functions and classes in your code, reducing redundancy and simplifying your program's structure.

Without modules, you would need to manually define each function and class in your programs. Modules streamline this process and allow for code reuse across multiple projects.

## Importing Modules

To use a module, Python provides the `import` statement. This statement allows you to include any Python source file as a module in your program.

When the Python interpreter encounters an `import` statement, it searches for the module in the search path, which is a list of directories where Python looks for modules.

### Key Points:
- A module is only loaded once, even if imported multiple times.
- This prevents the module from being executed repeatedly during multiple imports.

## Python Standard Library Modules

Python includes a large number of pre-built modules that you can use in your programs. These modules have been written by Python developers and are part of the Python Standard Library. Additionally, you can find many modules uploaded by developers on platforms like GitHub to extend your program's functionality.

### Example: The `math` Module

The `math` module is a built-in Python module that provides mathematical functions. Here's how to use it:

```python
import math
