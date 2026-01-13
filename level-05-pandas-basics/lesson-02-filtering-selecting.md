# Lesson 5.2: Filtering and Selecting Data

## Boolean Indexing

Filter rows based on conditions using boolean indexing.

### Basic Filtering

```python
import pandas as pd

df = pd.read_csv('data/datasets/employees.csv')

# Filter rows where salary > 70000
high_salary = df[df['salary'] > 70000]
print(high_salary)

# Filter by string
engineers = df[df['job_title'] == 'Software Engineer']
print(engineers)
```

### Multiple Conditions

```python
# AND condition (use &)
high_salary_engineers = df[(df['salary'] > 70000) & (df['job_title'] == 'Software Engineer')]

# OR condition (use |)
high_salary_or_engineers = df[(df['salary'] > 70000) | (df['job_title'] == 'Software Engineer')]

# NOT condition (use ~)
not_engineers = df[~(df['job_title'] == 'Software Engineer')]
```

### Common Filtering Operations

```python
# Greater than
df[df['salary'] > 75000]

# Less than
df[df['age'] < 30]

# Equal to
df[df['department_id'] == 1]

# Not equal to
df[df['department_id'] != 1]

# Contains (for strings)
df[df['job_title'].str.contains('Engineer')]

# Is in list
df[df['department_id'].isin([1, 2, 3])]

# Is null
df[df['department_id'].isnull()]

# Not null
df[df['department_id'].notnull()]
```

## Selecting Specific Columns and Rows

### Selecting Columns

```python
# Single column
df['name']

# Multiple columns
df[['name', 'age', 'salary']]

# Columns by position
df.iloc[:, 0:3]  # First 3 columns
```

### Selecting Rows and Columns Together

```python
# By position
df.iloc[0:5, 0:3]  # First 5 rows, first 3 columns

# By label
df.loc[0:4, ['name', 'age']]  # Rows 0-4, specific columns
```

## String Operations

Pandas provides string methods for text data:

```python
# Contains
df[df['name'].str.contains('John')]

# Startswith
df[df['email'].str.startswith('john')]

# Endswith
df[df['email'].str.endswith('.com')]

# Case insensitive
df[df['name'].str.contains('john', case=False)]

# Length
df[df['name'].str.len() > 10]
```

## Sorting Data

```python
# Sort by single column
df.sort_values('salary')

# Sort descending
df.sort_values('salary', ascending=False)

# Sort by multiple columns
df.sort_values(['department_id', 'salary'], ascending=[True, False])

# Reset index after sorting
df.sort_values('salary').reset_index(drop=True)
```

## Adding and Modifying Columns

### Adding New Columns

```python
# Simple assignment
df['bonus'] = df['salary'] * 0.1

# Based on condition
df['high_earner'] = df['salary'] > 75000

# Using apply
df['name_length'] = df['name'].apply(len)
```

### Modifying Columns

```python
# Update values
df['salary'] = df['salary'] * 1.1  # 10% raise

# Conditional update
df.loc[df['department_id'] == 1, 'salary'] = df['salary'] * 1.05
```

## Dropping Columns and Rows

```python
# Drop columns
df.drop('column_name', axis=1)
df.drop(['col1', 'col2'], axis=1)

# Drop rows
df.drop(0)  # Drop row with index 0
df.drop([0, 1, 2])  # Drop multiple rows

# Drop with condition
df.drop(df[df['salary'] < 50000].index)
```

## Best Practices

1. **Use boolean indexing** for filtering
2. **Use `&` and `|`** for multiple conditions (not `and`/`or`)
3. **Use parentheses** around conditions when combining
4. **Use `.loc` and `.iloc`** for specific row/column selection
5. **Reset index** after filtering if needed

## Next Steps

In the next lesson, you'll learn about grouping and aggregations, which are essential for data analysis.

---

**Key Takeaways:**
- Use boolean indexing `df[df['column'] > value]` to filter rows
- Use `&` for AND, `|` for OR, `~` for NOT
- Use `.loc` for label-based selection, `.iloc` for position-based
- Use string methods like `.str.contains()` for text filtering
- Use `sort_values()` to sort dataframes
