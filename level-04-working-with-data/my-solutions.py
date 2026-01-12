import csv
import pandas as pd
import json

# Exercise 1: Reading Text Files
# Difficulty: Beginner

# Create a text file called data.txt with the following content:

# Line 1
# Line 2
# Line 3
# Line 4
# Line 5

# Write a Python program that:

#   1. Reads the file
#   2. Counts the total number of lines
#   3. Prints each line with its line number
#   4. Finds the longest line

# Expected Output Format:

#   Total lines: 5
#   1: Line 1
#   2: Line 2
#   3: Line 3
#   4: Line 4
#   5: Line 5
#   Longest line: Line 1 (6 characters)

# read the file
with open("level-04-working-with-data/data.txt", "r") as file:
    content = file.read()

# read all lines in the file and make it a list
with open("level-04-working-with-data/data.txt", "r") as file:
    lines = file.readlines()

total_lines = len(lines)
print(f"Total Lines: {total_lines}")

with open("level-04-working-with-data/data.txt", "r") as file:
    # run through every line and put a number by using enumerate
    for line_number, line in enumerate(file, start=1):
        print(f"{line_number}: {line.rstrip()}")

with open("level-04-working-with-data/data.txt", "r") as file:
    # get the max value base on the length of the lines and remove the \n
    longest_line = max(file, key=len).rstrip()

chars = len(longest_line)
print(f"Longest Line: {longest_line} ({chars} characters)")


# =================================================================================

# Exercise 2: Writing to Files
# Difficulty: Beginner

# Write a Python program that:

#   1. Creates a list of 5 product names and prices
#   2. Writes them to a file called products.txt in the format:
#       Product: Laptop, Price: $999.99
#       Product: Mouse, Price: $29.99
#       ...
#   3. Reads the file back and prints the content

# Expected Output Format:

#   Product: Laptop, Price: $999.99
#   Product: Mouse, Price: $29.99
#   Product: Keyboard, Price: $89.99
#   Product: Monitor, Price: $349.99
#   Product: Headphones, Price: $149.99

with open("level-04-working-with-data/products.txt", "r") as file:
    content = file.read()
    print(content)

# =================================================================================

# Exercise 3: CSV Reading (Built-in csv module)
# Difficulty: Intermediate

# Create a CSV file employees.csv with the following data:

# name,age,department,salary
# John,30,Engineering,85000
# Alice,25,Marketing,65000
# Bob,35,Sales,70000

# Write a Python program using the csv module that:

#   1. Reads the CSV file
#   2. Calculates the average salary
#   3. Finds the employee with the highest salary
#   4. Counts employees by department

# Expected Output Format:

# Average salary: $73333.33
# Highest paid: John ($85000)
# Employees by department:
#   Engineering: 1
#   Marketing: 1
#   Sales: 1

salaries = []
employees = []

with open("level-04-working-with-data/employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        salaries.append(int(row["salary"]))
        employees.append(row)

avg_salary = sum(salaries) / len(salaries)

highest_salary = max(employees, key=lambda x: int(x["salary"]))

dept_count = {}

for emp in employees:
    dept = emp["department"]
    if dept not in dept_count:
        dept_count[dept] = 1
    else:
        dept_count[dept] += 1

print(f"Average salary: ${avg_salary}")
print(f"Highest paid: {highest_salary['name']} (${highest_salary['salary']})")
print(f"Employee by department:")
for dept, count in dept_count.items():
    print(f" {dept}: {count}")

# =================================================================================

# Exercise 4: CSV Writing (Built-in csv module)
# Difficulty: Intermediate

# Write a Python program that:

#   1. Creates a list of dictionaries with product data:
#       products = [
#           {"name": "Laptop", "price": 999.99, "stock": 25},
#           {"name": "Mouse", "price": 29.99, "stock": 150},
#           {"name": "Keyboard", "price": 89.99, "stock": 80}
#       ]
#   2. Writes this data to a CSV file products.csv
#   3. Reads the file back and verifies the data

# Expected Output Format:

# CSV file created successfully!
# Verification:
#   Laptop: $999.99 (Stock: 25)
#   Mouse: $29.99 (Stock: 150)
#   Keyboard: $89.99 (Stock: 80)

products = [
    {"name": "Laptop", "price": 999.99, "stock": 25},
    {"name": "Mouse", "price": 29.99, "stock": 150},
    {"name": "Keyboard", "price": 89.99, "stock": 80}
]

with open("level-04-working-with-data/products.csv", "w", newline="") as file:
    fieldnames = ["name", "price", "stock"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products)

# =================================================================================

# Exercise 5: Reading CSV with pandas
# Difficulty: Beginner

# Using the employees.csv file from Exercise 3, write a Python program using pandas that:

# 1. Reads the CSV file
# 2. Displays the first 3 rows
# 3. Shows basic information about the data
# 4. Calculates average age and salary

# Expected Output Format:

# First 3 rows:
#    name  age    department  salary
# 0  John   30  Engineering   85000
# 1 Alice   25    Marketing   65000
# 2   Bob   35        Sales   70000

# Average age: 30.0
# Average salary: 73333.33

df = pd.read_csv("level-04-working-with-data/employees.csv")

first_three = df.head(3)

total_age = df["age"].sum()
avg_age = total_age / len(df["age"])

total_salary = df["salary"].sum()
avg_salary = total_salary / len(df["salary"])

print(f"First 3 rows:\n {first_three}")
print(f"Average age: {avg_age}")
print(f"Average salary: {avg_salary}")

# =================================================================================

# Exercise 6: Filtering CSV Data with pandas
# Difficulty: Intermediate

# Using the employees.csv file, write a Python program that:

#   1. Reads the data with pandas
#   2. Filters employees with salary > 70000
#   3. Filters employees in Engineering department
#   4. Creates a new CSV file with high-salary employees

# Expected Output Format:

# High salary employees (>70000):
#    name  age    department  salary
# 0  John   30  Engineering   85000
# 2   Bob   35        Sales   70000

# Engineering employees:
#    name  age    department  salary
# 0  John   30  Engineering   85000

# Saved to high_salary_employees.csv

df = pd.read_csv("level-04-working-with-data/employees.csv")
high_salaries = df[df["salary"].astype(int) >= 70000]

eng_emps = df[df["department"] == "Engineering"]

print("High salary employees (>=70000): \n")
print(high_salaries)

print("Engineering employees: \n")
print(eng_emps)

high_salaries.to_csv("level-04-working-with-data/high_salary_employees.csv", index=False)
print("\nSaved to high_salary_employees.csv")

# =================================================================================

# Exercise 7: Working with JSON
# Difficulty: Intermediate

# Create a JSON file data.json with:

# {
#   "employees": [
#     {"name": "John", "age": 30, "department": "Engineering"},
#     {"name": "Alice", "age": 25, "department": "Marketing"},
#     {"name": "Bob", "age": 35, "department": "Sales"}
#   ]
# }

# Write a Python program that:

#   1. Reads the JSON file
#   2. Prints all employee names
#   3. Calculates average age
#   4. Adds a new employee
#   5. Saves the updated data back to the file

# Expected Output Format:

# Employee names: ['John', 'Alice', 'Bob']
# Average age: 30.0
# Added new employee: Charlie
# Updated data saved to data.json

with open("level-04-working-with-data/data.json", "r") as file:
    data = json.load(file)

names = [emp["name"] for emp in data["employees"]]
print(f"Employee names: {names}")

ages = [emp["age"] for emp in data["employees"]]
avg_age = sum(ages) / len(ages)
print(f"Average age: {avg_age}")

new_employee = {
    "name": "Charlie",
    "age": 25,
    "department": "HR"
}

if new_employee["name"] not in names:
    data["employees"].append(new_employee)
    print("Added new employee: Charlie")
else:
    print("Charlie already exist")

with open("level-04-working-with-data/data.json", "w") as file:
    json.dump(data, file, indent=2)
    print("Updated data saved to data.json")

# =================================================================================

# Exercise 8: Data Processing Pipeline
# Difficulty: Advanced

# Create a CSV file sales.csv:

# product,quantity,price
# Laptop,5,999.99
# Mouse,20,29.99
# Keyboard,10,89.99

# Write a Python program that:

#   1. Reads the CSV with pandas
#   2. Calculates total revenue for each product (quantity * price)
#   3. Adds a new column "revenue" to the dataframe
#   4. Finds the product with highest revenue
#   5. Saves the updated data to sales_with_revenue.csv

# Expected Output Format:

# Product Revenue:
#   Laptop: $4999.95
#   Mouse: $599.80
#   Keyboard: $899.90

# Highest revenue product: Laptop ($4999.95)
# Saved to sales_with_revenue.csv

df = pd.read_csv("level-04-working-with-data/sales.csv")

df["revenue"] = df["quantity"] * df["price"]
print("Product Revenue: ")

# pairs the product to its revenue
for prod, revenue in zip(df["product"], df["revenue"]):
    print(f"    {prod}: ${revenue:.2f}")

# find the row index of the max revenue
idx = df["revenue"].idxmax()

# use the idx as a locator for the highest revenue product
highest_revenue_prod = df.loc[idx, "product"]
highest_revenue_value = df.loc[idx, "revenue"]
print(f"Highest revenue product: {highest_revenue_prod}: ${highest_revenue_value}")

df.to_csv("level-04-working-with-data/sales_with_revenue.csv")
print("Saved to sales_with_revenue.csv")


# =================================================================================

# Exercise 9: Error Handling for Files
# Difficulty: Intermediate

# Write a Python program that:

#   1. Tries to read a file called data.txt
#   2. Handles FileNotFoundError gracefully
#   3. Handles PermissionError gracefully
#   4. If file doesn't exist, creates it with sample data
#   5. Then reads and displays the content

# Expected Output Format:

# File not found. Creating new file with sample data.
# File created and read successfully:
# Sample data line 1
# Sample data line 2

try:
    with open("level-04-working-with-data/data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found. Creating new file with sample data.")
    with open("level-04-working-with-data/data.txt", "w") as file:
        file.write("Sample data line 1\n")
        file.write("Sample data line 2")
    with open("level-04-working-with-data/data.txt", "r") as file:
        content = file.read()
    print("File created and read successfully:")
except PermissionError:
    print("No permission to read this file!")

print(content)

# =================================================================================

# Exercise 10: Multiple File Operations
# Difficulty: Advanced

# Write a Python program that:

#   1. Reads data from employees.csv (from Exercise 3)
#   2. Groups employees by department
#   3. Creates separate CSV files for each department:
#       engineering_employees.csv
#       marketing_employees.csv
#       sales_employees.csv
#   4. Prints a summary of what was created

# Expected Output Format:

# Created department files:
#   engineering_employees.csv: 1 employees
#   marketing_employees.csv: 1 employees
#   sales_employees.csv: 1 employees

df = pd.read_csv("level-04-working-with-data/employees.csv")

grouped = df.groupby("department")

print("Created department files: ")
for dept, group in grouped:
    filename = f"level-04-working-with-data/{dept.lower().replace(' ', '_')}_employees.csv"
    
    # create that specific department and do not include the row number
    group.to_csv(filename, index=False)

    print(f" {filename}: {len(group)} employees")
