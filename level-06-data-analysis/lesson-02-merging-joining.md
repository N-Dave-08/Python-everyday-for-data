# Lesson 6.2: Merging and Joining DataFrames

## Combining DataFrames

Often you need to combine data from multiple sources. Pandas provides several methods for this.

## Merge (SQL-like Joins)

### Inner Join

Returns only rows that have matching keys in both DataFrames:

```python
employees = pd.read_csv('data/datasets/employees.csv')
departments = pd.read_csv('data/datasets/departments.csv')

# Inner join
result = pd.merge(employees, departments, on='department_id', how='inner')
```

### Left Join

Returns all rows from left DataFrame, matching rows from right:

```python
# Left join
result = pd.merge(employees, departments, on='department_id', how='left')
```

### Right Join

Returns all rows from right DataFrame, matching rows from left:

```python
# Right join
result = pd.merge(employees, departments, on='department_id', how='right')
```

### Outer Join

Returns all rows from both DataFrames:

```python
# Outer join (full outer)
result = pd.merge(employees, departments, on='department_id', how='outer')
```

## Different Column Names

When joining columns have different names:

```python
# Specify left and right column names
result = pd.merge(
    employees,
    departments,
    left_on='department_id',
    right_on='department_id',
    how='inner'
)
```

## Concatenation

Combine DataFrames along an axis:

```python
# Vertical concatenation (stack rows)
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
result = pd.concat([df1, df2], ignore_index=True)

# Horizontal concatenation (stack columns)
result = pd.concat([df1, df2], axis=1)
```

## Join Method

Alternative syntax using the `join()` method:

```python
# Set index first
employees.set_index('department_id', inplace=True)
departments.set_index('department_id', inplace=True)

# Join
result = employees.join(departments, how='left')
```

## Handling Duplicate Column Names

When both DataFrames have columns with the same name:

```python
# Add suffixes
result = pd.merge(
    employees,
    departments,
    on='department_id',
    suffixes=('_emp', '_dept')
)
```

## Best Practices

1. **Use `merge()` for SQL-like joins**: Most flexible
2. **Use `concat()` for simple stacking**: When structure is similar
3. **Specify `how` parameter**: Be explicit about join type
4. **Handle duplicate columns**: Use suffixes when needed
5. **Check data before merging**: Verify keys match as expected

## Next Steps

You now know how to combine and analyze data! In the next level, you'll learn about data visualization to present your findings.

---

**Key Takeaways:**
- Use `merge()` for SQL-like joins (inner, left, right, outer)
- Use `concat()` to stack DataFrames vertically or horizontally
- Specify `on`, `left_on`, `right_on` for join keys
- Use `suffixes` to handle duplicate column names
- Choose the right join type based on your needs
