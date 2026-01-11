# Exercise 1: Conditionals
# Difficulty: Beginner

# Write a program that:

#   1. Takes a score (0-100) as input
#   2. Assigns a grade based on the score:
#       A: 90-100
#       B: 80-89
#       C: 70-79
#       D: 60-69
#       F: Below 60
#   3. Prints the grade
# Note: For testing, you can hardcode the score instead of using input().

# Expected Output Format:

#   Score: 85
#   Grade: B
from email import message
from enum import unique
from itertools import product
from turtle import width


grades = []

for _ in range(5):
    while True:
        try:
            grade = int(input("Enter your grade: "))
            if grade > 100 or grade < 0:
                raise ValueError("Please enter a valid grade")
            break
        except ValueError as e:
            print(f"Inavlid input, please enter valid value: {e}")
    grades.append(grade)

def calc_avg(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

score = calc_avg(grades)
grade = ""

if score < 60:
    grade = "F"
elif score >= 60 and score < 70:
    grade = "D"
elif score >= 70 and score < 80:
    grade = "C"
elif score >= 80 and score < 90:
    grade = "B"
elif score >= 90 and score <= 100:
    grade = "A"
else:
    print("inavlid")

print(f"Score: {score}")
print(f"Grade: {grade}")

# =================================================================================

# Exercise 2: Loops - Sum and Average
# Difficulty: Beginner

# Given a list of numbers: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#   1. Use a for loop to calculate the sum
#   2. Calculate the average
#   3. Find the maximum value
#   4. Find the minimum value
#   5. Print all results

# Expected Output Format:

#   Sum: 550
#   Average: 55.0
#   Maximum: 100
#   Minimum: 10

list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
total = 0

for num in list:
    total += num

avg = total /len(list)
max_num = max(list)
min_num = min(list)

print(f"Sum: {total}")
print(f"Average: {avg}")
print(f"Maximum: {max_num}")
print(f"Minimum: {min_num}")

# =================================================================================

# Exercise 3: Loops - Filtering
# Difficulty: Beginner

# Given a list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Create a new list with only even numbers (using a loop)
# Create a new list with only numbers divisible by 3 (using a loop)
# Create a new list with numbers greater than 10 (using a loop)
# Expected Output Format:

# Evens: [2, 4, 6, 8, 10, 12, 14]
# Divisible by 3: [3, 6, 9, 12, 15]
# Greater than 10: [11, 12, 13, 14, 15]

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
evens = []
div_by_three = []
greater_than_then = []

for num in list:
    if num % 2 == 0:
        evens.append(num)

for num in list:
    if num % 3 == 0:
        div_by_three.append(num)

for num in list:
    if num > 10:
        greater_than_then.append(num)

print(f"Evens: {evens}")
print(f"Divisible by 3: {div_by_three}")
print(f"Greater than 10: {greater_than_then}")

# =================================================================================

# Exercise 4: Nested Loops
# Difficulty: Intermediate

# Create a multiplication table for numbers 1 to 5:

# Use nested loops
# Format: "1 x 1 = 1", "1 x 2 = 2", etc.
# Print a blank line between each table
# Expected Output Format:

# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5

# 2 x 1 = 2
# 2 x 2 = 4
# ...

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print()

# =================================================================================

# Exercise 5: Functions - Basic
# Difficulty: Beginner

# Create a function called calculate_area that:

# Takes length and width as parameters
# Returns the area of a rectangle
# Test it with length=10, width=5
# Create a function called greet_person that:

# Takes name and optional greeting (default "Hello")
# Returns a greeting message
# Test with name="Alice" and name="Bob" with greeting="Hi"
# Expected Output Format:

# Area: 50
# Hello, Alice!
# Hi, Bob!

length = int(input("enter length: "))
width = int(input("enter width: "))

def calc_area(length, width):
    return length * width

area = calc_area(length, width)

name = str(input("enter your name: "))
greet = str(input("enter your greetings: "))

def greet_person(name, greet="Hello"):
    return f"{greet}, {name}"

if greet.strip() == "":
    message = greet_person(name)
else:
    message = greet_person(name, greet)

print(f"Area: {area}")
print(message)


# =================================================================================

# Exercise 6: Functions - Multiple Returns
# Difficulty: Intermediate

# Create a function called analyze_numbers that:

# Takes a list of numbers as parameter
# Returns a tuple with: (sum, average, maximum, minimum)
# Test with [10, 20, 30, 40, 50]
# Expected Output Format:

# Numbers: [10, 20, 30, 40, 50]
# Sum: 150, Average: 30.0, Max: 50, Min: 10

list = []
avg = 0

for num in range(5):
    num = int(input("enter a number: "))
    list.append(num)

def analyze_num(sum, avg, max, min):
    sum = sum(list)
    avg = sum / len(list)
    max = max(list)
    min = min(list)
    return sum, avg, max, min

print(analyze_num(sum, avg, max, min))

# =================================================================================

# Exercise 7: Functions - Data Processing
# Difficulty: Intermediate

# Create a function called process_employees that:

# Takes a list of dictionaries (employees) as parameter
# Returns a dictionary with:
# Total number of employees
# Average age
# List of all names
# Test with:
# employees = [
#     {"name": "John", "age": 30},
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 35}
# ]
# Expected Output Format:

# Total: 3
# Average Age: 30.0
# Names: ['John', 'Alice', 'Bob']

employees = []

for _ in range(3):
    name = str(input("enter name of the employee: "))
    age = int(input("enter the age of that employee: "))

    # putting the name and age values inside a dictionary
    employee = {"name": name, "age": age}

    # adding the employee value inside the employees
    employees.append(employee)

def process_employees(employees):
    # number of employees
    total = len(employees)

    # sum of all ages of employees
    sum_of_age = sum(employee["age"] for employee in employees)

    # average age of employees
    avg_age = sum_of_age / len(employees)

    # put the names of the employees into a list
    names = [employee["name"] for employee in employees]

    # gather all in a dictionary
    return {
        "total": total,
        "avg_age": avg_age,
        "names": names
    }

result = process_employees(employees)

print(f"Total: {result["total"]}")
print(f"Average Age: {result["avg_age"]}")
print(f"Names: {result["names"]}")

# =================================================================================

# Exercise 8: Error Handling
# Difficulty: Intermediate

# Create a function called safe_divide that:

# Takes two numbers a and b as parameters
# Returns a / b
# Handles ZeroDivisionError and returns None with a message
# Handles TypeError if non-numeric values are passed
# Test with:

# safe_divide(10, 2) → should return 5.0
# safe_divide(10, 0) → should handle error gracefully
# safe_divide("10", 2) → should handle error gracefully
# Expected Output Format:

# Result: 5.0
# Error: Cannot divide by zero!
# Error: Invalid input types!

def safe_divide(a_str, b_str):
    try:
        a = int(a_str)
        b = int(b_str)
        result = int(a / b)
        return result
    except ValueError:
        return "invalid input types"
    except ZeroDivisionError:
        return "cannot devide by zero"

a = input("enter first number: ")
b = input("enter second number: ")

quotient = safe_divide(a, b)

print(quotient)

# =================================================================================

# Exercise 9: Lambda Functions
# Difficulty: Intermediate

# Create a lambda function that squares a number
# Use it with map() to square all numbers in [1, 2, 3, 4, 5]
# Create a lambda function that checks if a number is even
# Use it with filter() to get even numbers from [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected Output Format:

# Squared: [1, 4, 9, 16, 25]
# Evens: [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers2))

print(f"Squared: {squares}")
print(f"Evens: {evens}")

# =================================================================================

# Exercise 10: Comprehensive Exercise
# Difficulty: Advanced

# Create a function called analyze_sales that:

#   1. Takes a list of sales dictionaries with keys: product, quantity, price
#   2. Returns a dictionary with:
#       Total revenue (sum of quantity * price)
#       Number of unique products
#       Average sale amount
#       Product with highest total sales
#   3. Handle errors gracefully (missing keys, invalid data types)

#   Test with:
#   sales = [
#       {"product": "A", "quantity": 10, "price": 5.0},
#       {"product": "B", "quantity": 5, "price": 10.0},
#       {"product": "A", "quantity": 3, "price": 5.0},
#       {"product": "C", "quantity": 8, "price": 7.5}
#   ]
# Expected Output Format:

#   Total Revenue: 177.5
#   Unique Products: 3
#   Average Sale: 43.75
#   Top Product: C

sales = [
      {"product": "A", "quantity": 10, "price": 5.0},
      {"product": "B", "quantity": 5, "price": 10.0},
      {"product": "A", "quantity": 3, "price": 5.0},
      {"product": "C", "quantity": 8, "price": 7.5}
  ]


def analyze_sales(final_result):
    total_revenue = 0
    product_totals = {}
    valid_sales_count = 0

    for sale in final_result:
        try:
            product = sale["product"]
            quantity = sale["quantity"]
            price = sale["price"]

            # check types
            if not isinstance(product, str) or not isinstance(quantity, (int, float)) or not isinstance(price, (int, float)):
                # skip invalid entries
                continue 
            
            # get revenue per dictionary
            revenue = quantity * price

            # add the revenue per dictionary
            total_revenue += revenue

            # count the dictionaries
            valid_sales_count += 1

            # if sale["product"] is in product_totals add its revenue to itself
            if product in product_totals:
                product_totals[product] += revenue
            # if sale["product"] is not in product_totals add it to the dictionary
            else:
                product_totals[product] = revenue
        except KeyError:
            continue

    # get the total number of unique products
    unique_prods = len(product_totals)

    # sum of every revenue per dictionary not per unique products
    # if valid_sales_count is zero, make the avg_sale zero
    avg_sale = total_revenue / valid_sales_count if valid_sales_count else 0

    # get the product with the highest revenue by comparing the values of the keys
    highest_sale = max(product_totals, key=product_totals.get) if product_totals else None

    return {
        "total_revenue": total_revenue,
        "unique_prods": unique_prods,
        "avg_sale": avg_sale,
        "highest_sale": highest_sale
    }


final_result = analyze_sales(sales)