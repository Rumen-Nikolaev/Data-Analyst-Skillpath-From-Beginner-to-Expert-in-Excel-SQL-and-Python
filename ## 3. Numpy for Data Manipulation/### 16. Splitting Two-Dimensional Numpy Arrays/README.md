# Splitting Numpy Arrays

This document provides examples on how to split one-dimensional and two-dimensional numpy arrays using `split`, `hsplit`, and `vsplit` functions.

## One-Dimensional Arrays

### Step 1: Create an Array

```python
import numpy as np

# Create an array with odd, even, and some custom numbers
array = np.array([1, 3, 5, 50, 50, 2, 4, 6])
print(array)
