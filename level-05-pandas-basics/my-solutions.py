import pandas as pd

# Exercise 1: Reading and Exploring Data
# Difficulty: Beginner

#   1. Read the employees.csv file
#   2. Display the first 5 rows
#   3. Display basic information about the dataframe
#   4. Display statistical summary
#   5. Print the shape of the dataframe

# Expected Output Format:

# First 5 rows:
#    employee_id first_name last_name  ...
# 0            1       John     Smith  ...

# Shape: (15, 9)

df = pd.read_csv('data/datasets/employees.csv')

first_five = df.head(5)
print("First 5 rows: ")
print(first_five)

print(f"\nBasic Information: ")
print(df.info())

print(f"\nStatistical Summary: ")
print(df.describe())

print(f"\nShape: {df.shape}")

# =================================================================================

# Exercise 2: Selecting Columns
# Difficulty: Beginner

# Using the employees.csv file:

#   1. Select and display only the 'first_name', 'last_name', and 'salary' columns
#   2. Select and display only the 'email' column
#   3. Count how many employees there are

# Expected Output Format:

# Selected columns:
#   first_name last_name  salary
# 0       John     Smith  85000.0
# ...

# Total employees: 15

df = pd.read_csv('data/datasets/employees.csv')

full_name_salary = df[['first_name', 'last_name', 'salary']]
print("First Name, Last Name, Salary: ")
print(full_name_salary)

emails = df['email']
print("\nEmails Only: ")
print(emails)

total_emps = len(df)
print(f"\nTotal employees: {total_emps}")

# =================================================================================

# Exercise 3: Basic Filtering
# Difficulty: Beginner

# Using the employees.csv file:

#   1. Find all employees with salary greater than 75000
#   2. Find all employees in department_id 1
#   3. Find all employees whose job_title is 'Software Engineer'

# Expected Output Format:

#   High salary employees: 7 employees
#   Department 1 employees: 6 employees
#   Software Engineers: 4 employees

df = pd.read_csv('data/datasets/employees.csv')

high_salary = df[df['salary'] > 75000]
total_high_salary_emps = len(high_salary)
print(f"High salary employees: {total_high_salary_emps} employees")

dept1_emp = df[df['department_id'] == 1]
total_dept1_emps = len(dept1_emp)
print(f"Department 1 employees: {total_dept1_emps} employees")

soft_eng = df[df['job_title'] == 'Software Engineer']
total_soft_engs = len(soft_eng)
print(f"Software Engineers: {total_soft_engs} employees")

# =================================================================================

# Exercise 4: Multiple Conditions
# Difficulty: Intermediate

# Using the employees.csv file:

# Find employees who are Software Engineers AND have salary > 70000
# Find employees in department 1 OR department 2
# Find employees whose salary is between 60000 and 80000 (inclusive)
# Expected Output Format:

# Software Engineers with high salary: 3 employees
# Department 1 or 2: 9 employees
# Salary between 60k-80k: 7 employees

df = pd.read_csv('data/datasets/employees.csv')

high_salary_soft_eng = df[
    (df['job_title'] == 'Software Engineer') & (df['salary'] > 70000)
]
total_high_salary_soft_eng = len(high_salary_soft_eng)
print(f"Software Engineers with high salary: {total_high_salary_soft_eng} employees")

dept1_and_dept2_emp = df[
    (df['department_id'] == 1) | (df['department_id'] == 2)
]
total_dept1_and_dept2_emp = len(dept1_and_dept2_emp)
print(f"Department 1 or 2: {total_dept1_and_dept2_emp} employees")

mid_salary = df[
    (df['salary'] > 60000) & (df['salary'] > 80000)
]
total_mid_salary = len(mid_salary)
print(f"Salary between 60k-80k: {total_mid_salary} employees")

# =================================================================================

# Exercise 5: String Operations
# Difficulty: Intermediate

# Using the employees.csv file:

#   1. Find all employees whose first_name starts with 'J'
#   2. Find all employees whose email contains 'company.com'
#   3. Create a new column 'full_name' that combines first_name and last_name

# Expected Output Format:

#   Names starting with J: 3 employees
#   Emails with company.com: 15 employees
#   Full names created successfully

df = pd.read_csv('data/datasets/employees.csv')

j_names = df[df['first_name'].str.startswith('J')]
total_j_names = len(j_names)
print(f"Names starting with J: {total_j_names} employees")

company_emails = df[df['email'].str.contains('company.com')]
total_company_emails = len(company_emails)
print(f"Emails with company.com: {total_company_emails} employees")

df['full_name'] = df['first_name'] + " " + df['last_name']
print("Full names created successfully")

# =================================================================================

# Exercise 6: Sorting Data
# Difficulty: Beginner

# Using the employees.csv file:

#   1. Sort employees by salary in descending order
#   2. Sort employees by department_id, then by salary (descending)
#   3. Display the top 5 highest paid employees

# Expected Output Format:

# Top 5 highest paid:
#   first_name  salary
#     William  88000.0
#     Richard  92000.0
#     ...

df = pd.read_csv('data/datasets/employees.csv')

desc_salary = df.sort_values('salary', ascending=False)
sort_by_dept_salary_desc = df.sort_values(by=['department_id', 'salary'], ascending=[True, False])

df['full_name'] = df['first_name'] + " " + df['last_name']
print(f"Top 5 highest paid: ")
print(desc_salary[['full_name', 'salary']].head(5))


# =================================================================================

# Exercise 7: Adding and Modifying Columns

# Difficulty: Intermediate

# Using the employees.csv file:

#   1. Add a new column 'annual_bonus' that is 10% of salary
#   2. Add a column 'high_earner' that is True if salary > 75000
#   3. Add a column 'name_length' with the length of first_name
#   4. Give all employees in department 1 a 5% salary increase

# Expected Output Format:

#   Added columns: annual_bonus, high_earner, name_length
#   Updated salaries for department 1

df = pd.read_csv('data/datasets/employees.csv')

df['annual_bonus'] = df['salary'] * 0.1
df['high_earner'] = df['salary'] > 75000
df['name_length'] = len(df['first_name'])
print(f"Added columns: annual_bonus, high_earner, name_length")

df.loc[df['department_id'] == 1, 'salary'] = df.loc[df['department_id'] == 1, 'salary'] * 1.05
print("Updated salaries for department 1")

# =================================================================================

# Exercise 8: Working with Missing Data
# Difficulty: Intermediate

# Using the employees.csv file:

#   1. Check which columns have missing values
#   2. Count how many missing values are in each column
#   3. Find all employees who don't have a department_id (is null)
#   4. Fill missing department_id with 0 (or handle appropriately)

# Expected Output Format:

# Missing values per column:
#   department_id: 0
#   ...

# Employees without department: 0

df = pd.read_csv('data/datasets/employees.csv')

# number of missing values per column
df.isnull().sum()

df['department_id'] = df['department_id'].fillna(0)

print("Missing values per column: ")
print(df.isnull().sum())

# =================================================================================

# Exercise 9: Data Aggregation
# Difficulty: Intermediate

# Using the employees.csv file:

#   1. Calculate the average salary
#   2. Calculate the average salary by department
#   3. Find the highest and lowest salaries
#   4. Count employees by job_title

# Expected Output Format:

# Average salary: $75000.00
# Average by department:
#   Department 1: $85000.00
#   ...

# Highest: $95000.00, Lowest: $55000.00
# Employees by job_title:
#   Software Engineer: 4
#   ...

df = pd.read_csv('data/datasets/employees.csv')

avg_salary = sum(df['salary']) / len(df['salary'])
print(f"Average salary: {avg_salary}")

dept_avg_salary = df.groupby('department_id')['salary'].mean()
print("\nAverage by department: ")
print(dept_avg_salary)

highest_salary = df.loc[df['salary'].idxmax()]
lowest_salary = df.loc[df['salary'].idxmin()]
print(f"\nHighest: ${highest_salary['salary']}, Lowest: ${lowest_salary['salary']}")

count_job_title = df.groupby('job_title').size()
print("\nEmployees by job_title: ")
print(count_job_title)

# =================================================================================

# Exercise 10: Multiple DataFrames
# Difficulty: Advanced

# 1. Read both employees.csv and departments.csv
# 2. Display information about both dataframes
# 3. Find the department name for each employee (you'll need to merge/join - we'll cover this in detail next level, but try using basic operations)
# 4. Calculate average salary by department name

# Expected Output Format:

# Employees: 15 rows
# Departments: 5 rows
# Average salary by department:
#   Engineering: $85000.00
#   ...

employees_df = pd.read_csv('data/datasets/employees.csv')
departments_df = pd.read_csv('data/datasets/departments.csv')

employees_df.info()
departments_df.info()

merged_df = pd.merge(
    employees_df,
    departments_df,
    on='department_id',
    how='left'
)

merged_df[['department_name', 'first_name']]

print(f"Employees: {len(employees_df)}")
print(f"Departments: {len(departments_df)} \n")

dept_avg_salary = merged_df.groupby('department_name')['salary'].mean()
for dept, salary in dept_avg_salary.items():
    print(f"{dept}: ${salary}")