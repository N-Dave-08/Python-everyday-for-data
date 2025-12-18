# Lesson 7.1: Introduction to Matplotlib

## What is Matplotlib?

**Matplotlib** is Python's primary plotting library. It creates static, animated, and interactive visualizations.

### Installing Matplotlib

```bash
pip install matplotlib
```

### Importing

```python
import matplotlib.pyplot as plt
```

## Basic Plotting

### Line Plot

```python
import matplotlib.pyplot as plt

# Simple line plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.show()
```

### Customizing Plots

```python
plt.plot(x, y, color='blue', linewidth=2, marker='o', label='Data')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.title('My Plot')
plt.legend()
plt.grid(True)
plt.show()
```

## Common Plot Types

### Scatter Plot

```python
plt.scatter(x, y, color='red', s=100, alpha=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot')
plt.show()
```

### Bar Chart

```python
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

plt.bar(categories, values, color='skyblue')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()
```

### Horizontal Bar Chart

```python
plt.barh(categories, values, color='lightgreen')
plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Horizontal Bar Chart')
plt.show()
```

### Histogram

```python
import numpy as np

data = np.random.normal(100, 15, 1000)
plt.hist(data, bins=30, color='purple', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
```

## Multiple Plots

### Subplots

```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].plot(x, y)
axes[0, 0].set_title('Line Plot')

axes[0, 1].scatter(x, y)
axes[0, 1].set_title('Scatter Plot')

axes[1, 0].bar(categories, values)
axes[1, 0].set_title('Bar Chart')

axes[1, 1].hist(data, bins=30)
axes[1, 1].set_title('Histogram')

plt.tight_layout()
plt.show()
```

## Plotting with Pandas

Pandas integrates with matplotlib:

```python
import pandas as pd

df = pd.read_csv('data/datasets/employees.csv')

# Plot directly from DataFrame
df['salary'].plot(kind='hist', bins=20)
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

# Line plot
df.plot(x='employee_id', y='salary', kind='line')
plt.show()

# Bar plot
df.groupby('department_id')['salary'].mean().plot(kind='bar')
plt.title('Average Salary by Department')
plt.ylabel('Average Salary')
plt.show()
```

## Styling

### Colors and Styles

```python
# Named colors
plt.plot(x, y, color='red')
plt.plot(x, y, color='blue', linestyle='--', linewidth=2)

# RGB colors
plt.plot(x, y, color=(0.2, 0.4, 0.6))

# Markers
plt.plot(x, y, marker='o', markersize=8, markerfacecolor='red')
```

### Figure Size

```python
plt.figure(figsize=(10, 6))  # Width, Height in inches
plt.plot(x, y)
plt.show()
```

## Saving Plots

```python
plt.plot(x, y)
plt.title('My Plot')
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.show()
```

## Best Practices

1. **Always label axes**: Use `xlabel()` and `ylabel()`
2. **Add titles**: Use `title()` for clarity
3. **Use legends**: When plotting multiple series
4. **Choose appropriate plot types**: Match data to visualization
5. **Save high-quality images**: Use `dpi=300` for publications

## Next Steps

In the next lesson, you'll learn about Seaborn, which provides more advanced and beautiful visualizations.

---

**Key Takeaways:**
- Use `plt.plot()` for line plots, `plt.scatter()` for scatter plots
- Use `plt.bar()` for bar charts, `plt.hist()` for histograms
- Always add labels, titles, and legends
- Use `plt.subplots()` for multiple plots
- Pandas DataFrames have built-in `.plot()` methods
- Save plots with `plt.savefig()`
