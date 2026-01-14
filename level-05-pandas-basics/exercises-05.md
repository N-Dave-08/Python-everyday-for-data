# Level 5 Exercises: Pandas Basics

Complete these exercises using the datasets in `data/datasets/`. Make sure you've run `data/setup.py` first!

## Exercise 1: Reading and Exploring Data
**Difficulty: Beginner**

1. Read the `employees.csv` file
2. Display the first 5 rows
3. Display basic information about the dataframe
4. Display statistical summary
5. Print the shape of the dataframe

**Expected Output Format:**
```
First 5 rows:
   employee_id first_name last_name  ...
0            1       John     Smith  ...

Shape: (15, 9)
```

---

## Exercise 2: Selecting Columns
**Difficulty: Beginner**

Using the `employees.csv` file:
1. Select and display only the 'first_name', 'last_name', and 'salary' columns
2. Select and display only the 'email' column
3. Count how many employees there are

**Expected Output Format:**
```
Selected columns:
  first_name last_name  salary
0       John     Smith  85000.0
...

Total employees: 15
```

---

## Exercise 3: Basic Filtering
**Difficulty: Beginner**

Using the `employees.csv` file:
1. Find all employees with salary greater than 75000
2. Find all employees in department_id 1
3. Find all employees whose job_title is 'Software Engineer'

**Expected Output Format:**
```
High salary employees: 7 employees
Department 1 employees: 6 employees
Software Engineers: 3 employees
```

---

## Exercise 4: Multiple Conditions
**Difficulty: Intermediate**

Using the `employees.csv` file:
1. Find employees who are Software Engineers AND have salary > 70000
2. Find employees in department 1 OR department 2
3. Find employees whose salary is between 60000 and 80000 (inclusive)

**Expected Output Format:**
```
Software Engineers with high salary: 3 employees
Department 1 or 2: 9 employees
Salary between 60k-80k: 7 employees
```

---

## Exercise 5: String Operations
**Difficulty: Intermediate**

Using the `employees.csv` file:
1. Find all employees whose first_name starts with 'J'
2. Find all employees whose email contains 'company.com'
3. Create a new column 'full_name' that combines first_name and last_name

**Expected Output Format:**
```
Names starting with J: 3 employees
Emails with company.com: 15 employees
Full names created successfully
```

---

## Exercise 6: Sorting Data
**Difficulty: Beginner**

Using the `employees.csv` file:
1. Sort employees by salary in descending order
2. Sort employees by department_id, then by salary (descending)
3. Display the top 5 highest paid employees

**Expected Output Format:**
```
Top 5 highest paid:
  first_name  salary
    William  88000.0
    Richard  92000.0
    ...
```

---

## Exercise 7: Adding and Modifying Columns
**Difficulty: Intermediate**

Using the `employees.csv` file:
1. Add a new column 'annual_bonus' that is 10% of salary
2. Add a column 'high_earner' that is True if salary > 75000
3. Add a column 'name_length' with the length of first_name
4. Give all employees in department 1 a 5% salary increase

**Expected Output Format:**
```
Added columns: annual_bonus, high_earner, name_length
Updated salaries for department 1
```

---

## Exercise 8: Working with Missing Data
**Difficulty: Intermediate**

Using the `employees.csv` file:
1. Check which columns have missing values
2. Count how many missing values are in each column
3. Find all employees who don't have a department_id (is null)
4. Fill missing department_id with 0 (or handle appropriately)

**Expected Output Format:**
```
Missing values per column:
  department_id: 0
  ...

Employees without department: 0
```

---

## Exercise 9: Data Aggregation
**Difficulty: Intermediate**

Using the `employees.csv` file:
1. Calculate the average salary
2. Calculate the average salary by department
3. Find the highest and lowest salaries
4. Count employees by job_title

**Expected Output Format:**
```
Average salary: $75000.00
Average by department:
  Department 1: $85000.00
  ...

Highest: $95000.00, Lowest: $55000.00
Employees by job_title:
  Software Engineer: 4
  ...
```

---

## Exercise 10: Multiple DataFrames
**Difficulty: Advanced**

1. Read both `employees.csv` and `departments.csv`
2. Display information about both dataframes
3. Find the department name for each employee (you'll need to merge/join - we'll cover this in detail next level, but try using basic operations)
4. Calculate average salary by department name

**Expected Output Format:**
```
Employees: 15 rows
Departments: 5 rows
Average salary by department:
  Engineering: $85000.00
  ...
```

---

## Hints

<details>
<summary>Hint for Exercise 1</summary>
Use `pd.read_csv()`, `head()`, `info()`, `describe()`, and `shape`.
</details>

<details>
<summary>Hint for Exercise 2</summary>
Use `df[['col1', 'col2']]` for multiple columns, `df['col']` for single, `len(df)` for count.
</details>

<details>
<summary>Hint for Exercise 3</summary>
Use boolean indexing: `df[df['salary'] > 75000]`, `df[df['department_id'] == 1]`.
</details>

<details>
<summary>Hint for Exercise 4</summary>
Use `&` for AND, `|` for OR, combine conditions with parentheses. For range, use `(df['col'] >= min) & (df['col'] <= max)`.
</details>

<details>
<summary>Hint for Exercise 5</summary>
Use `.str.startswith()`, `.str.contains()`, and create new column with `df['new_col'] = df['col1'] + ' ' + df['col2']`.
</details>

<details>
<summary>Hint for Exercise 6</summary>
Use `sort_values()` with `ascending=False`, multiple columns in list, `head(5)` for top 5.
</details>

<details>
<summary>Hint for Exercise 7</summary>
Create columns with `df['new'] = ...`, use boolean for conditions, use `.apply()` or `.str.len()` for length.
</details>

<details>
<summary>Hint for Exercise 8</summary>
Use `isnull()`, `sum()` to count, filter with `isnull()`, use `fillna()` to fill.
</details>

<details>
<summary>Hint for Exercise 9</summary>
Use `mean()`, `groupby()` then `mean()`, `max()` and `min()`, `value_counts()` for counting.
</details>

<details>
<summary>Hint for Exercise 10</summary>
Read both files, use `merge()` or join operations (we'll cover this next level, but you can try basic matching).
</details>

---

**Good luck!** Try to solve these without looking at the solutions first. If you get stuck, review the lessons or check the hints.
