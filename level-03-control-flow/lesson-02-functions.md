# Lesson 3.2: Functions

## What are Functions?

**Functions** are reusable blocks of code that perform a specific task. They help organize code, avoid repetition, and make programs easier to understand and maintain.

### Defining Functions

```python
def greet():
    print("Hello, World!")

# Call the function
greet()  # Output: Hello, World!
```

### Functions with Parameters

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!
```

### Functions with Return Values

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8
```

## Function Parameters

### Multiple Parameters

```python
def calculate_total(price, quantity, tax_rate):
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total

total = calculate_total(10.0, 3, 0.08)
print(total)  # 32.4
```

### Default Parameters

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Hello, Alice!
greet("Bob", "Hi")          # Hi, Bob!
greet("Charlie", "Goodbye") # Goodbye, Charlie!
```

### Keyword Arguments

```python
def create_profile(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

# Positional arguments
create_profile("John", 30, "New York")

# Keyword arguments (order doesn't matter)
create_profile(city="Boston", name="Alice", age=25)
```

### Variable Arguments

```python
# *args (variable positional arguments)
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# **kwargs (variable keyword arguments)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=30, city="NYC")
```

## Return Values

### Single Return

```python
def square(x):
    return x ** 2

result = square(5)  # 25
```

### Multiple Returns

```python
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide(17, 5)
print(f"Quotient: {q}, Remainder: {r}")  # Quotient: 3, Remainder: 2
```

### No Return (Returns None)

```python
def print_message(msg):
    print(msg)
    # No return statement

result = print_message("Hello")
print(result)  # None
```

## Lambda Functions

Anonymous functions defined with `lambda`:

```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square = lambda x: x ** 2

# Use with map, filter, etc.
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]

# Filter with lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]
```

## Scope and Variables

### Local vs Global Scope

```python
x = 10  # Global variable

def my_function():
    x = 20  # Local variable
    print(x)  # 20

my_function()
print(x)  # 10 (global unchanged)

# Access global variable
def another_function():
    global x
    x = 30  # Modifies global
    print(x)  # 30

another_function()
print(x)  # 30
```

## Common Function Patterns

### Data Processing Functions

```python
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

scores = [85, 90, 78, 92, 88]
avg = calculate_average(scores)
print(avg)  # 86.6
```

### Validation Functions

```python
def is_valid_email(email):
    return "@" in email and "." in email

print(is_valid_email("user@example.com"))  # True
print(is_valid_email("invalid"))             # False
```

### Data Transformation Functions

```python
def format_name(first, last):
    return f"{first.capitalize()} {last.capitalize()}"

full_name = format_name("john", "smith")
print(full_name)  # John Smith
```

## Docstrings

Document your functions:

```python
def calculate_total(price, quantity, tax_rate=0.08):
    """
    Calculate the total cost including tax.
    
    Parameters:
    price (float): Unit price
    quantity (int): Number of items
    tax_rate (float): Tax rate (default 0.08)
    
    Returns:
    float: Total cost including tax
    """
    subtotal = price * quantity
    tax = subtotal * tax_rate
    return subtotal + tax
```

## Best Practices

1. **Use descriptive function names**: `calculate_total()` not `calc()`
2. **Keep functions focused**: One function, one purpose
3. **Use docstrings**: Document what your function does
4. **Avoid global variables**: Pass data as parameters
5. **Return values, don't print**: Makes functions reusable
6. **Use default parameters**: For optional arguments

## Common Pitfalls

### Modifying Mutable Default Arguments

```python
# ❌ Don't do this
def add_item(item, items=[]):
    items.append(item)
    return items

# ✅ Use None instead
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### Forgetting Return Statement

```python
# ❌ This returns None
def add(a, b):
    a + b  # Missing return!

# ✅ Always return
def add(a, b):
    return a + b
```

## Next Steps

In the next lesson, you'll learn about error handling, which helps make your code more robust.

---

**Key Takeaways:**
- Functions are reusable blocks of code
- Use `def` to define functions
- Parameters allow functions to accept input
- Use `return` to send values back
- Lambda functions are concise anonymous functions
- Use docstrings to document your functions
- Keep functions focused and reusable
