# Lesson 5.1: Introduction to Pandas

## What is Pandas?

**Pandas** is the most powerful Python library for data manipulation and analysis. It provides data structures and tools for working with structured data, similar to Excel or SQL.

### Why Pandas?

- **Easy data manipulation**: Filter, sort, group, merge data easily
- **Handles missing data**: Built-in support for NaN values
- **Time series support**: Great for date/time data
- **Fast and efficient**: Built on NumPy for performance
- **Excel-like operations**: Familiar if you know spreadsheets

## Installing Pandas

```bash
pip install pandas
```

## Importing Pandas

```python
import pandas as pd
```

The convention is to import pandas as `pd` for brevity.

## Core Data Structures

### Series

A **Series** is a one-dimensional array with labels (like a column in Excel):

```python
import pandas as pd

# Create Series from list
s = pd.Series([1, 2, 3, 4, 5])
print(s)

# With custom index
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)
```

### DataFrame

A **DataFrame** is a two-dimensional table (like a spreadsheet):

```python
# Create DataFrame from dictionary
data = {
    'name': ['John', 'Alice', 'Bob'],
    'age': [30, 25, 35],
    'city': ['New York', 'Boston', 'Chicago']
}
df = pd.DataFrame(data)
print(df)
```

## Reading Data

### Reading CSV Files

```python
# Read CSV file
df = pd.read_csv('data/datasets/employees.csv')

# Display first few rows
print(df.head())

# Display last few rows
print(df.tail())
```

### Reading Other Formats

```python
# Excel
df = pd.read_excel('data.xlsx')

# JSON
df = pd.read_json('data.json')

# SQL (requires sqlalchemy)
df = pd.read_sql('SELECT * FROM table', connection)
```

## Basic DataFrame Operations

### Viewing Data

```python
# First 5 rows (default)
df.head()

# First 10 rows
df.head(10)

# Last 5 rows
df.tail()

# Shape (rows, columns)
df.shape  # (15, 9) means 15 rows, 9 columns

# Column names
df.columns

# Data types
df.dtypes

# Basic info
df.info()

# Statistical summary
df.describe()
```

### Selecting Columns

```python
# Single column (returns Series)
df['name']

# Multiple columns (returns DataFrame)
df[['name', 'age']]

# Using dot notation (only if column name is valid Python identifier)
df.name  # Same as df['name']
```

### Selecting Rows

```python
# By index
df.iloc[0]      # First row
df.iloc[0:3]    # First 3 rows
df.iloc[0, 1]   # First row, second column

# By label
df.loc[0]       # Row with index 0
df.loc[0:2]     # Rows 0 to 2 (inclusive)
```

## Basic Data Exploration

### Summary Statistics

```python
# Numerical columns summary
df.describe()

# Count non-null values
df.count()

# Mean, median, std for numerical columns
df.mean()
df.median()
df.std()
```

### Data Types

```python
# Check data types
df.dtypes

# Convert data types
df['age'] = df['age'].astype(int)
df['salary'] = df['salary'].astype(float)
```

## Working with Missing Data

```python
# Check for missing values
df.isnull()
df.isnull().sum()  # Count missing per column

# Drop rows with missing values
df.dropna()

# Fill missing values
df.fillna(0)  # Fill with 0
df['column'].fillna(df['column'].mean())  # Fill with mean
```

## Next Steps

In the next lesson, you'll learn about filtering and selecting data, which is essential for data analysis.

---

**Key Takeaways:**
- Pandas provides Series (1D) and DataFrame (2D) data structures
- Use `pd.read_csv()` to read CSV files
- Use `head()`, `tail()`, `info()`, `describe()` to explore data
- Select columns with `df['column']` or `df[['col1', 'col2']]`
- Use `isnull()` and `fillna()` to handle missing data
