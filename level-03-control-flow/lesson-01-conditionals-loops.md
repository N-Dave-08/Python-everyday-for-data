# Lesson 3.1: Conditionals and Loops

## Conditionals: if/elif/else

Conditionals allow your code to make decisions based on conditions.

### Basic if Statement

```python
age = 20

if age >= 18:
    print("You are an adult")
```

### if/else

```python
age = 15

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

### if/elif/else

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")
```

### Multiple Conditions

```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive")

if age < 18 or age > 65:
    print("Special considerations apply")
```

### Nested Conditionals

```python
temperature = 75
is_sunny = True

if temperature > 70:
    if is_sunny:
        print("Perfect beach weather!")
    else:
        print("Warm but cloudy")
else:
    print("Too cold for beach")
```

## For Loops

For loops iterate over sequences (lists, strings, ranges, etc.).

### Iterating Over Lists

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

### Iterating with Index

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

### Iterating Over Strings

```python
word = "Python"

for char in word:
    print(char)
```

### Using range()

```python
# Range from 0 to 4
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Range from 2 to 6
for i in range(2, 7):
    print(i)  # 2, 3, 4, 5, 6

# Range with step
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

### Iterating Over Dictionaries

```python
person = {"name": "John", "age": 30, "city": "New York"}

# Iterate keys
for key in person:
    print(key, person[key])

# Iterate items
for key, value in person.items():
    print(f"{key}: {value}")
```

## While Loops

While loops repeat as long as a condition is true.

### Basic While Loop

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

### Infinite Loop Prevention

```python
# Always ensure condition can become False
count = 0
max_count = 10

while count < max_count:
    print(count)
    count += 1
    # Without count += 1, this would loop forever!
```

## Loop Control: break and continue

### break

Exit the loop immediately:

```python
for i in range(10):
    if i == 5:
        break  # Exit loop when i is 5
    print(i)
# Output: 0, 1, 2, 3, 4
```

### continue

Skip to the next iteration:

```python
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
# Output: 1, 3, 5, 7, 9
```

## Nested Loops

Loops can be nested inside other loops:

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()  # Blank line between tables
```

## List Comprehensions (Review)

A concise way to create lists:

```python
# Traditional loop
squares = []
for x in range(10):
    squares.append(x**2)

# List comprehension (equivalent)
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(20) if x % 2 == 0]
```

## Common Patterns

### Finding Items

```python
numbers = [1, 2, 3, 4, 5]
target = 3

found = False
for num in numbers:
    if num == target:
        found = True
        break

# Or use 'in'
found = target in numbers
```

### Accumulating Values

```python
numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total += num

print(total)  # 15
```

### Filtering

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)

# Or use list comprehension
evens = [num for num in numbers if num % 2 == 0]
```

## Best Practices

1. **Use descriptive variable names**: `for item in items` not `for i in l`
2. **Use `enumerate()` when you need index**: `for i, item in enumerate(items)`
3. **Use `break` and `continue` sparingly**: Can make code harder to read
4. **Prefer list comprehensions** for simple transformations
5. **Avoid infinite loops**: Always ensure while condition can become False

## Common Pitfalls

### Modifying List While Iterating

```python
# ❌ Don't do this
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Can cause issues

# ✅ Create new list instead
numbers = [num for num in numbers if num % 2 != 0]
```

### Off-by-One Errors

```python
# range(5) gives 0, 1, 2, 3, 4 (not 5!)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

## Next Steps

In the next lesson, you'll learn about functions, which allow you to organize and reuse code.

---

**Key Takeaways:**
- Use `if/elif/else` for conditional execution
- Use `for` loops to iterate over sequences
- Use `while` loops for conditional repetition
- Use `break` to exit loops and `continue` to skip iterations
- List comprehensions provide a concise way to create lists
- Be careful when modifying lists while iterating
