# Level 3 Exercises: Control Flow & Functions

Complete these exercises to practice conditionals, loops, functions, and error handling.

## Exercise 1: Conditionals
**Difficulty: Beginner**

Write a program that:
1. Takes a score (0-100) as input
2. Assigns a grade based on the score:
   - A: 90-100
   - B: 80-89
   - C: 70-79
   - D: 60-69
   - F: Below 60
3. Prints the grade

**Note**: For testing, you can hardcode the score instead of using `input()`.

**Expected Output Format:**
```
Score: 85
Grade: B
```

---

## Exercise 2: Loops - Sum and Average
**Difficulty: Beginner**

Given a list of numbers: `[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]`
1. Use a for loop to calculate the sum
2. Calculate the average
3. Find the maximum value
4. Find the minimum value
5. Print all results

**Expected Output Format:**
```
Sum: 550
Average: 55.0
Maximum: 100
Minimum: 10
```

---

## Exercise 3: Loops - Filtering
**Difficulty: Beginner**

Given a list: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]`
1. Create a new list with only even numbers (using a loop)
2. Create a new list with only numbers divisible by 3 (using a loop)
3. Create a new list with numbers greater than 10 (using a loop)

**Expected Output Format:**
```
Evens: [2, 4, 6, 8, 10, 12, 14]
Divisible by 3: [3, 6, 9, 12, 15]
Greater than 10: [11, 12, 13, 14, 15]
```

---

## Exercise 4: Nested Loops
**Difficulty: Intermediate**

Create a multiplication table for numbers 1 to 5:
- Use nested loops
- Format: "1 x 1 = 1", "1 x 2 = 2", etc.
- Print a blank line between each table

**Expected Output Format:**
```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5

2 x 1 = 2
2 x 2 = 4
...
```

---

## Exercise 5: Functions - Basic
**Difficulty: Beginner**

Create a function called `calculate_area` that:
1. Takes `length` and `width` as parameters
2. Returns the area of a rectangle
3. Test it with length=10, width=5

Create a function called `greet_person` that:
1. Takes `name` and optional `greeting` (default "Hello")
2. Returns a greeting message
3. Test with name="Alice" and name="Bob" with greeting="Hi"

**Expected Output Format:**
```
Area: 50
Hello, Alice!
Hi, Bob!
```

---

## Exercise 6: Functions - Multiple Returns
**Difficulty: Intermediate**

Create a function called `analyze_numbers` that:
1. Takes a list of numbers as parameter
2. Returns a tuple with: (sum, average, maximum, minimum)
3. Test with `[10, 20, 30, 40, 50]`

**Expected Output Format:**
```
Numbers: [10, 20, 30, 40, 50]
Sum: 150, Average: 30.0, Max: 50, Min: 10
```

---

## Exercise 7: Functions - Data Processing
**Difficulty: Intermediate**

Create a function called `process_employees` that:
1. Takes a list of dictionaries (employees) as parameter
2. Returns a dictionary with:
   - Total number of employees
   - Average age
   - List of all names
3. Test with:
   ```python
   employees = [
       {"name": "John", "age": 30},
       {"name": "Alice", "age": 25},
       {"name": "Bob", "age": 35}
   ]
   ```

**Expected Output Format:**
```
Total: 3
Average Age: 30.0
Names: ['John', 'Alice', 'Bob']
```

---

## Exercise 8: Error Handling
**Difficulty: Intermediate**

Create a function called `safe_divide` that:
1. Takes two numbers `a` and `b` as parameters
2. Returns `a / b`
3. Handles `ZeroDivisionError` and returns `None` with a message
4. Handles `TypeError` if non-numeric values are passed

Test with:
- `safe_divide(10, 2)` → should return 5.0
- `safe_divide(10, 0)` → should handle error gracefully
- `safe_divide("10", 2)` → should handle error gracefully

**Expected Output Format:**
```
Result: 5.0
Error: Cannot divide by zero!
Error: Invalid input types!
```

---

## Exercise 9: Lambda Functions
**Difficulty: Intermediate**

1. Create a lambda function that squares a number
2. Use it with `map()` to square all numbers in `[1, 2, 3, 4, 5]`
3. Create a lambda function that checks if a number is even
4. Use it with `filter()` to get even numbers from `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

**Expected Output Format:**
```
Squared: [1, 4, 9, 16, 25]
Evens: [2, 4, 6, 8, 10]
```

---

## Exercise 10: Comprehensive Exercise
**Difficulty: Advanced**

Create a function called `analyze_sales` that:
1. Takes a list of sales dictionaries with keys: `product`, `quantity`, `price`
2. Returns a dictionary with:
   - Total revenue (sum of quantity * price)
   - Number of unique products
   - Average sale amount
   - Product with highest total sales
3. Handle errors gracefully (missing keys, invalid data types)

Test with:
```python
sales = [
    {"product": "A", "quantity": 10, "price": 5.0},
    {"product": "B", "quantity": 5, "price": 10.0},
    {"product": "A", "quantity": 3, "price": 5.0},
    {"product": "C", "quantity": 8, "price": 7.5}
]
```

**Expected Output Format:**
```
Total Revenue: 177.5
Unique Products: 3
Average Sale: 43.75
Top Product: C
```

---

## Hints

<details>
<summary>Hint for Exercise 1</summary>
Use if/elif/else statements with comparison operators (>=, <).
</details>

<details>
<summary>Hint for Exercise 2</summary>
Initialize variables before the loop, accumulate sum in the loop, calculate average after.
</details>

<details>
<summary>Hint for Exercise 3</summary>
Create empty lists, use if statements inside loops to filter, append matching items.
</details>

<details>
<summary>Hint for Exercise 4</summary>
Use nested for loops: outer loop for multiplier, inner loop for multiplicand.
</details>

<details>
<summary>Hint for Exercise 5</summary>
Use `def` to define functions, `return` to return values, default parameters for optional args.
</details>

<details>
<summary>Hint for Exercise 6</summary>
Calculate all values, return as tuple: `return (sum, avg, max, min)`.
</details>

<details>
<summary>Hint for Exercise 7</summary>
Iterate through list, accumulate data, use dictionary comprehensions or loops to build result.
</details>

<details>
<summary>Hint for Exercise 8</summary>
Use try/except blocks, catch specific exceptions, return None on error.
</details>

<details>
<summary>Hint for Exercise 9</summary>
Lambda syntax: `lambda x: expression`, use with `map()` and `filter()`, convert to list.
</details>

<details>
<summary>Hint for Exercise 10</summary>
Iterate through sales, calculate totals, use dictionaries to track product sales, handle errors with try/except.
</details>

---

**Good luck!** Try to solve these without looking at the solutions first. If you get stuck, review the lessons or check the hints.
