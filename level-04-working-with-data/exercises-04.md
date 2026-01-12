# Level 4 Exercises: Working with Data

Complete these exercises to practice file I/O, CSV, and JSON operations.

## Exercise 1: Reading Text Files
**Difficulty: Beginner**

Create a text file called `data.txt` with the following content:
```
Line 1
Line 2
Line 3
Line 4
Line 5
```

Write a Python program that:
1. Reads the file
2. Counts the total number of lines
3. Prints each line with its line number
4. Finds the longest line

**Expected Output Format:**
```
Total lines: 5
1: Line 1
2: Line 2
3: Line 3
4: Line 4
5: Line 5
Longest line: Line 1 (6 characters)
```

---

## Exercise 2: Writing to Files
**Difficulty: Beginner**

Write a Python program that:
1. Creates a list of 5 product names and prices
2. Writes them to a file called `products.txt` in the format:
   ```
   Product: Laptop, Price: $999.99
   Product: Mouse, Price: $29.99
   ...
   ```
3. Reads the file back and prints the content

**Expected Output Format:**
```
Product: Laptop, Price: $999.99
Product: Mouse, Price: $29.99
Product: Keyboard, Price: $89.99
Product: Monitor, Price: $349.99
Product: Headphones, Price: $149.99
```

---

## Exercise 3: CSV Reading (Built-in csv module)
**Difficulty: Intermediate**

Create a CSV file `employees.csv` with the following data:
```csv
name,age,department,salary
John,30,Engineering,85000
Alice,25,Marketing,65000
Bob,35,Sales,70000
```

Write a Python program using the `csv` module that:
1. Reads the CSV file
2. Calculates the average salary
3. Finds the employee with the highest salary
4. Counts employees by department

**Expected Output Format:**
```
Average salary: $73333.33
Highest paid: John ($85000)
Employees by department:
  Engineering: 1
  Marketing: 1
  Sales: 1
```

---

## Exercise 4: CSV Writing (Built-in csv module)
**Difficulty: Intermediate**

Write a Python program that:
1. Creates a list of dictionaries with product data:
   ```python
   products = [
       {"name": "Laptop", "price": 999.99, "stock": 25},
       {"name": "Mouse", "price": 29.99, "stock": 150},
       {"name": "Keyboard", "price": 89.99, "stock": 80}
   ]
   ```
2. Writes this data to a CSV file `products.csv`
3. Reads the file back and verifies the data

**Expected Output Format:**
```
CSV file created successfully!
Verification:
  Laptop: $999.99 (Stock: 25)
  Mouse: $29.99 (Stock: 150)
  Keyboard: $89.99 (Stock: 80)
```

---

## Exercise 5: Reading CSV with pandas
**Difficulty: Beginner**

Using the `employees.csv` file from Exercise 3, write a Python program using pandas that:
1. Reads the CSV file
2. Displays the first 3 rows
3. Shows basic information about the data
4. Calculates average age and salary

**Expected Output Format:**
```
First 3 rows:
   name  age    department  salary
0  John   30  Engineering   85000
1 Alice   25    Marketing   65000
2   Bob   35        Sales   70000

Average age: 30.0
Average salary: 73333.33
```

---

## Exercise 6: Filtering CSV Data with pandas
**Difficulty: Intermediate**

Using the `employees.csv` file, write a Python program that:
1. Reads the data with pandas
2. Filters employees with salary >= 70000
3. Filters employees in Engineering department
4. Creates a new CSV file with high-salary employees

**Expected Output Format:**
```
High salary employees (>=70000):
   name  age    department  salary
0  John   30  Engineering   85000
2   Bob   35        Sales   70000

Engineering employees:
   name  age    department  salary
0  John   30  Engineering   85000

Saved to high_salary_employees.csv
```

---

## Exercise 7: Working with JSON
**Difficulty: Intermediate**

Create a JSON file `data.json` with:
```json
{
  "employees": [
    {"name": "John", "age": 30, "department": "Engineering"},
    {"name": "Alice", "age": 25, "department": "Marketing"},
    {"name": "Bob", "age": 35, "department": "Sales"}
  ]
}
```

Write a Python program that:
1. Reads the JSON file
2. Prints all employee names
3. Calculates average age
4. Adds a new employee
5. Saves the updated data back to the file

**Expected Output Format:**
```
Employee names: ['John', 'Alice', 'Bob']
Average age: 30.0
Added new employee: Charlie
Updated data saved to data.json
```

---

## Exercise 8: Data Processing Pipeline
**Difficulty: Advanced**

Create a CSV file `sales.csv`:
```csv
product,quantity,price
Laptop,5,999.99
Mouse,20,29.99
Keyboard,10,89.99
```

Write a Python program that:
1. Reads the CSV with pandas
2. Calculates total revenue for each product (quantity * price)
3. Adds a new column "revenue" to the dataframe
4. Finds the product with highest revenue
5. Saves the updated data to `sales_with_revenue.csv`

**Expected Output Format:**
```
Product Revenue:
  Laptop: $4999.95
  Mouse: $599.80
  Keyboard: $899.90

Highest revenue product: Laptop ($4999.95)
Saved to sales_with_revenue.csv
```

---

## Exercise 9: Error Handling for Files
**Difficulty: Intermediate**

Write a Python program that:
1. Tries to read a file called `data.txt`
2. Handles `FileNotFoundError` gracefully
3. Handles `PermissionError` gracefully
4. If file doesn't exist, creates it with sample data
5. Then reads and displays the content

**Expected Output Format:**
```
File not found. Creating new file with sample data.
File created and read successfully:
Sample data line 1
Sample data line 2
```

---

## Exercise 10: Multiple File Operations
**Difficulty: Advanced**

Write a Python program that:
1. Reads data from `employees.csv` (from Exercise 3)
2. Groups employees by department
3. Creates separate CSV files for each department:
   - `engineering_employees.csv`
   - `marketing_employees.csv`
   - `sales_employees.csv`
4. Prints a summary of what was created

**Expected Output Format:**
```
Created department files:
  engineering_employees.csv: 1 employees
  marketing_employees.csv: 1 employees
  sales_employees.csv: 1 employees
```

---

## Hints

<details>
<summary>Hint for Exercise 1</summary>
Use `with open()` to read file, `readlines()` or iterate line by line, use `enumerate()` for line numbers, `len()` for line length.
</details>

<details>
<summary>Hint for Exercise 2</summary>
Create list of dictionaries, use `with open()` in write mode, format strings with f-strings, write each line.
</details>

<details>
<summary>Hint for Exercise 3</summary>
Use `csv.DictReader()` to read, iterate through rows, accumulate salary sum, track highest salary employee.
</details>

<details>
<summary>Hint for Exercise 4</summary>
Use `csv.DictWriter()` with fieldnames, call `writeheader()`, then `writerows()`.
</details>

<details>
<summary>Hint for Exercise 5</summary>
Use `pd.read_csv()`, `head()`, `info()`, and calculate mean of numeric columns.
</details>

<details>
<summary>Hint for Exercise 6</summary>
Use boolean indexing: `df[df['salary'] > 70000]`, filter by department, use `to_csv()` to save.
</details>

<details>
<summary>Hint for Exercise 7</summary>
Use `json.load()` to read, `json.dump()` to write, modify the dictionary, calculate statistics.
</details>

<details>
<summary>Hint for Exercise 8</summary>
Read CSV, create new column with calculation, find max, save to new file.
</details>

<details>
<summary>Hint for Exercise 9</summary>
Use try/except blocks, catch FileNotFoundError and PermissionError, create file if it doesn't exist.
</details>

<details>
<summary>Hint for Exercise 10</summary>
Read CSV, use `groupby()` or filter by department, save each group to separate file.
</details>

---

**Good luck!** Try to solve these without looking at the solutions first. If you get stuck, review the lessons or check the hints.
