import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Exercise 1: Basic Line Plot
# Difficulty: Beginner

# Using employees.csv:

# Create a line plot showing employee_id vs salary
# Add proper labels and title
# Add a grid
# Save the plot as 'salary_line.png'
# Expected Output: A line plot showing salary progression across employees.

employees = pd.read_csv('data/datasets/employees.csv')

plt.plot(employees['employee_id'], employees['salary'], label='Data')
plt.xlabel('Employee ID')
plt.ylabel('Salary')
plt.title('Employee ID vs Salary')
plt.grid(True)
plt.legend()
plt.savefig('level-07-data-visualization/salary_line.png')
plt.show()

# =================================================================================

# Exercise 2: Bar Chart
# Difficulty: Beginner

# Using employees.csv:

# Calculate average salary by department
# Create a bar chart showing this
# Add labels, title, and color the bars
# Rotate x-axis labels if needed
# Expected Output: A bar chart showing average salary for each department.

employees = pd.read_csv('data/datasets/employees.csv')
departments = pd.read_csv('data/datasets/departments.csv')

merged = employees.merge(
    departments,
    on='department_id',
    how='left'
)

dept_avg_salary = merged.groupby('department_name')['salary'].mean()

plt.bar(dept_avg_salary.index, dept_avg_salary.values, color='skyblue')
plt.xlabel('Department')
plt.ylabel('Salary')
plt.title('Average Salary by Department')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# =================================================================================

# Exercise 3: Scatter Plot
# Difficulty: Beginner

# Using employees.csv:

# Create a scatter plot of age vs salary
# Color points by department_id
# Add labels and title
# Add a legend
# Expected Output: A scatter plot showing relationship between age and salary, colored by department.

employees = pd.read_csv('data/datasets/employees.csv')
# add age column with random values ranges from 22 to 61
employees['age'] = np.random.randint(22, 61, size=len(employees))
employees.to_csv('data/datasets/employees.csv')

sns.scatterplot(data=employees, x='age', y='salary', hue='department_id')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Salary by Age')
plt.tight_layout()
plt.show()

# =================================================================================

# Exercise 4: Histogram
# Difficulty: Beginner

# Using employees.csv:

# Create a histogram of salary distribution
# Use 20 bins
# Add labels and title
# Add a vertical line for the mean salary
# Expected Output: A histogram showing salary distribution with mean line.

employees = pd.read_csv('data/datasets/employees.csv')

mean_salary = employees['salary'].mean()

sns.histplot(employees['salary'], bins=20, color='purple', kde=True)
plt.axvline(mean_salary, color='red', linestyle='--', label=f'Mean Salary: {mean_salary:.2f}')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.title('Salary Distribution of Employees')
plt.legend()
plt.tight_layout()
plt.show()

# =================================================================================

# Exercise 5: Multiple Subplots
# Difficulty: Intermediate

# Using employees.csv:

# Create a 2x2 subplot grid
# Plot 1: Salary histogram
# Plot 2: Age vs Salary scatter
# Plot 3: Average salary by department (bar)
# Plot 4: Salary box plot by department
# Add titles to each subplot
# Expected Output: A figure with 4 different visualizations.

employees = pd.read_csv('data/datasets/employees.csv')

fig, axes = plt.subplots(2, 2, figsize=(20, 10))

# Salary Histogram
axes[0, 0].hist(employees['salary'], bins=20, color='purple', alpha=0.7)
axes[0, 0].set_title('Salary Histogram')
axes[0, 0].set_xlabel('Salary')
axes[0, 0].set_ylabel('Frequency')

# Age vs Salary scatter
axes[0, 1].scatter(employees['age'], employees['salary'], color='red', alpha=0.6)
axes[0, 1].set_title('Age vs Salary')
axes[0, 1].set_xlabel('Age')
axes[0, 1].set_ylabel('Salary')

# Average salary by department (bar)
merged = employees.merge(
    departments,
    on='department_id',
    how='left'
)

dept_avg_salary = merged.groupby('department_name')['salary'].mean()

axes[1, 0].bar(dept_avg_salary.index, dept_avg_salary.values, color='skyblue')
axes[1, 0].tick_params(axis='x', rotation=45)
axes[1, 0].set_title('Average Salary by Department')
axes[1, 0].set_xlabel('Department')
axes[1, 0].set_ylabel('Average Salary')
axes[1, 0].tick_params(axis='x', rotation=45)

# Salary box plot by department
sns.boxplot(ax=axes[1, 1], x='department_name', y='salary', data=merged, palette='Set2')
axes[1, 1].set_title('Salary Distribution by department')
axes[1, 1].set_xlabel('Department')
axes[1, 1].set_ylabel('Salary')
axes[1, 1].tick_params(axis='x', rotation=45)

plt.show()

# =================================================================================

# Exercise 6: Seaborn Bar Plot
# Difficulty: Intermediate

# Using employees.csv:

# Use seaborn to create a bar plot of average salary by department
# Add error bars
# Customize colors
# Add proper labels and title
# Expected Output: A seaborn bar plot with error bars.

employees = pd.read_csv('data/datasets/employees.csv')

merged = employees.merge(
    departments,
    on='department_id',
    how='left'
)

dept_avg_salary = merged.groupby('department_name', as_index=False)['salary'].mean()

sns.barplot(
    data=dept_avg_salary, 
    x='department_name', 
    y='salary', 
    color='skyblue', 
    ci='sd'
)
plt.xlabel('Department Name')
plt.ylabel('Average Salary')
plt.title('Average Salary by Department') 
plt.tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.show()

# =================================================================================

# Exercise 7: Box Plot
# Difficulty: Intermediate

# Using employees.csv:

# Create a box plot showing salary distribution by department
# Use seaborn for better styling
# Add labels and title
# Identify outliers if any
# Expected Output: A box plot showing salary distributions by department.

employees = pd.read_csv('data/datasets/employees.csv')

merged = employees.merge(
    departments,
    on='department_id',
    how='left'
)

sns.boxplot(
    data=merged, 
    x='department_name', 
    y='salary',
    palette='Set2',
)
# swatmplot on top to see individual point
sns.swarmplot(
    data=merged,
    x='department_name', 
    y='salary',
    color='black',
    size=5
)

plt.xlabel('Department Name')
plt.ylabel('Salary')
plt.title('Salary Distribution by Department') 
plt.tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.show()

# =================================================================================

# Exercise 8: Heatmap
# Difficulty: Intermediate

# Using employees.csv:

# Select numerical columns (age, salary, etc.)
# Calculate correlation matrix
# Create a heatmap of correlations
# Add annotations showing correlation values
# Use a color scheme (coolwarm)
# Expected Output: A correlation heatmap showing relationships between numerical variables.

employees = pd.read_csv('data/datasets/employees.csv')

correlation = employees[['age', 'salary']].corr()

sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# =================================================================================

# Exercise 9: Advanced Visualization
# Difficulty: Advanced

# Using merged data from employees and departments:

# Create a grouped bar chart showing:
# Average salary by department
# Number of employees by department
# Use different colors for each metric
# Add a legend
# Make it publication-ready
# Expected Output: A grouped bar chart with multiple metrics.

employees = pd.read_csv('data/datasets/employees.csv')
departments = pd.read_csv('data/datasets/departments.csv')

merged = employees.merge(
    departments,
    on='department_id',
    how='left'
)

sns.barplot(
    data=merged,
    x='department_name',
    y='salary',
    hue='job_title',
    estimator='mean',
    ci='sd'
)
plt.title('Average Salary by Department and Job Title')
plt.xlabel('Department')
plt.ylabel('Salary')
plt.tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.show()

# =================================================================================

# Exercise 10: Comprehensive Dashboard
# Difficulty: Advanced

# Create a comprehensive visualization dashboard:

# Read employees and sales data
# Create a figure with multiple subplots:
# Sales over time (line plot)
# Top 5 products by sales (bar chart)
# Sales by region (pie chart or bar)
# Sales distribution (histogram)
# Add overall title
# Save as high-resolution image
# Expected Output: A comprehensive dashboard with multiple visualizations.

employees = pd.read_csv('data/datasets/employees.csv')
sales = pd.read_csv('data/datasets/sales.csv')
products = pd.read_csv('data/datasets/products.csv')


fig, axes = plt.subplots(2, 2, figsize=(20, 10))

# =================================================================================
# Sales over time (line plot)
# =================================================================================

emp_sales = employees.merge(
    sales,
    on='employee_id',
    how='left'
)

emp_sales['sale_date'] = pd.to_datetime(emp_sales['sale_date'])

sales_over_time = emp_sales.groupby('sale_date', as_index=False)['total_amount'].sum()

axes[0, 0].plot(sales_over_time['sale_date'], sales_over_time['total_amount'])
axes[0, 0].set_title('Total Sales Over Time')
axes[0, 0].set_xlabel('Date')
axes[0, 0].set_ylabel('Total Sales')

# =================================================================================
# Top 5 products by sales (bar chart)
# =================================================================================

emp_sales_product = emp_sales.merge(
    products,
    on='product_id',
    how='left'
)

top_products = (
    emp_sales_product.groupby('product_name')['total_amount']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
axes[0, 1].bar(top_products.index, top_products.values)
axes[0, 1].set_title('Top 5 Products by Sales')
axes[0, 1].set_xlabel('Product')
axes[0, 1].set_ylabel('Sales')
axes[0, 1].tick_params(axis='x', rotation=45)

# =================================================================================
# Sales by region (pie chart)
# =================================================================================

sales_by_region = emp_sales_product.groupby('region')['total_amount'].sum()

axes[1, 0].pie(
    sales_by_region.values,
    labels=sales_by_region.index,
    autopct='%1.1f%%',
    startangle=90
)
axes[1, 0].set_title('Sales by Region')

# =================================================================================
# Sales distribution (histogram)
# =================================================================================

axes[1, 1].hist(emp_sales_product['total_amount'], bins=20)
axes[1, 1].set_xlabel('Total Amount')
axes[1, 1].set_ylabel('Frequency')
axes[1, 1].set_title('Sales Distribution')

# =================================================================================
# Overall layout and save
# =================================================================================

plt.suptitle('Company Sales Dashboard', fontsize=18)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('level-07-data-visualization/sales_dashboard.png', dpi=300)

plt.show()