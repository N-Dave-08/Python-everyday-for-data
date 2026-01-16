import pandas as pd

# Exercise 1: Basic Grouping
# Difficulty: Beginner

# Using employees.csv:

#   1. Group employees by department_id
#   2. Calculate the average salary for each department
#   3. Count the number of employees in each department
#   4. Find the highest salary in each department

# Expected Output Format:

# Average salary by department:
#   Department 1: $85000.00
#   Department 2: $71000.00
#   ...

# Employee count by department:
#   Department 1: 6
#   ...

# Highest salary by department:
#   Department 1: $95000.00
#   ...

df = pd.read_csv('data/datasets/employees.csv')

grouped = df.groupby('department_id')

avg_salary = grouped['salary'].mean()
print("Average salary by department: ")
for dept, salary in avg_salary.items():
    print(f"Department {dept}: ${salary}")

emp_count = grouped['employee_id'].sum()
print("\nEmployee count by department: ")
for dept, emp in emp_count.items():
    print(f"Department {dept}: {emp} employees")

dept_highest_salary = grouped['salary'].max()
print("\nHighest salary by department: ")
for dept, salary in dept_highest_salary.items():
    print(f"Department {dept}: ${salary}")

# =================================================================================

# Exercise 2: Multiple Aggregations
# Difficulty: Intermediate

# Using employees.csv:

#   1. Group by job_title
#   2. Calculate mean, min, max, and count of salaries for each job title
#   3. Display the results in a clear format

# Expected Output Format:

# Job Title Statistics:
#   Software Engineer:
#     Mean: $85750.00
#     Min: $82000.00
#     Max: $88000.00
#     Count: 4
#   ...

df = pd.read_csv('data/datasets/employees.csv')

grouped = df.groupby('job_title')
job_title_stats = df.groupby('job_title')['salary'].agg([
    'mean', 
    'min', 
    'max', 
    'count'
])

print("Job Title Statistics: ")

for job, row in job_title_stats.iterrows():
    print(f"\n {job}: ")
    print(f"    Mean: ${row['mean']}")
    print(f"    Min: ${row['min']}")
    print(f"    Max: ${row['max']}")
    print(f"    Count: {row['count']}")

# =================================================================================

# Exercise 3: Grouping by Multiple Columns
# Difficulty: Intermediate

# Using employees.csv:

#   1. Group by both department_id and job_title
#   2. Calculate the average salary for each combination
#   3. Count employees in each group

# Expected Output Format:

# Average salary by department and job:
#   Department 1, Software Engineer: $85000.00 (2 employees)
#   Department 2, Data Analyst: $71000.00 (3 employees)
#   ...

df = pd.read_csv('data/datasets/employees.csv')

dept_stats = df.groupby(['department_id', 'job_title']).agg({
    'salary': 'mean',
    'employee_id': 'sum'
})

print("Average salary by department and job: \n")

for (dept, job), row in dept_stats.iterrows():
    print(f"Department {dept}, {job}: ${row['salary']}")

# =================================================================================

# Exercise 4: Custom Aggregations
# Difficulty: Advanced

# Using employees.csv:

#   1. Create a function that calculates the salary range (max - min) for a group
#   2. Apply it to each department
#   3. Create a function that finds the median salary
#   4. Apply both functions using agg()

# Expected Output Format:

# Department Statistics:
#   Department 1:
#     Salary Range: $40000.00
#     Median Salary: $85000.00
#   ...

df = pd.read_csv('data/datasets/employees.csv')

def salary_range(group):
    return group.max() - group.min()

def salary_median(group):
    return group.median()

grouped = df.groupby('department_id')['salary'].agg([
    salary_range,
    salary_median
])

print("Department Statistics: ")

for dept, row in grouped.iterrows():
    print(f"Department{dept}: \nSalary Range: ${row['salary_range']} \nMedian Salary: ${row['salary_median']}\n")

# =================================================================================

# Exercise 5: Merging DataFrames
# Difficulty: Intermediate

#   1. Read employees.csv and departments.csv
#   2. Merge them on department_id using an inner join
#   3. Display employees with their department names
#   4. Show only: employee name, department name, and salary

# Expected Output Format:

# Employee - Department - Salary:
#   John Smith - Engineering - $85000.00
#   Alice Johnson - Data Science - $72000.00
#   ...

employees = pd.read_csv('data/datasets/employees.csv')
departments = pd.read_csv('data/datasets/departments.csv')

merged = pd.merge(
    employees,
    departments,
    on='department_id',
    how='inner'
)

merged['full_name'] = merged['first_name'] + ' ' + merged['last_name']

result = merged[['full_name', 'department_name', 'salary']]

print("Employee - Department - Salary:\n")

for _, row in merged.iterrows():
    print(f"{row['full_name']} - {row['department_name']} - ${row['salary']}")

# =================================================================================

# Exercise 6: Different Join Types
# Difficulty: Intermediate

#   1. Merge employees.csv and departments.csv using:
#       Inner join
#       Left join
#       Right join
#   2. Count how many rows each produces
#   3. Explain the difference

# Expected Output Format:

# Inner join: 15 rows
# Left join: 15 rows
# Right join: 15 rows
# (Actual numbers may vary based on data)

employees = pd.read_csv('data/datasets/employees.csv')
departments = pd.read_csv('data/datasets/departments.csv')

inner_join = pd.merge(
    employees,
    departments,
    on='department_id',
    how='inner'
)
print(f"Inner join: {inner_join.shape[0]} rows")
# inner join is returning data that are in both tables

left_join = pd.merge(
    employees,
    departments,
    on='department_id',
    how='left'
)
print(f"Left join: {left_join.shape[0]} rows")
# left join is returning data Nan if the right table has empty value for the reference

right_join = pd.merge(
    employees,
    departments,
    on='department_id',
    how='right'
)
print(f"Right join: {right_join.shape[0]} rows")
# right join is returning data Nan if the left table has empty value for the reference

# =================================================================================

# Exercise 7: Complex Merging
# Difficulty: Advanced

#   1. Read orders.csv and customers.csv
#   2. Merge them to show customer information with their orders
#   3. Calculate total order amount per customer
#   4. Find the customer with the most orders

# Expected Output Format:

# Total orders per customer:
#   Alice Adams: $1359.97 (3 orders)
#   Bob Baker: $29.99 (1 order)
#   ...

# Top customer: Alice Adams

customers = pd.read_csv('data/datasets/customers.csv')
orders = pd.read_csv('data/datasets/orders.csv')

merged = pd.merge(
    customers,
    orders,
    on='customer_id',
    how='left'
)

total_orders = (
    merged.groupby(['customer_id', 'first_name', 'last_name'])['total_amount']
    .sum()
    .reset_index() # reset_index() is needed to make new index, and not use customer_id, first_name, last_name as index
)

for _, row in total_orders.iterrows():
    print(f"{row['first_name']} {row['last_name']}: ${row['total_amount']}")

highest_order_amount = merged.iloc[total_orders['total_amount'].idxmax()]

print(f"\nTop customer: {highest_order_amount['first_name']} {highest_order_amount['last_name']}")

# =================================================================================

# Exercise 8: Pivot Tables
# Difficulty: Intermediate

# Using the merged employees-departments data:

#   1. Create a pivot table showing average salary by department and job title
#   2. Create a pivot table showing employee count by department and job title
#   3. Display both pivot tables

# Expected Output Format:

# Average Salary Pivot:
#                 Software Engineer  Data Analyst  ...
# Department 1        85000.00          ...
# Department 2         ...             71000.00
# ...

employees = pd.read_csv('data/datasets/employees.csv')
departments = pd.read_csv('data/datasets/departments.csv')

merged = pd.merge(
    employees,
    departments,
    on='department_id',
    how='inner'
)

avg_salary = pd.pivot_table(
    merged,
    values='salary',
    index=['department_name', 'job_title'],
    aggfunc='mean'
)
print("Average Salary Pivot: \n")
for dept, group in avg_salary.groupby('department_name'):
    print(f"{dept}:")
    for job, row in group.iterrows():
        print(f"    {job[1]}: ${row['salary']:.2f}")
    print()

emp_count = pd.pivot_table(
    merged,
    values='employee_id',
    index=['department_name', 'job_title'],
    aggfunc='count'
)
print("Employee Count Pivot: ")
for dept, group in emp_count.groupby('department_name'):
    print(f"{dept}:")
    for job, row in group.iterrows():
        print(f"    {job[1]}: {row['employee_id']} employees")
    print()


# =================================================================================

# Exercise 9: Transform Operations
# Difficulty: Advanced

# Using employees.csv:

#   1. Add a column showing each employee's salary as a percentage of their department's average
#   2. Add a column showing how many standard deviations each salary is from the department mean
#   3. Display the results

# Expected Output Format:

# Employee salary analysis:
#   John: $85000 (100% of dept avg, 0.0 std dev)
#   ...

employees = pd.read_csv('data/datasets/employees.csv')

dept_avg = employees.groupby('department_id')['salary'].mean()
employees['salary_percent'] = employees['salary'] / employees['department_id'].map(dept_avg) * 100

dept_stats = employees.groupby('department_id')['salary'].agg(['mean', 'std'])
employees['salary_zscore'] = (
    # (employee's salary - employee's department salary mean) / employee's department std
    (employees['salary'] - employees['department_id'].map(dept_stats['mean'])) /
    employees['department_id'].map(dept_stats['std'])
)


# =================================================================================

# Exercise 10: Comprehensive Analysis
# Difficulty: Advanced

# Create a comprehensive analysis:

#   1. Merge employees, departments, and sales data
#   2. Calculate total sales per employee
#   3. Calculate average sales per department
#   4. Find the top-performing employee in each department
#   5. Create a summary report

# Expected Output Format:

# Sales Analysis Report:
#   Total sales per employee:
#     John Smith: $2599.98
#     ...
  
#   Average sales by department:
#     Engineering: $1500.00
#     ...
  
#   Top performer per department:
#     Engineering: John Smith
#     ...

employees = pd.read_csv('data/datasets/employees.csv')
departments = pd.read_csv('data/datasets/departments.csv')
sales = pd.read_csv('data/datasets/sales.csv')

emp_sales = pd.merge(
    employees,
    sales,
    on='employee_id',
    how='left'
)

emp_total_sales = (
    emp_sales
    .groupby(['department_id', 'employee_id', 'first_name', 'last_name'])['total_amount']
    .sum()
    .reset_index()
)
emp_total_sales['full_name'] = emp_total_sales['first_name'] + ' ' + emp_total_sales['last_name']
print("\nTotal sales per employee: ")
for _, row in emp_total_sales.iterrows():
    print(f"{row['full_name']}: ${row['total_amount']:.2f}")

avg_dept_sales = emp_sales.groupby('department_id')['total_amount'].mean()
avg_dept_sales = avg_dept_sales.reset_index()
avg_dept_sales = pd.merge(
    avg_dept_sales,
    departments[['department_id', 'department_name']],
    on='department_id',
    how='left'
)
print("\nAverage sales by department: ")
for _, row in avg_dept_sales.iterrows():
    print(f"{row['department_name']}: ${row['total_amount']:.2f}")

emp_total_sales = emp_total_sales.reset_index()
emp_total_sales = pd.merge(
    emp_total_sales,
    departments[['department_id', 'department_name']],
    on='department_id',
    how='left'
)

top_emp = emp_total_sales.loc[
    emp_total_sales.groupby('department_id')['total_amount'].idxmax()
]
top_emp['full_name'] = top_emp['first_name'] + ' ' + top_emp['last_name']
print("\nTop performer per department: ")
for _, row in top_emp.iterrows():
    print(f"{row['department_name']}: {row['full_name']}")