# Conditional Statements in Python

In this section, we explore conditional statements in Python, which are essential for decision-making and controlling the flow of a program.

## Decision Making

Decision making in programming involves anticipating conditions and specifying actions based on whether the conditions evaluate to `True` or `False`. Python supports decision-making structures, most commonly through `if` statements and loops.

Python assumes any non-zero or non-`None` values as `True`, and `0` or `None` as `False`.

## Control Statements

### `if` Statement

The `if` statement is a control structure that allows a block of code to execute if a condition evaluates to `True`. If the condition is `False`, the block of code is skipped.

Example:
```python
age = int(input("Enter your age: "))
if age < 21:
    print("You can't enter this place.")
