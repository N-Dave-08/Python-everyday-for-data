# Level 2 Exercises: Data Structures

Complete these exercises to practice working with lists, dictionaries, sets, and tuples.

## Exercise 1: List Basics
**Difficulty: Beginner**

Create a list of 5 fruits: `["apple", "banana", "cherry", "date", "elderberry"]`
1. Print the first fruit
2. Print the last fruit
3. Print the middle 3 fruits (using slicing)
4. Add "fig" to the end of the list
5. Insert "apricot" at index 2
6. Print the final list

**Expected Output Format:**
```
First fruit: apple
Last fruit: elderberry
Middle fruits: ['banana', 'cherry', 'date']
Final list: ['apple', 'banana', 'apricot', 'cherry', 'date', 'elderberry', 'fig']
```

---

## Exercise 2: List Operations
**Difficulty: Beginner**

Given the list: `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]`
1. Find the sum of all numbers
2. Find the maximum value
3. Find the minimum value
4. Count how many times 5 appears
5. Sort the list in ascending order
6. Remove all duplicates (convert to set and back to list)

**Expected Output Format:**
```
Sum: 42
Maximum: 9
Minimum: 1
Count of 5: 3
Sorted: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
Unique: [1, 2, 3, 4, 5, 6, 9]
```

---

## Exercise 3: List Comprehensions
**Difficulty: Intermediate**

1. Create a list of squares from 0 to 9 using list comprehension
2. Create a list of even numbers from 0 to 20 using list comprehension
3. Given `words = ["hello", "world", "python", "data"]`, create a list of word lengths using list comprehension
4. Create a list of numbers from 1 to 20 that are divisible by 3 using list comprehension

**Expected Output Format:**
```
Squares: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Evens: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Word lengths: [5, 5, 6, 4]
Divisible by 3: [3, 6, 9, 12, 15, 18]
```

---

## Exercise 4: Dictionary Basics
**Difficulty: Beginner**

Create a dictionary for a product with the following information:
- name: "Laptop"
- price: 999.99
- quantity: 5
- in_stock: True

1. Print all keys
2. Print all values
3. Print the product name
4. Update the quantity to 10
5. Add a new key "category" with value "Electronics"
6. Print the final dictionary

**Expected Output Format:**
```
Keys: dict_keys(['name', 'price', 'quantity', 'in_stock'])
Values: dict_values(['Laptop', 999.99, 5, True])
Product name: Laptop
Final dictionary: {'name': 'Laptop', 'price': 999.99, 'quantity': 10, 'in_stock': True, 'category': 'Electronics'}
```

---

## Exercise 5: Dictionary Operations
**Difficulty: Intermediate**

Given two dictionaries:
```python
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
```

1. Merge them (dict2 values should overwrite dict1 for common keys)
2. Find all keys that are in both dictionaries
3. Find all keys that are only in dict1
4. Find all keys that are only in dict2
5. Create a new dictionary with the sum of values for common keys

**Expected Output Format:**
```
Merged: {'a': 1, 'b': 4, 'c': 5, 'd': 6}
Common keys: ['b', 'c']
Only in dict1: ['a']
Only in dict2: ['d']
Summed values: {'b': 6, 'c': 8}
```

---

## Exercise 6: Dictionary Comprehensions
**Difficulty: Intermediate**

1. Create a dictionary mapping numbers 0-9 to their squares using dictionary comprehension
2. Given `words = ["apple", "banana", "cherry"]`, create a dictionary mapping each word to its length using dictionary comprehension
3. Create a dictionary of even numbers (0-10) mapped to their doubles using dictionary comprehension

**Expected Output Format:**
```
Squares: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
Word lengths: {'apple': 5, 'banana': 6, 'cherry': 6}
Even doubles: {0: 0, 2: 4, 4: 8, 6: 12, 8: 16, 10: 20}
```

---

## Exercise 7: Sets
**Difficulty: Intermediate**

Given two sets:
```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
```

1. Find the union of both sets
2. Find the intersection of both sets
3. Find elements in set1 but not in set2
4. Find elements in set2 but not in set1
5. Find elements that are in either set but not both (symmetric difference)
6. Remove duplicates from the list `[1, 2, 2, 3, 3, 3, 4, 5, 5]` using a set

**Expected Output Format:**
```
Union: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection: {4, 5}
Set1 - Set2: {1, 2, 3}
Set2 - Set1: {6, 7, 8}
Symmetric difference: {1, 2, 3, 6, 7, 8}
Unique from list: [1, 2, 3, 4, 5]
```

---

## Exercise 8: Tuples
**Difficulty: Beginner**

1. Create a tuple with coordinates: `(10, 20)`
2. Unpack the tuple into two variables `x` and `y`
3. Create a tuple with person info: `("John", 30, "New York")`
4. Unpack it into `name`, `age`, and `city`
5. Create a tuple of 5 numbers and find its length
6. Count how many times 3 appears in the tuple `(1, 2, 3, 2, 3, 4, 3, 5)`

**Expected Output Format:**
```
Coordinates: (10, 20)
x = 10, y = 20
Person: ('John', 30, 'New York')
name = John, age = 30, city = New York
Length: 5
Count of 3: 3
```

---

## Exercise 9: Nested Data Structures
**Difficulty: Intermediate**

Create a list of dictionaries representing employees:
```python
employees = [
    {"name": "John", "age": 30, "department": "Engineering"},
    {"name": "Alice", "age": 25, "department": "Marketing"},
    {"name": "Bob", "age": 35, "department": "Engineering"}
]
```

1. Print all employee names
2. Find the average age
3. Count employees by department
4. Find the oldest employee's name
5. Create a list of all departments (unique)

**Expected Output Format:**
```
Names: ['John', 'Alice', 'Bob']
Average age: 30.0
Employees by department: {'Engineering': 2, 'Marketing': 1}
Oldest employee: Bob
Departments: ['Engineering', 'Marketing']
```

---

## Hints

<details>
<summary>Hint for Exercise 1</summary>
Use indexing `[0]` for first, `[-1]` for last, slicing `[1:4]` for middle, `append()` to add, and `insert()` to insert at index.
</details>

<details>
<summary>Hint for Exercise 2</summary>
Use `sum()`, `max()`, `min()`, `count()`, `sort()`, and convert to set then back to list for unique values.
</details>

<details>
<summary>Hint for Exercise 3</summary>
List comprehension syntax: `[expression for item in iterable if condition]`
</details>

<details>
<summary>Hint for Exercise 4</summary>
Use dictionary methods: `.keys()`, `.values()`, access with `dict["key"]`, update with `dict["key"] = value`.
</details>

<details>
<summary>Hint for Exercise 5</summary>
Use `update()` to merge, set operations for keys, and dictionary comprehension for summing values.
</details>

<details>
<summary>Hint for Exercise 6</summary>
Dictionary comprehension syntax: `{key: value for item in iterable}`
</details>

<details>
<summary>Hint for Exercise 7</summary>
Use set operators: `|` (union), `&` (intersection), `-` (difference), `^` (symmetric difference).
</details>

<details>
<summary>Hint for Exercise 8</summary>
Use tuple unpacking: `x, y = tuple`, and tuple methods: `len()`, `count()`.
</details>

<details>
<summary>Hint for Exercise 9</summary>
Iterate through the list, access dictionary values, use list comprehensions, and calculate statistics.
</details>

---

**Good luck!** Try to solve these without looking at the solutions first. If you get stuck, review the lessons or check the hints.
