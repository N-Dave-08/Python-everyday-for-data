# Exercise 1: Basic Variables
# Difficulty: Beginner

# Create variables to store information about a person:

# Name (string)
# Age (integer)
# City (string)
# Is employed (boolean)
# Print all the information in a formatted message.

# Expected Output Format:

# Name: John Smith
# Age: 30
# City: New York
# Is Employed: True

from math import remainder
from tkinter import X


name = "john smith".title()
age = 30
city = "new york".title()
isEmployed = True

print(f"Name: {name}, Age: {age}, City: {city}, IsEmployed: {isEmployed}")

# =================================================================================

# Exercise 2: Data Types
# Difficulty: Beginner

# Create variables with different data types and determine their types:

# An integer: 42
# A float: 3.14
# A string: "Hello"
# A boolean: True
# A None value: None
# Print each variable along with its type.

# Expected Output Format:

# Value: 42, Type: <class 'int'>
# Value: 3.14, Type: <class 'float'>
# Value: Hello, Type: <class 'str'>
# Value: True, Type: <class 'bool'>
# Value: None, Type: <class 'NoneType'>

integer = 42
float = 3.14
string = "Hello"
boolean = True
none = None

print(f"Value: {integer}, Type: {type(integer)}")
print(f"Value: {float}, Type: {type(float)}")
print(f"Value: {string}, Type: {type(string)}")
print(f"Value: {boolean}, Type: {type(boolean)}")
print(f"Value: {none}, Type: {type(none)}")

# =================================================================================

# Exercise 3: Basic Calculations
# Difficulty: Beginner

# Calculate the following:

#   1. The sum of 15, 25, and 35
#   2. The product of 8 and 7
#   3. The result of 100 divided by 4
#   4. The remainder when 27 is divided by 5
#   5. 2 raised to the power of 8

# Print each calculation with a descriptive message.

# Expected Output Format:

# Sum: 75
# Product: 56
# Quotient: 25.0
# Remainder: 2
# Power: 256

sum = 15 + 25 + 35
product = 8 * 7
result = 100 / 4
remainder = 27 % 5
power = 2 ** 8

print(f"Sum: {sum}")
print(f"Product: {product}")
print(f"Result: {result}")
print(f"Remainder: {remainder}")
print(f"Power: {power}")

# =================================================================================

# Exercise 4: String Operations
# Difficulty: Beginner

# Given the string "Python Programming":

# Convert it to uppercase
# Convert it to lowercase
# Find the length of the string
# Count how many times the letter 'P' appears
# Replace "Programming" with "Data Analysis"
# Print each result.

# Expected Output Format:

# Uppercase: PYTHON PROGRAMMING
# Lowercase: python programming
# Length: 18
# Count of 'P': 2
# Replaced: Python Data Analysis

text = "Python Programming"

uppercase = text.upper()
lowercase = text.lower()
length = len(text)
count = text.count('p')
replace = text.replace('Programming', 'Data Analysis')

print(f"Uppercase: {uppercase}")
print(f"Lowercase: {lowercase}")
print(f"Lenght: {length}")
print(f"Count: {count}")
print(f"Replaced: {replace}")

# =================================================================================

# Exercise 5: String Formatting
# Difficulty: Beginner

# Create variables for:

# Product name: "Laptop"
# Price: 999.99
# Quantity: 3
# Use f-string formatting to create a message that displays: "The total cost for 3 Laptop(s) is $2999.97"

# Expected Output Format:

# The total cost for 3 Laptop(s) is $2999.97

name = "Laptop"
price = 999.99
quantity = 3
total = price * quantity

print(f"The total cost for {quantity} Laptop(s) is ${total:.2f}")

# =================================================================================

# Exercise 6: Type Conversion
# Difficulty: Intermediate

# Given the following values (as strings):

# "42" (should be integer)
# "3.14" (should be float)
# "100" (should be integer)
# Convert each to the appropriate numeric type and:

# Add the integer values together
# Multiply the float by 10
# Print all results
# Expected Output Format:

# Sum of integers: 142
# Float multiplied by 10: 31.4

x = int("42")
y = float("3.14")
z = int("100")

sum = x + z
product = y * 10

print(f"Sum of integers: {sum}")
print(f"Float multiplied by 10: {product:.1f}")

# =================================================================================

# Exercise 7: Working with User Input
# Difficulty: Intermediate

# Write a program that:

# Asks the user for their first name
# Asks the user for their age (as an integer)
# Asks the user for their favorite number (as a float)
# Displays a formatted message with all the information
# Note: For testing purposes, you can hardcode values instead of using input().

# Expected Output Format:

# First Name: Alice
# Age: 25
# Favorite Number: 7.5
# Hello, Alice! You are 25 years old and your favorite number is 7.5.

name = input("Enter your first name: ")
age = int(input("Enter your age: "))
fav_num = float(input("Enter your favorite number: "))

print(f"Hello, {name}! You are {age} years old and your favorite number is {fav_num}.")

# =================================================================================

# Exercise 8: Calculate Statistics
# Difficulty: Intermediate

# Given a list of test scores: [85, 92, 78, 96, 88, 90, 82]

# Calculate the sum of all scores
# Calculate the average (mean) score
# Find the highest score
# Find the lowest score
# Calculate the range (highest - lowest)
# Print all statistics with descriptive labels.

# Expected Output Format:

# Scores: [85, 92, 78, 96, 88, 90, 82]
# Sum: 611
# Average: 87.29
# Highest: 96
# Lowest: 78
# Range: 18

scores = [85, 92, 78, 96, 88, 90, 82]

total = sum(scores)
avg = sum(scores) / len(scores)
highest = max(scores)
lowest = min(scores)
range = highest - lowest

print(f"Scores: {scores}")
print(f"Sum: {total}")
print(f"Average: {round(avg, 2)}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Range: {range}")