# Lesson 7.2: Advanced Visualization with Seaborn

## What is Seaborn?

**Seaborn** is a statistical visualization library built on matplotlib. It provides beautiful, high-level plots with less code.

### Installing Seaborn

```bash
pip install seaborn
```

### Importing

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

## Styling

```python
# Set style
sns.set_style("whitegrid")
sns.set_palette("husl")

# Create plot
sns.scatterplot(data=df, x='age', y='salary')
plt.show()
```

## Common Seaborn Plots

### Scatter Plot

```python
sns.scatterplot(data=df, x='age', y='salary', hue='department_id')
plt.title('Salary vs Age by Department')
plt.show()
```

### Line Plot

```python
sns.lineplot(data=df, x='employee_id', y='salary', hue='department_id')
plt.show()
```

### Bar Plot

```python
sns.barplot(data=df, x='department_id', y='salary')
plt.title('Average Salary by Department')
plt.show()
```

### Box Plot

```python
sns.boxplot(data=df, x='department_id', y='salary')
plt.title('Salary Distribution by Department')
plt.show()
```

### Violin Plot

```python
sns.violinplot(data=df, x='department_id', y='salary')
plt.show()
```

### Heatmap

```python
# Create correlation matrix
correlation = df[['age', 'salary']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
```

### Pair Plot

```python
# Plot relationships between multiple variables
sns.pairplot(df[['age', 'salary', 'department_id']], hue='department_id')
plt.show()
```

## Advanced Features

### Faceting

```python
# Create multiple plots based on categories
g = sns.FacetGrid(df, col='department_id')
g.map(plt.scatter, 'age', 'salary')
plt.show()
```

### Distribution Plots

```python
# Histogram with density curve
sns.histplot(data=df, x='salary', kde=True, bins=20)
plt.show()

# Distribution plot
sns.displot(data=df, x='salary', kind='kde', hue='department_id')
plt.show()
```

## Best Practices

1. **Use Seaborn for statistical plots**: Box plots, violin plots, etc.
2. **Use color palettes**: `sns.set_palette()` for consistent colors
3. **Combine with matplotlib**: Use `plt` for additional customization
4. **Use `hue` parameter**: To add categorical dimensions
5. **Save figures**: Use `plt.savefig()` with high DPI

## Next Steps

You now know how to create visualizations! In the final level, you'll learn about advanced topics like APIs, web scraping, and machine learning basics.

---

**Key Takeaways:**
- Seaborn provides beautiful statistical visualizations
- Use `sns.scatterplot()`, `sns.barplot()`, `sns.boxplot()` for common plots
- Use `hue` parameter to add categorical dimensions
- Heatmaps are great for correlation matrices
- Pair plots show relationships between multiple variables
- Combine Seaborn with matplotlib for full control
