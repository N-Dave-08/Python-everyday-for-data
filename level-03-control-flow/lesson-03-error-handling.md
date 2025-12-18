# Lesson 3.3: Error Handling

## What is Error Handling?

**Error handling** allows your program to gracefully handle unexpected situations (errors/exceptions) instead of crashing.

## Common Errors

### SyntaxError

```python
# Missing colon
if x > 5  # SyntaxError: expected ':'

# Incorrect indentation
if x > 5:
print("Hello")  # IndentationError
```

### TypeError

```python
# Wrong type operation
"10" + 5  # TypeError: can only concatenate str to str

# Wrong number of arguments
def add(a, b):
    return a + b
add(1)  # TypeError: missing required argument
```

### ValueError

```python
# Invalid value
int("abc")  # ValueError: invalid literal for int()
```

### KeyError

```python
# Key doesn't exist
person = {"name": "John"}
person["age"]  # KeyError: 'age'
```

### IndexError

```python
# Index out of range
numbers = [1, 2, 3]
numbers[5]  # IndexError: list index out of range
```

## try/except Blocks

### Basic Error Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Handling Multiple Exceptions

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Catching All Exceptions

```python
try:
    # Some code
    result = risky_operation()
except Exception as e:
    print(f"An error occurred: {e}")
```

### else Clause

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero!")
else:
    print(f"Result: {result}")  # Only runs if no exception
```

### finally Clause

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()  # Always executes, even if error occurs
```

## Raising Exceptions

### Raise Your Own Exceptions

```python
def calculate_age(birth_year):
    if birth_year > 2024:
        raise ValueError("Birth year cannot be in the future!")
    return 2024 - birth_year

try:
    age = calculate_age(2030)
except ValueError as e:
    print(f"Error: {e}")
```

### Custom Exception Messages

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed!")
    return a / b
```

## Common Error Handling Patterns

### Input Validation

```python
def get_positive_number():
    while True:
        try:
            number = float(input("Enter a positive number: "))
            if number <= 0:
                raise ValueError("Number must be positive!")
            return number
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

number = get_positive_number()
```

### File Operations

```python
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
        return None
    except PermissionError:
        print(f"Permission denied to read '{filename}'!")
        return None
```

### Dictionary Access

```python
person = {"name": "John", "age": 30}

# Safe access
try:
    email = person["email"]
except KeyError:
    email = "N/A"

# Or use get()
email = person.get("email", "N/A")
```

### List Operations

```python
numbers = [1, 2, 3]

# Safe indexing
try:
    value = numbers[5]
except IndexError:
    value = None
    print("Index out of range!")

# Or check length first
if len(numbers) > 5:
    value = numbers[5]
else:
    value = None
```

## Best Practices

1. **Be specific**: Catch specific exceptions, not all
2. **Don't ignore errors**: At least log them
3. **Use finally for cleanup**: Close files, connections, etc.
4. **Provide helpful messages**: Tell users what went wrong
5. **Validate input early**: Check before processing

## Common Patterns

### Retry Logic

```python
def fetch_data(max_retries=3):
    for attempt in range(max_retries):
        try:
            # Attempt to fetch data
            return get_data()
        except ConnectionError:
            if attempt == max_retries - 1:
                raise
            print(f"Retry {attempt + 1}/{max_retries}...")
```

### Context Managers (with statement)

```python
# Automatically handles file closing
with open("data.txt", "r") as f:
    content = f.read()
# File is automatically closed here, even if error occurs
```

## Next Steps

You now have the fundamentals of Python! In the next level, you'll learn how to work with files and data formats (CSV, JSON), which is essential for data analysis.

---

**Key Takeaways:**
- Use `try/except` to handle errors gracefully
- Catch specific exceptions when possible
- Use `else` for code that runs when no error occurs
- Use `finally` for cleanup code that always runs
- Raise exceptions with `raise` for invalid conditions
- Validate input and handle errors early
