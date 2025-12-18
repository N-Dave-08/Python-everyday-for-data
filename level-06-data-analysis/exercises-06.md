# Level 6 Exercises: Data Analysis

Complete these exercises using grouping, aggregations, and merging operations.

## Exercise 1: Basic Grouping
**Difficulty: Beginner**

Using `employees.csv`:
1. Group employees by `department_id`
2. Calculate the average salary for each department
3. Count the number of employees in each department
4. Find the highest salary in each department

**Expected Output Format:**
```
Average salary by department:
  Department 1: $85000.00
  Department 2: $71000.00
  ...

Employee count by department:
  Department 1: 6
  ...

Highest salary by department:
  Department 1: $95000.00
  ...
```

---

## Exercise 2: Multiple Aggregations
**Difficulty: Intermediate**

Using `employees.csv`:
1. Group by `job_title`
2. Calculate mean, min, max, and count of salaries for each job title
3. Display the results in a clear format

**Expected Output Format:**
```
Job Title Statistics:
  Software Engineer:
    Mean: $85750.00
    Min: $82000.00
    Max: $88000.00
    Count: 4
  ...
```

---

## Exercise 3: Grouping by Multiple Columns
**Difficulty: Intermediate**

Using `employees.csv`:
1. Group by both `department_id` and `job_title`
2. Calculate the average salary for each combination
3. Count employees in each group

**Expected Output Format:**
```
Average salary by department and job:
  Department 1, Software Engineer: $85000.00 (2 employees)
  Department 2, Data Analyst: $71000.00 (3 employees)
  ...
```

---

## Exercise 4: Custom Aggregations
**Difficulty: Advanced**

Using `employees.csv`:
1. Create a function that calculates the salary range (max - min) for a group
2. Apply it to each department
3. Create a function that finds the median salary
4. Apply both functions using `agg()`

**Expected Output Format:**
```
Department Statistics:
  Department 1:
    Salary Range: $40000.00
    Median Salary: $85000.00
  ...
```

---

## Exercise 5: Merging DataFrames
**Difficulty: Intermediate**

1. Read `employees.csv` and `departments.csv`
2. Merge them on `department_id` using an inner join
3. Display employees with their department names
4. Show only: employee name, department name, and salary

**Expected Output Format:**
```
Employee - Department - Salary:
  John Smith - Engineering - $85000.00
  Alice Johnson - Data Science - $72000.00
  ...
```

---

## Exercise 6: Different Join Types
**Difficulty: Intermediate**

1. Merge `employees.csv` and `departments.csv` using:
   - Inner join
   - Left join
   - Right join
2. Count how many rows each produces
3. Explain the difference

**Expected Output Format:**
```
Inner join: 15 rows
Left join: 15 rows
Right join: 15 rows
(Actual numbers may vary based on data)
```

---

## Exercise 7: Complex Merging
**Difficulty: Advanced**

1. Read `orders.csv` and `customers.csv`
2. Merge them to show customer information with their orders
3. Calculate total order amount per customer
4. Find the customer with the most orders

**Expected Output Format:**
```
Total orders per customer:
  Alice Adams: $1359.97 (3 orders)
  Bob Baker: $29.99 (1 order)
  ...

Top customer: Alice Adams
```

---

## Exercise 8: Pivot Tables
**Difficulty: Intermediate**

Using the merged employees-departments data:
1. Create a pivot table showing average salary by department and job title
2. Create a pivot table showing employee count by department and job title
3. Display both pivot tables

**Expected Output Format:**
```
Average Salary Pivot:
                Software Engineer  Data Analyst  ...
Department 1        85000.00          ...
Department 2         ...             71000.00
...
```

---

## Exercise 9: Transform Operations
**Difficulty: Advanced**

Using `employees.csv`:
1. Add a column showing each employee's salary as a percentage of their department's average
2. Add a column showing how many standard deviations each salary is from the department mean
3. Display the results

**Expected Output Format:**
```
Employee salary analysis:
  John: $85000 (100% of dept avg, 0.0 std dev)
  ...
```

---

## Exercise 10: Comprehensive Analysis
**Difficulty: Advanced**

Create a comprehensive analysis:
1. Merge employees, departments, and sales data
2. Calculate total sales per employee
3. Calculate average sales per department
4. Find the top-performing employee in each department
5. Create a summary report

**Expected Output Format:**
```
Sales Analysis Report:
  Total sales per employee:
    John Smith: $2599.98
    ...
  
  Average sales by department:
    Engineering: $1500.00
    ...
  
  Top performer per department:
    Engineering: John Smith
    ...
```

---

## Hints

<details>
<summary>Hint for Exercise 1</summary>
Use `groupby('department_id')`, then apply `.mean()`, `.count()`, `.max()` on salary column.
</details>

<details>
<summary>Hint for Exercise 2</summary>
Use `groupby('job_title')['salary'].agg(['mean', 'min', 'max', 'count'])`.
</details>

<details>
<summary>Hint for Exercise 3</summary>
Use `groupby(['department_id', 'job_title'])` with multiple aggregations.
</details>

<details>
<summary>Hint for Exercise 4</summary>
Define functions, use `agg()` with dictionary mapping columns to functions.
</details>

<details>
<summary>Hint for Exercise 5</summary>
Use `pd.merge()` with `on='department_id'` and `how='inner'`, select specific columns.
</details>

<details>
<summary>Hint for Exercise 6</summary>
Try different `how` parameters: 'inner', 'left', 'right', 'outer', count rows with `len()`.
</details>

<details>
<summary>Hint for Exercise 7</summary>
Merge on customer_id, group by customer, sum order amounts, count orders.
</details>

<details>
<summary>Hint for Exercise 8</summary>
Use `pivot_table()` with `values`, `index`, `columns`, and `aggfunc` parameters.
</details>

<details>
<summary>Hint for Exercise 9</summary>
Use `transform()` with lambda functions to calculate percentages and z-scores.
</details>

<details>
<summary>Hint for Exercise 10</summary>
Merge multiple dataframes, group by employee and department, use multiple aggregations, find max per group.
</details>

---

**Good luck!** These exercises combine multiple concepts. Take your time and break them down into steps.
