# Lesson 1.1: Introduction to Python and Data Analysis

## What is Python?

**Python** is a high-level, interpreted programming language known for its simplicity and readability. It's one of the most popular languages for data analysis, data science, and machine learning.

## Why Python for Data Analysis?

Python has become the go-to language for data analysis because:

- **Easy to Learn**: Simple syntax that reads like English
- **Powerful Libraries**: Rich ecosystem of data analysis tools (pandas, numpy, matplotlib)
- **Versatile**: Can handle everything from simple scripts to complex data pipelines
- **Community**: Large, active community with extensive resources
- **Industry Standard**: Widely used in data science, finance, research, and tech companies

## Key Concepts

### Python as an Interpreted Language

Python is an **interpreted language**, meaning:
- Code is executed line by line
- No compilation step required
- You can run code immediately and see results
- Great for interactive data exploration

### Python Version

This course uses **Python 3.8+**. Python 3 is the current version and has many improvements over Python 2.

**Check your Python version:**
```python
import sys
print(sys.version)
# Should show Python 3.x.x
```

### Running Python Code

You can run Python code in several ways:

1. **Interactive Mode (REPL)**
   ```bash
   python
   # Or: python3
   ```
   Then type code directly:
   ```python
   >>> print("Hello, Python!")
   Hello, Python!
   ```

2. **Script Files**
   ```bash
   python my_script.py
   ```

3. **Jupyter Notebooks** (optional)
   - Interactive coding environment
   - Great for data analysis and visualization

## Python Syntax Basics

### General Rules

1. **Indentation Matters**
   - Python uses indentation (spaces/tabs) to define code blocks
   - Use 4 spaces (recommended) or tabs consistently
   ```python
   if True:
       print("This is indented")
       print("This too")
   ```

2. **Comments**
   - Use `#` for single-line comments
   - Use `"""` or `'''` for multi-line comments
   ```python
   # This is a single-line comment
   
   """
   This is a
   multi-line comment
   """
   ```

3. **Case Sensitive**
   - `name` and `Name` are different variables
   - Python keywords are lowercase

4. **No Semicolons Required**
   - Unlike some languages, Python doesn't require semicolons
   - Each statement typically goes on its own line

### Example Python Code Structure

```python
# Import libraries
import pandas as pd

# Define variables
name = "John"
age = 30

# Perform operations
result = age * 2

# Display output
print(f"Name: {name}, Double age: {result}")
```

## Python for Data Analysis Workflow

A typical data analysis workflow in Python:

1. **Load Data** - Read from CSV, database, API, etc.
2. **Explore Data** - Understand structure, check for issues
3. **Clean Data** - Handle missing values, fix errors
4. **Analyze Data** - Calculate statistics, find patterns
5. **Visualize Data** - Create charts and graphs
6. **Share Results** - Export reports, present findings

## Essential Libraries for Data Analysis

### pandas
- **Purpose**: Data manipulation and analysis
- **Use**: Reading CSV files, filtering data, grouping, merging
- **Import**: `import pandas as pd`

### numpy
- **Purpose**: Numerical computing
- **Use**: Mathematical operations, arrays, linear algebra
- **Import**: `import numpy as np`

### matplotlib
- **Purpose**: Data visualization
- **Use**: Creating charts, plots, graphs
- **Import**: `import matplotlib.pyplot as plt`

### seaborn
- **Purpose**: Statistical visualization
- **Use**: Advanced, beautiful plots
- **Import**: `import seaborn as sns`

We'll learn these libraries throughout the course!

## Your First Python Program

Let's write a simple program:

```python
# My first Python program
print("Hello, Python for Data Analysis!")

# Calculate something
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
print(f"The average is: {average}")
```

**Output:**
```
Hello, Python for Data Analysis!
The average is: 30.0
```

## Next Steps

In the next lesson, you'll learn about variables, data types, and basic operations - the building blocks of Python programming.

---

**Key Takeaways:**
- Python is a powerful, easy-to-learn language for data analysis
- Python 3.8+ is recommended for this course
- Indentation is crucial in Python
- Essential libraries: pandas, numpy, matplotlib, seaborn
- Python code is executed line by line (interpreted)
