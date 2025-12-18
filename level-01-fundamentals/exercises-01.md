# Level 1 Exercises: Python Fundamentals

Complete these exercises to practice Python fundamentals: variables, data types, and basic operations.

## Exercise 1: Basic Variables
**Difficulty: Beginner**

Create variables to store information about a person:
- Name (string)
- Age (integer)
- City (string)
- Is employed (boolean)

Print all the information in a formatted message.

**Expected Output Format:**
```
Name: John Smith
Age: 30
City: New York
Is Employed: True
```

---

## Exercise 2: Data Types
**Difficulty: Beginner**

Create variables with different data types and determine their types:
- An integer: `42`
- A float: `3.14`
- A string: `"Hello"`
- A boolean: `True`
- A None value: `None`

Print each variable along with its type.

**Expected Output Format:**
```
Value: 42, Type: <class 'int'>
Value: 3.14, Type: <class 'float'>
Value: Hello, Type: <class 'str'>
Value: True, Type: <class 'bool'>
Value: None, Type: <class 'NoneType'>
```

---

## Exercise 3: Basic Calculations
**Difficulty: Beginner**

Calculate the following:
1. The sum of 15, 25, and 35
2. The product of 8 and 7
3. The result of 100 divided by 4
4. The remainder when 27 is divided by 5
5. 2 raised to the power of 8

Print each calculation with a descriptive message.

**Expected Output Format:**
```
Sum: 75
Product: 56
Quotient: 25.0
Remainder: 2
Power: 256
```

---

## Exercise 4: String Operations
**Difficulty: Beginner**

Given the string `"Python Programming"`:
1. Convert it to uppercase
2. Convert it to lowercase
3. Find the length of the string
4. Count how many times the letter 'P' appears
5. Replace "Programming" with "Data Analysis"

Print each result.

**Expected Output Format:**
```
Uppercase: PYTHON PROGRAMMING
Lowercase: python programming
Length: 18
Count of 'P': 2
Replaced: Python Data Analysis
```

---

## Exercise 5: String Formatting
**Difficulty: Beginner**

Create variables for:
- Product name: "Laptop"
- Price: 999.99
- Quantity: 3

Use f-string formatting to create a message that displays:
"The total cost for 3 Laptop(s) is $2999.97"

**Expected Output Format:**
```
The total cost for 3 Laptop(s) is $2999.97
```

---

## Exercise 6: Type Conversion
**Difficulty: Intermediate**

Given the following values (as strings):
- `"42"` (should be integer)
- `"3.14"` (should be float)
- `"100"` (should be integer)

Convert each to the appropriate numeric type and:
1. Add the integer values together
2. Multiply the float by 10
3. Print all results

**Expected Output Format:**
```
Sum of integers: 142
Float multiplied by 10: 31.4
```

---

## Exercise 7: Working with User Input
**Difficulty: Intermediate**

Write a program that:
1. Asks the user for their first name
2. Asks the user for their age (as an integer)
3. Asks the user for their favorite number (as a float)
4. Displays a formatted message with all the information

**Note**: For testing purposes, you can hardcode values instead of using `input()`.

**Expected Output Format:**
```
First Name: Alice
Age: 25
Favorite Number: 7.5
Hello, Alice! You are 25 years old and your favorite number is 7.5.
```

---

## Exercise 8: Calculate Statistics
**Difficulty: Intermediate**

Given a list of test scores: `[85, 92, 78, 96, 88, 90, 82]`
1. Calculate the sum of all scores
2. Calculate the average (mean) score
3. Find the highest score
4. Find the lowest score
5. Calculate the range (highest - lowest)

Print all statistics with descriptive labels.

**Expected Output Format:**
```
Scores: [85, 92, 78, 96, 88, 90, 82]
Sum: 611
Average: 87.29
Highest: 96
Lowest: 78
Range: 18
```

---

## Hints

<details>
<summary>Hint for Exercise 1</summary>
Create variables using assignment (`=`), then use f-strings to format the output.
</details>

<details>
<summary>Hint for Exercise 2</summary>
Use the `type()` function to check the type of each variable.
</details>

<details>
<summary>Hint for Exercise 3</summary>
Use arithmetic operators: `+`, `*`, `/`, `%`, and `**`.
</details>

<details>
<summary>Hint for Exercise 4</summary>
Use string methods: `.upper()`, `.lower()`, `len()`, `.count()`, and `.replace()`.
</details>

<details>
<summary>Hint for Exercise 5</summary>
Use f-string formatting: `f"text {variable}"`. Calculate total cost as price * quantity.
</details>

<details>
<summary>Hint for Exercise 6</summary>
Use `int()` to convert to integer and `float()` to convert to float.
</details>

<details>
<summary>Hint for Exercise 7</summary>
Use `input()` for strings, `int(input())` for integers, and `float(input())` for floats. For testing, you can assign values directly.
</details>

<details>
<summary>Hint for Exercise 8</summary>
Use `sum()`, `len()`, `max()`, and `min()` functions. Calculate average as sum divided by length.
</details>

---

**Good luck!** Try to solve these without looking at the solutions first. If you get stuck, review the lessons or check the hints.
