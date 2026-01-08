# Exercise 1: List Basics
# Difficulty: Beginner

# Create a list of 5 fruits: ["apple", "banana", "cherry", "date", "elderberry"]

#   1. Print the first fruit
#   2. Print the last fruit
#   3. Print the middle 3 fruits (using slicing)
#   4. Add "fig" to the end of the list
#   5. Insert "apricot" at index 2
#   6. Print the final list

# Expected Output Format:

#   First fruit: apple
#   Last fruit: elderberry
#   Middle fruits: ['banana', 'cherry', 'date']
#   Final list: ['apple', 'banana', 'apricot', 'cherry', 'date', 'elderberry', 'fig']

from heapq import merge


fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Middle fruits: {fruits[1:-1]}")
print(f"Final list: {fruits[:]}")

# =================================================================================

# Exercise 2: List Operations
# Difficulty: Beginner

# Given the list: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Find the sum of all numbers
# Find the maximum value
# Find the minimum value
# Count how many times 5 appears
# Sort the list in ascending order
# Remove all duplicates (convert to set and back to list)

# Expected Output Format:

#   Sum: 44
#   Maximum: 9
#   Minimum: 1
#   Count of 5: 3
#   Sorted: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
#   Unique: [1, 2, 3, 4, 5, 6, 9]

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(f"Sum: {sum(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")
print(f"Count of 5: {numbers.count(5)}")
print(f"Sorted: {sorted(numbers)}")
print(f"Unique: {set(numbers)}")

# =================================================================================

# Exercise 3: List Comprehensions
# Difficulty: Intermediate

#   1. Create a list of squares from 0 to 9 using list comprehension
#   2. Create a list of even numbers from 0 to 20 using list comprehension
#   3. Given words = ["hello", "world", "python", "data"], create a list of word lengths using list comprehension
#   4. Create a list of numbers from 1 to 20 that are divisible by 3 using list comprehension

# Expected Output Format:

#   Squares: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#   Evens: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#   Word lengths: [5, 5, 6, 4]
#   Divisible by 3: [3, 6, 9, 12, 15, 18]

squares = [x**2 for x in range(10)]
evens = [x for x in range(21) if x % 2 == 0]
words = ["hello", "world", "python", "data"]
lengths = [len(word) for word in words]
div_by_three = [x for x in range (1, 21) if x % 3 == 0]

print(f"Squares: {squares}")
print(f"Evens: {evens}")
print(f"Word lengths: {lengths}")
print(f"Divisible by 3: {div_by_three}")

# =================================================================================

# Exercise 4: Dictionary Basics
# Difficulty: Beginner

# Create a dictionary for a product with the following information:

# name: "Laptop"
# price: 999.99
# quantity: 5
# in_stock: True
# Print all keys
# Print all values
# Print the product name
# Update the quantity to 10
# Add a new key "category" with value "Electronics"
# Print the final dictionary

# Expected Output Format:

#   Keys: dict_keys(['name', 'price', 'quantity', 'in_stock'])
#   Values: dict_values(['Laptop', 999.99, 5, True])
#   Product name: Laptop
#   Final dictionary: {'name': 'Laptop', 'price': 999.99, 'quantity': 10, 'in_stock': True, 'category': 'Electronics'}

dict = {
    "name": "Laptop",
    "price": 999.99,
    "quantity": 5,
    "in_stock": True
}

dict["quantity"] = 10

dict_keys = dict.keys()
dict_values = dict.values()
dict["category"] = 'Electronics'

print(f"Keys: {dict_keys}")
print(f"Values: {dict_values}")
print(f"Product name: {dict['name']}")
print(f"Final dictionary: {dict}")

# =================================================================================

# Exercise 5: Dictionary Operations
# Difficulty: Intermediate

# Given two dictionaries:

# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 4, "c": 5, "d": 6}
# Merge them (dict2 values should overwrite dict1 for common keys)
# Find all keys that are in both dictionaries
# Find all keys that are only in dict1
# Find all keys that are only in dict2
# Create a new dictionary with the sum of values for common keys
# Expected Output Format:

# Merged: {'a': 1, 'b': 4, 'c': 5, 'd': 6}
# Common keys: ['b', 'c']
# Only in dict1: ['a']
# Only in dict2: ['d']
# Summed values: {'b': 6, 'c': 8}

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}

merged = dict1 | dict2
common_keys = sorted(set(dict1) & set(dict2))
dict1_keys = set(dict1) - set(dict2)
dict2_keys = set(dict2) - set(dict1)
sum_of_common_keys = {key: dict1[key] + dict2[key] for key in common_keys}

print(f"Merged: {merged}")
print(f"Common keys: {common_keys}")
print(f"Only in dict1: {dict1_keys}")
print(f"Only in dict2: {dict2_keys}")
print(f"Summed values: {sum_of_common_keys}")

# =================================================================================

# Exercise 6: Dictionary Comprehensions
# Difficulty: Intermediate

# Create a dictionary mapping numbers 0-9 to their squares using dictionary comprehension
# Given words = ["apple", "banana", "cherry"], create a dictionary mapping each word to its length using dictionary comprehension
# Create a dictionary of even numbers (0-10) mapped to their doubles using dictionary comprehension
# Expected Output Format:

# Squares: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# Word lengths: {'apple': 5, 'banana': 6, 'cherry': 6}
# Even doubles: {0: 0, 2: 4, 4: 8, 6: 12, 8: 16, 10: 20}

squares = {x: x**2 for x in range(10)}

words = ["apple", "banana", "cherry"]
lengths = {word:len(word) for word in words}

evens = {x: x*2 for x in range(11) if x % 2 == 0}

print(f"Squares: {squares}")
print(f"Word lengths: {lengths}")
print(f"Even doubles: {evens}")

# =================================================================================

# Exercise 7: Sets
# Difficulty: Intermediate

# Given two sets:

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# Find the union of both sets
# Find the intersection of both sets
# Find elements in set1 but not in set2
# Find elements in set2 but not in set1
# Find elements that are in either set but not both (symmetric difference)
# Remove duplicates from the list [1, 2, 2, 3, 3, 3, 4, 5, 5] using a set
# Expected Output Format:

# Union: {1, 2, 3, 4, 5, 6, 7, 8}
# Intersection: {4, 5}
# Set1 - Set2: {1, 2, 3}
# Set2 - Set1: {6, 7, 8}
# Symmetric difference: {1, 2, 3, 6, 7, 8}
# Unique from list: [1, 2, 3, 4, 5]

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1 | set2
union = set1.union(set2)
intersection = set1 & set2
intersection = set1.intersection(set2)
diff_set1 = set1 - set2
diff_set2 = set2 - set1
sym_diff = set1 ^ set2
sym_diff = set1.symmetric_difference(set2)

numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = list(set(numbers))

print(f"Union: {union}")
print(f"Intersection: {intersection}")
print(f"Set1 - Set2: {diff_set1}")
print(f"Set2 - Set1: {diff_set2}")
print(f"Symmetric difference: {sym_diff}")
print(f"Unique from list: {unique}")

# =================================================================================

# Exercise 8: Tuples
# Difficulty: Beginner

# Create a tuple with coordinates: (10, 20)
# Unpack the tuple into two variables x and y
# Create a tuple with person info: ("John", 30, "New York")
# Unpack it into name, age, and city
# Create a tuple of 5 numbers and find its length
# Count how many times 3 appears in the tuple (1, 2, 3, 2, 3, 4, 3, 5)
# Expected Output Format:

# Coordinates: (10, 20)
# x = 10, y = 20
# Person: ('John', 30, 'New York')
# name = John, age = 30, city = New York
# Length: 5
# Count of 3: 3

coordinates = (10, 20)
x, y = coordinates
person = ("John", 30, "New York")
name, age, city = person
numbers = (1, 2, 3, 4, 5)
length = len(numbers)
count_of_3 = (1, 2, 3, 2, 3, 4, 3, 5).count(3)

print(f"Coordinates: {coordinates}")
print(f"x = {x}, y = {y}")
print(f"Person: {person}")
print(f"name = {name}, age = {age}, city = {city}")
print(f"Length: {length}")
print(f"Count of 3: {count_of_3}")

# =================================================================================

# Exercise 9: Nested Data Structures
# Difficulty: Intermediate

# Create a list of dictionaries representing employees:

# employees = [
#     {"name": "John", "age": 30, "department": "Engineering"},
#     {"name": "Alice", "age": 25, "department": "Marketing"},
#     {"name": "Bob", "age": 35, "department": "Engineering"}
# ]
# Print all employee names
# Find the average age
# Count employees by department
# Find the oldest employee's name
# Create a list of all departments (unique)
# Expected Output Format:

# Names: ['John', 'Alice', 'Bob']
# Average age: 30.0
# Employees by department: {'Engineering': 2, 'Marketing': 1}
# Oldest employee: Bob
# Departments: ['Engineering', 'Marketing']

employees = [
    {"name": "John", "age": 30, "department": "Engineering"},
    {"name": "Alice", "age": 25, "department": "Marketing"},
    {"name": "Bob", "age": 35, "department": "Engineering"}
]

names = [employee["name"] for employee in employees]

age = [employee["age"] for employee in employees]
avg_age = sum(age) / len(age)

by_dept = {}
for employee in employees:
    department = employee["department"]
    if department not in by_dept:
        by_dept[department] = 1
    else:
        by_dept[department] += 1

oldest = max(employees, key=lambda emp: emp["age"])

depts = [employee["department"] for employee in employees]

print(f"Names: {names}")
print(f"Average age: {age}")
print(f"Employees by department: {by_dept}")
print(f"Oldest employee: {oldest["name"]}")
print(f"Departments: {set(depts)}")