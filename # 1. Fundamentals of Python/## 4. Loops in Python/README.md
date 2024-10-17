# Understanding Loops in Python

In this guide, we will cover the basics of loop concepts in Python, including the different types of loops, loop control statements, and the `range()` function.

## What are Loops?

Loops are statements that allow code to run repeatedly. In general, statements in Python are executed sequentially, one after another. However, there are situations when we need to execute a block of code multiple times. This is where loops come into play.

There are two main types of loops in Python:
- **while loops**
- **for loops**

### While Loops

A `while` loop allows us to repeat one or more actions while a condition remains `True`. Once the condition becomes `False`, the loop ends, and the program continues with the next statement.

Example:

```python
i = 0
while i < 15:
    print(i)
    i += 1
