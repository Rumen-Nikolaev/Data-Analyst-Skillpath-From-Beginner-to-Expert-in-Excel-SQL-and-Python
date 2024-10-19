 Data Manipulation and Reshaping in R

This document outlines the process of data manipulation, reshaping, and merging in R. It covers various functions to split, merge, and change data frames, and how to organize data into rows and columns.

## Prerequisites
- R installed on your machine
- Necessary libraries such as `readxl` (for Excel files) and `MASS` (for built-in datasets)

### Data Frames

Most of the time, data processing in R is done by taking the input data as a **data frame**. There are situations when the data frame needs to be transformed into a different format for further analysis.

### Merging Data Frames

R provides functions to merge two data frames. The data frames must have the same column names on which the merging occurs. The `merge()` function allows merging of data frames, similar to SQL `JOIN` operations.
