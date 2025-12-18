# Lesson 1.2: Variables, Data Types, and Basic Operations

## Variables

A **variable** is a name that refers to a value stored in memory. Think of it as a labeled container that holds data.

### Creating Variables

In Python, you create variables by assigning a value to a name:

```python
name = "John"
age = 30
height = 5.9
```

**Rules for variable names:**
- Must start with a letter or underscore
- Can contain letters, numbers, and underscores
- Case sensitive (`name` ≠ `Name`)
- Cannot be Python keywords (like `if`, `for`, `print`)
- Use descriptive names (e.g., `employee_name` not `n`)

### Variable Assignment

```python
# Simple assignment
x = 10

# Multiple assignment
a, b, c = 1, 2, 3

# Same value to multiple variables
x = y = z = 0
```

## Data Types

Python has several built-in data types. Let's explore the most important ones:

### 1. Integers (int)

Whole numbers (positive, negative, or zero):

```python
age = 30
count = -5
zero = 0
large_number = 1000000
```

### 2. Floats (float)

Decimal numbers:

```python
price = 19.99
temperature = -5.5
pi = 3.14159
```

### 3. Strings (str)

Text data enclosed in quotes:

```python
name = "John"
message = 'Hello, World!'
description = """This is a
multi-line string"""
```

**String Operations:**
```python
first_name = "John"
last_name = "Smith"

# Concatenation
full_name = first_name + " " + last_name  # "John Smith"

# Repetition
greeting = "Hello! " * 3  # "Hello! Hello! Hello! "

# Length
length = len(first_name)  # 4
```

### 4. Booleans (bool)

True or False values:

```python
is_active = True
is_complete = False
```

### 5. None

Represents the absence of a value:

```python
value = None
```

## Checking Data Types

Use the `type()` function to check a variable's type:

```python
x = 42
print(type(x))  # <class 'int'>

name = "Python"
print(type(name))  # <class 'str'>

price = 19.99
print(type(price))  # <class 'float'>

is_valid = True
print(type(is_valid))  # <class 'bool'>
```

## Type Conversion

Convert between types using built-in functions:

```python
# Convert to integer
x = int(3.14)  # 3
y = int("42")  # 42

# Convert to float
a = float(5)  # 5.0
b = float("3.14")  # 3.14

# Convert to string
c = str(42)  # "42"
d = str(3.14)  # "3.14"

# Convert to boolean
e = bool(1)  # True
f = bool(0)  # False
g = bool("")  # False
h = bool("Hello")  # True
```

## Basic Operations

### Arithmetic Operations

```python
# Addition
sum = 10 + 5  # 15

# Subtraction
difference = 10 - 5  # 5

# Multiplication
product = 10 * 5  # 50

# Division (always returns float)
quotient = 10 / 5  # 2.0

# Floor Division (integer division)
floor = 10 // 3  # 3

# Modulus (remainder)
remainder = 10 % 3  # 1

# Exponentiation
power = 2 ** 3  # 8
```

### String Operations

```python
# Concatenation
greeting = "Hello" + " " + "World"  # "Hello World"

# Repetition
stars = "*" * 5  # "*****"

# Formatting (f-strings - recommended)
name = "John"
age = 30
message = f"My name is {name} and I'm {age} years old"
# "My name is John and I'm 30 years old"
```

### Comparison Operations

```python
# Equal to
5 == 5  # True
5 == 3  # False

# Not equal to
5 != 3  # True
5 != 5  # False

# Greater than
5 > 3  # True
3 > 5  # False

# Less than
3 < 5  # True
5 < 3  # False

# Greater than or equal to
5 >= 5  # True
5 >= 3  # True

# Less than or equal to
3 <= 5  # True
5 <= 5  # True
```

### Logical Operations

```python
# AND
True and True  # True
True and False  # False

# OR
True or False  # True
False or False  # False

# NOT
not True  # False
not False  # True
```

## Working with Numbers

### Common Math Operations

```python
# Absolute value
abs(-5)  # 5

# Round
round(3.14159, 2)  # 3.14

# Maximum
max(1, 5, 3)  # 5

# Minimum
min(1, 5, 3)  # 1

# Sum
sum([1, 2, 3, 4, 5])  # 15
```

## Input and Output

### Getting User Input

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert to integer
```

### Displaying Output

```python
# Print function
print("Hello, World!")

# Print multiple values
print("Name:", "John", "Age:", 30)

# Print with formatting
name = "John"
age = 30
print(f"Name: {name}, Age: {age}")
```

## Common Pitfalls

### 1. String vs Number Operations

```python
# ❌ This won't work as expected
result = "10" + 5  # TypeError: can only concatenate str to str

# ✅ Convert first
result = int("10") + 5  # 15
```

### 2. Integer Division

```python
# Division always returns float
result = 10 / 2  # 5.0 (not 5)

# Use floor division for integers
result = 10 // 2  # 5
```

### 3. Variable Names

```python
# ❌ Can't use keywords
if = 5  # SyntaxError: invalid syntax

# ✅ Use descriptive names
condition = 5
```

## Best Practices

1. **Use descriptive variable names**: `employee_name` not `n`
2. **Use f-strings for formatting**: `f"Hello, {name}"`
3. **Check types when needed**: Use `type()` to verify
4. **Convert types explicitly**: Don't rely on implicit conversions
5. **Use meaningful names**: Code should be self-documenting

## Practice Examples

Try these examples:

```python
# 1. Create variables for a person
name = "Alice"
age = 25
height = 5.6
is_student = True

# 2. Perform calculations
total = 100
discount = 0.15
final_price = total * (1 - discount)
print(f"Final price: ${final_price}")

# 3. String operations
first = "Hello"
second = "World"
greeting = f"{first}, {second}!"
print(greeting)

# 4. Type checking
value = 42
print(f"Value: {value}, Type: {type(value)}")
```

## Next Steps

In the next lesson, you'll learn about more complex data structures like lists and dictionaries, which are essential for working with data.

---

**Key Takeaways:**
- Variables store values and are created with assignment (`=`)
- Python has several data types: int, float, str, bool, None
- Use `type()` to check a variable's type
- Convert types explicitly using `int()`, `float()`, `str()`, `bool()`
- Python supports arithmetic, comparison, and logical operations
- Use f-strings for string formatting: `f"Hello, {name}"`
