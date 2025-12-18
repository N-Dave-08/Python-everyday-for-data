# Lesson 1.3: Basic Operations and Working with Data

## Working with Numbers

### Mathematical Operations Review

```python
# Basic arithmetic
a = 10
b = 3

print(a + b)  # 13 (addition)
print(a - b)  # 7 (subtraction)
print(a * b)  # 30 (multiplication)
print(a / b)  # 3.333... (division)
print(a // b)  # 3 (floor division)
print(a % b)  # 1 (modulus/remainder)
print(a ** b)  # 1000 (exponentiation)
```

### Order of Operations

Python follows standard mathematical order of operations (PEMDAS):

```python
result = 2 + 3 * 4  # 14 (not 20)
# Multiplication happens before addition

result = (2 + 3) * 4  # 20
# Parentheses change the order
```

### Working with Large Numbers

Python handles large numbers automatically:

```python
large = 1000000
very_large = 10 ** 100  # Python handles this!
```

## String Operations

### String Methods

Strings have many useful methods:

```python
text = "Hello, Python!"

# Convert to uppercase
upper_text = text.upper()  # "HELLO, PYTHON!"

# Convert to lowercase
lower_text = text.lower()  # "hello, python!"

# Capitalize first letter
capitalized = text.capitalize()  # "Hello, python!"

# Count occurrences
count = text.count('o')  # 2

# Find position
position = text.find('Python')  # 7

# Replace
new_text = text.replace('Python', 'World')  # "Hello, World!"

# Split into list
words = text.split(',')  # ['Hello', ' Python!']

# Strip whitespace
clean = "  hello  ".strip()  # "hello"
```

### String Formatting

Multiple ways to format strings:

```python
name = "John"
age = 30

# f-strings (recommended - Python 3.6+)
message = f"My name is {name} and I'm {age} years old"

# .format() method
message = "My name is {} and I'm {} years old".format(name, age)

# % formatting (older style)
message = "My name is %s and I'm %d years old" % (name, age)
```

## Working with Variables

### Variable Reassignment

Variables can be reassigned:

```python
x = 10
print(x)  # 10

x = 20
print(x)  # 20

x = x + 5  # Add 5 to current value
print(x)  # 25
```

### Increment and Decrement

```python
count = 0

# Increment
count = count + 1  # 1
count += 1  # 2 (shorthand)

# Decrement
count = count - 1  # 1
count -= 1  # 0 (shorthand)

# Other operations
count *= 2  # Multiply by 2
count /= 2  # Divide by 2
```

## Working with Data Files (Preview)

### Reading CSV Files with pandas

We'll learn more about this in later lessons, but here's a preview:

```python
import pandas as pd

# Read a CSV file
df = pd.read_csv('data/datasets/employees.csv')

# Display first few rows
print(df.head())

# Get basic info
print(df.info())
```

## Common Operations for Data Analysis

### Calculating Statistics

```python
numbers = [10, 20, 30, 40, 50]

# Sum
total = sum(numbers)  # 150

# Average
average = sum(numbers) / len(numbers)  # 30.0

# Maximum
maximum = max(numbers)  # 50

# Minimum
minimum = min(numbers)  # 10

# Count
count = len(numbers)  # 5
```

### Working with Multiple Values

```python
# Multiple variables
x, y, z = 1, 2, 3

# Swap values
x, y = y, x  # x is now 2, y is now 1

# Unpacking
values = (10, 20, 30)
a, b, c = values
```

## Input/Output Operations

### Getting Input

```python
# String input
name = input("Enter your name: ")

# Number input (need to convert)
age = int(input("Enter your age: "))
price = float(input("Enter price: "))
```

### Displaying Output

```python
# Simple print
print("Hello")

# Print multiple items
print("Name:", "John", "Age:", 30)

# Print with separator
print("A", "B", "C", sep="-")  # A-B-C

# Print without newline
print("Hello", end=" ")
print("World")  # Hello World
```

## Error Handling Basics

### Common Errors

```python
# TypeError: wrong type
# result = "10" + 5  # Error!

# ValueError: wrong value
# age = int("abc")  # Error!

# NameError: undefined variable
# print(undefined_var)  # Error!
```

### Basic Error Prevention

```python
# Check type before operation
value = "10"
if isinstance(value, str):
    value = int(value)
result = value + 5
```

## Best Practices

1. **Use meaningful variable names**: `total_sales` not `ts`
2. **Use f-strings for formatting**: Modern and readable
3. **Check types when needed**: Prevent type errors
4. **Use parentheses for clarity**: `(a + b) * c` is clearer
5. **Comment complex operations**: Explain what's happening

## Practice Examples

```python
# Example 1: Calculate total with tax
price = 100.0
tax_rate = 0.08
tax = price * tax_rate
total = price + tax
print(f"Price: ${price:.2f}, Tax: ${tax:.2f}, Total: ${total:.2f}")

# Example 2: Format employee information
first_name = "John"
last_name = "Smith"
employee_id = 12345
print(f"Employee: {first_name} {last_name} (ID: {employee_id})")

# Example 3: Calculate statistics
scores = [85, 90, 78, 92, 88]
average = sum(scores) / len(scores)
highest = max(scores)
lowest = min(scores)
print(f"Average: {average}, Highest: {highest}, Lowest: {lowest}")
```

## Next Steps

You now have the fundamentals! In the next level, you'll learn about data structures (lists, dictionaries) which are essential for working with data in Python.

---

**Key Takeaways:**
- Python follows standard order of operations (PEMDAS)
- Strings have many useful methods (upper, lower, split, replace, etc.)
- Use f-strings for string formatting (recommended)
- Variables can be reassigned and modified
- Use shorthand operators (`+=`, `-=`, etc.) for convenience
- Basic error prevention: check types and values before operations
