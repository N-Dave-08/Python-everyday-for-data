# Lesson 2.1: Lists and List Operations

## What is a List?

A **list** is an ordered collection of items. Lists are one of Python's most versatile data structures and are essential for working with data.

### Creating Lists

```python
# Empty list
my_list = []

# List with items
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "hello", 3.14, True]  # Can contain different types

# Using list() constructor
another_list = list(range(5))  # [0, 1, 2, 3, 4]
```

## Accessing List Elements

### Indexing

Lists are **zero-indexed** (first element is at index 0):

```python
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])   # "apple" (first element)
print(fruits[1])   # "banana" (second element)
print(fruits[-1])  # "date" (last element)
print(fruits[-2])  # "cherry" (second to last)
```

### Slicing

Extract portions of a list:

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers[2:5]    # [2, 3, 4] (from index 2 to 4, exclusive)
numbers[:3]     # [0, 1, 2] (first 3 elements)
numbers[3:]     # [3, 4, 5, 6, 7, 8, 9] (from index 3 to end)
numbers[:]      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (all elements)
numbers[::2]    # [0, 2, 4, 6, 8] (every 2nd element)
numbers[::-1]   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed)
```

## Modifying Lists

### Adding Elements

```python
fruits = ["apple", "banana"]

# Append (add to end)
fruits.append("cherry")  # ["apple", "banana", "cherry"]

# Insert (add at specific position)
fruits.insert(1, "orange")  # ["apple", "orange", "banana", "cherry"]

# Extend (add multiple items)
fruits.extend(["date", "elderberry"])  # Adds multiple items
```

### Removing Elements

```python
fruits = ["apple", "banana", "cherry", "banana"]

# Remove (removes first occurrence)
fruits.remove("banana")  # ["apple", "cherry", "banana"]

# Pop (removes and returns element)
last = fruits.pop()  # Removes and returns last element
first = fruits.pop(0)  # Removes and returns element at index 0

# Del (delete by index)
del fruits[0]  # Removes first element
```

### Modifying Elements

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"  # ["apple", "orange", "cherry"]
```

## List Methods

### Common Methods

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Length
len(numbers)  # 8

# Count occurrences
numbers.count(1)  # 2

# Find index
numbers.index(4)  # 2 (first occurrence)

# Sort (modifies original)
numbers.sort()  # [1, 1, 2, 3, 4, 5, 6, 9]

# Reverse (modifies original)
numbers.reverse()  # [9, 6, 5, 4, 3, 2, 1, 1]

# Sorted (returns new list, doesn't modify original)
sorted_numbers = sorted(numbers)  # New sorted list
```

## List Comprehensions

A concise way to create lists:

```python
# Basic comprehension
squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# With transformation
words = ["hello", "world", "python"]
lengths = [len(word) for word in words]  # [5, 5, 6]
```

## Working with Lists

### Checking Membership

```python
fruits = ["apple", "banana", "cherry"]

"apple" in fruits   # True
"orange" in fruits  # False
"apple" not in fruits  # False
```

### Iterating Over Lists

```python
fruits = ["apple", "banana", "cherry"]

# For loop
for fruit in fruits:
    print(fruit)

# With index
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

### List Operations

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2  # [1, 2, 3, 4, 5, 6]

# Repetition
repeated = list1 * 3  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Comparison
[1, 2, 3] == [1, 2, 3]  # True
[1, 2, 3] < [1, 2, 4]   # True (lexicographic comparison)
```

## Nested Lists

Lists can contain other lists:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access elements
matrix[0][1]  # 2 (first row, second column)

# Iterate
for row in matrix:
    for element in row:
        print(element)
```

## Common Patterns

### Finding Maximum/Minimum

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

max_value = max(numbers)  # 9
min_value = min(numbers)  # 1
```

### Sum and Average

```python
numbers = [1, 2, 3, 4, 5]

total = sum(numbers)  # 15
average = sum(numbers) / len(numbers)  # 3.0
```

### Copying Lists

```python
original = [1, 2, 3]

# Shallow copy
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

# All create independent copies
```

## Best Practices

1. **Use list comprehensions** for creating lists from other iterables
2. **Use `append()`** to add single items
3. **Use `extend()`** to add multiple items
4. **Be careful with nested lists** - copying may be shallow
5. **Use descriptive variable names** for lists (plural nouns)

## Common Pitfalls

### Modifying While Iterating

```python
# ❌ Don't do this
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Can cause issues

# ✅ Create a new list instead
numbers = [num for num in numbers if num % 2 != 0]
```

### Shallow vs Deep Copy

```python
# Shallow copy (nested lists still reference original)
original = [[1, 2], [3, 4]]
copy = original.copy()
copy[0][0] = 99  # Also modifies original!

# Deep copy (completely independent)
import copy
deep_copy = copy.deepcopy(original)
```

## Next Steps

In the next lesson, you'll learn about dictionaries, which are essential for working with structured data.

---

**Key Takeaways:**
- Lists are ordered, mutable collections
- Use indexing `[0]` and slicing `[1:3]` to access elements
- Lists have many useful methods: `append()`, `remove()`, `sort()`, etc.
- List comprehensions provide a concise way to create lists
- Lists can contain any type of data, including other lists
