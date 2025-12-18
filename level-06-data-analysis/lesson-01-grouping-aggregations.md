# Lesson 6.1: Grouping and Aggregations

## GroupBy Operations

Grouping data is one of the most powerful features in pandas. It allows you to split data into groups and apply operations to each group.

### Basic GroupBy

```python
import pandas as pd

df = pd.read_csv('data/datasets/employees.csv')

# Group by department
grouped = df.groupby('department_id')

# Apply aggregation
avg_salary = grouped['salary'].mean()
print(avg_salary)
```

### Common Aggregations

```python
# Mean
df.groupby('department_id')['salary'].mean()

# Sum
df.groupby('department_id')['salary'].sum()

# Count
df.groupby('department_id')['salary'].count()

# Min/Max
df.groupby('department_id')['salary'].min()
df.groupby('department_id')['salary'].max()

# Standard deviation
df.groupby('department_id')['salary'].std()
```

### Multiple Aggregations

```python
# Using agg()
df.groupby('department_id')['salary'].agg(['mean', 'sum', 'count', 'min', 'max'])

# Custom aggregation names
df.groupby('department_id')['salary'].agg(
    avg_salary='mean',
    total_salary='sum',
    employee_count='count'
)
```

### Grouping by Multiple Columns

```python
# Group by multiple columns
df.groupby(['department_id', 'job_title'])['salary'].mean()

# Multiple aggregations on multiple columns
df.groupby('department_id').agg({
    'salary': ['mean', 'sum'],
    'age': 'mean'
})
```

## Aggregation Functions

### Built-in Aggregations

```python
# All at once
df.groupby('department_id').agg({
    'salary': 'mean',
    'age': ['mean', 'min', 'max'],
    'employee_id': 'count'
})
```

### Custom Aggregations

```python
# Define custom function
def salary_range(group):
    return group.max() - group.min()

df.groupby('department_id')['salary'].apply(salary_range)
```

## Transform and Apply

### Transform

Apply a function to each group and return a Series with the same index:

```python
# Normalize salary within each department
df['normalized_salary'] = df.groupby('department_id')['salary'].transform(
    lambda x: (x - x.mean()) / x.std()
)
```

### Apply

Apply a function to each group:

```python
# Custom function for each group
def top_earner(group):
    return group.nlargest(1)

df.groupby('department_id')['salary'].apply(top_earner)
```

## Pivot Tables

Pivot tables provide another way to aggregate data:

```python
# Create pivot table
pivot = df.pivot_table(
    values='salary',
    index='department_id',
    columns='job_title',
    aggfunc='mean'
)
print(pivot)
```

## Next Steps

In the next lesson, you'll learn about merging and joining DataFrames, which is essential for combining data from multiple sources.

---

**Key Takeaways:**
- Use `groupby()` to group data by one or more columns
- Apply aggregations like `mean()`, `sum()`, `count()`, `min()`, `max()`
- Use `agg()` for multiple aggregations at once
- Use `transform()` to apply functions that return same-sized results
- Use `apply()` for custom operations on groups
- Pivot tables provide an alternative way to aggregate data
