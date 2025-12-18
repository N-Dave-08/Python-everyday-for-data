# Python Cheatsheet for Data Analysis

Quick reference guide for Python fundamentals and data analysis.

## Variables and Data Types

```python
# Variables
name = "John"
age = 30
price = 19.99
is_active = True
value = None

# Type checking
type(variable)

# Type conversion
int(value)
float(value)
str(value)
bool(value)
```

## Basic Operations

```python
# Arithmetic
a + b  # Addition
a - b  # Subtraction
a * b  # Multiplication
a / b  # Division (float)
a // b  # Floor division
a % b  # Modulus
a ** b  # Exponentiation

# Comparison
a == b  # Equal
a != b  # Not equal
a > b   # Greater than
a < b   # Less than
a >= b  # Greater or equal
a <= b  # Less or equal

# Logical
a and b  # AND
a or b   # OR
not a    # NOT
```

## Strings

```python
# Methods
text.upper()
text.lower()
text.strip()
text.split()
text.replace(old, new)
text.find(substring)
text.count(char)
len(text)

# Formatting
f"Hello, {name}"
"Hello, {}".format(name)
```

## Lists

```python
# Create
my_list = [1, 2, 3]
my_list = list(range(5))

# Access
my_list[0]        # First element
my_list[-1]       # Last element
my_list[1:3]      # Slice

# Methods
my_list.append(item)
my_list.extend(other_list)
my_list.insert(index, item)
my_list.remove(item)
my_list.pop()
my_list.sort()
my_list.reverse()
len(my_list)
```

## Dictionaries

```python
# Create
my_dict = {'key': 'value'}
my_dict = dict(key='value')

# Access
my_dict['key']
my_dict.get('key', default)

# Methods
my_dict.keys()
my_dict.values()
my_dict.items()
my_dict.update(other_dict)
del my_dict['key']
```

## Control Flow

```python
# If/Else
if condition:
    code
elif condition:
    code
else:
    code

# For loop
for item in iterable:
    code

# While loop
while condition:
    code

# Break/Continue
break      # Exit loop
continue   # Skip to next iteration
```

## Functions

```python
# Define
def function_name(param1, param2):
    return result

# Lambda
lambda x: x * 2
```

## File I/O

```python
# Read file
with open('file.txt', 'r') as f:
    content = f.read()

# Write file
with open('file.txt', 'w') as f:
    f.write(content)
```

## Pandas Basics

```python
import pandas as pd

# Read CSV
df = pd.read_csv('file.csv')

# Basic operations
df.head()
df.info()
df.describe()
df.shape
df.columns

# Selection
df['column']
df[['col1', 'col2']]
df[df['column'] > value]

# Filtering
df[df['column'] == value]
df[(df['col1'] > x) & (df['col2'] < y)]

# Grouping
df.groupby('column').sum()
df.groupby('column').mean()
```

## NumPy Basics

```python
import numpy as np

# Create array
arr = np.array([1, 2, 3])

# Operations
arr.mean()
arr.sum()
arr.max()
arr.min()
arr.std()
```

## Matplotlib Basics

```python
import matplotlib.pyplot as plt

# Line plot
plt.plot(x, y)
plt.show()

# Scatter plot
plt.scatter(x, y)
plt.show()

# Bar chart
plt.bar(x, y)
plt.show()

# Labels
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
```

## Common Patterns

```python
# List comprehension
[x*2 for x in range(10)]

# Dictionary comprehension
{x: x*2 for x in range(10)}

# Filter
filtered = [x for x in list if condition]

# Map
mapped = [function(x) for x in list]
```
