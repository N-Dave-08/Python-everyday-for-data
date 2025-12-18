# Lesson 2.2: Dictionaries

## What is a Dictionary?

A **dictionary** is an unordered collection of key-value pairs. Dictionaries are perfect for storing and accessing data by meaningful keys rather than numeric indices.

### Creating Dictionaries

```python
# Empty dictionary
my_dict = {}

# Dictionary with items
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Using dict() constructor
person2 = dict(name="Alice", age=25, city="Boston")

# Mixed types
data = {
    "name": "Product A",
    "price": 19.99,
    "in_stock": True,
    "tags": ["electronics", "gadgets"]
}
```

## Accessing Dictionary Values

### Using Keys

```python
person = {"name": "John", "age": 30, "city": "New York"}

# Access by key
name = person["name"]  # "John"
age = person["age"]    # 30

# Using get() (safer - returns None if key doesn't exist)
name = person.get("name")  # "John"
email = person.get("email")  # None (key doesn't exist)
email = person.get("email", "N/A")  # "N/A" (default value)
```

### Checking for Keys

```python
person = {"name": "John", "age": 30}

"name" in person    # True
"email" in person   # False
"name" not in person  # False
```

## Modifying Dictionaries

### Adding and Updating

```python
person = {"name": "John", "age": 30}

# Add new key-value pair
person["city"] = "New York"

# Update existing value
person["age"] = 31

# Update multiple values
person.update({"city": "Boston", "age": 32})
```

### Removing Items

```python
person = {"name": "John", "age": 30, "city": "New York"}

# Remove by key
del person["age"]

# Pop (remove and return value)
city = person.pop("city")  # Returns "New York"

# Popitem (remove and return last item as tuple)
item = person.popitem()  # Returns ("name", "John")

# Clear all items
person.clear()  # {}
```

## Dictionary Methods

### Getting Keys, Values, and Items

```python
person = {"name": "John", "age": 30, "city": "New York"}

# Get all keys
keys = person.keys()  # dict_keys(['name', 'age', 'city'])

# Get all values
values = person.values()  # dict_values(['John', 30, 'New York'])

# Get all key-value pairs
items = person.items()  # dict_items([('name', 'John'), ('age', 30), ...])

# Convert to list if needed
keys_list = list(person.keys())
```

### Other Useful Methods

```python
person = {"name": "John", "age": 30}

# Copy dictionary
person_copy = person.copy()

# Get value with default
email = person.get("email", "N/A")  # "N/A" if key doesn't exist

# Set default value if key doesn't exist
person.setdefault("city", "Unknown")  # Sets "city" to "Unknown" if not present
```

## Iterating Over Dictionaries

### Iterating Keys

```python
person = {"name": "John", "age": 30, "city": "New York"}

# Iterate keys (default)
for key in person:
    print(key, person[key])

# Explicitly iterate keys
for key in person.keys():
    print(key)
```

### Iterating Values

```python
# Iterate values
for value in person.values():
    print(value)
```

### Iterating Items

```python
# Iterate key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
```

## Dictionary Comprehensions

Create dictionaries concisely:

```python
# Basic comprehension
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# From two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
mapping = {k: v for k, v in zip(keys, values)}  # {'a': 1, 'b': 2, 'c': 3}

# With condition
evens = {x: x*2 for x in range(10) if x % 2 == 0}
```

## Nested Dictionaries

Dictionaries can contain other dictionaries:

```python
employees = {
    "emp1": {
        "name": "John",
        "age": 30,
        "department": "Engineering"
    },
    "emp2": {
        "name": "Alice",
        "age": 25,
        "department": "Marketing"
    }
}

# Access nested values
name = employees["emp1"]["name"]  # "John"
dept = employees["emp2"]["department"]  # "Marketing"
```

## Common Patterns

### Counting with Dictionaries

```python
# Count occurrences
text = "hello world"
counts = {}
for char in text:
    counts[char] = counts.get(char, 0) + 1
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# Using Counter (from collections module)
from collections import Counter
counts = Counter(text)
```

### Grouping Data

```python
# Group items by category
items = [
    {"name": "apple", "category": "fruit"},
    {"name": "banana", "category": "fruit"},
    {"name": "carrot", "category": "vegetable"}
]

grouped = {}
for item in items:
    category = item["category"]
    if category not in grouped:
        grouped[category] = []
    grouped[category].append(item["name"])
# {'fruit': ['apple', 'banana'], 'vegetable': ['carrot']}
```

### Merging Dictionaries

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Python 3.9+
merged = dict1 | dict2  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Older Python versions
merged = {**dict1, **dict2}
merged = dict1.copy()
merged.update(dict2)
```

## Best Practices

1. **Use meaningful keys**: `person["name"]` not `person["n"]`
2. **Use `get()` for safe access**: Prevents KeyError
3. **Use dictionary comprehensions** for creating dictionaries
4. **Keep keys immutable**: Use strings, numbers, or tuples as keys
5. **Use `items()` when you need both keys and values**

## Common Pitfalls

### KeyError

```python
# ❌ This raises KeyError if key doesn't exist
value = person["email"]

# ✅ Use get() instead
value = person.get("email", "N/A")
```

### Mutable Keys

```python
# ❌ Lists can't be keys (they're mutable)
# my_dict = {[1, 2]: "value"}  # TypeError

# ✅ Use tuples instead (they're immutable)
my_dict = {(1, 2): "value"}  # OK
```

### Shallow Copy

```python
# Shallow copy (nested dicts still reference original)
original = {"nested": {"a": 1}}
copy = original.copy()
copy["nested"]["a"] = 2  # Also modifies original!

# Deep copy
import copy
deep_copy = copy.deepcopy(original)
```

## Next Steps

In the next lesson, you'll learn about sets and tuples, which complete the core data structures in Python.

---

**Key Takeaways:**
- Dictionaries store key-value pairs
- Access values using keys: `dict["key"]` or `dict.get("key")`
- Dictionaries are mutable and unordered
- Use `items()`, `keys()`, and `values()` to iterate
- Dictionary comprehensions provide a concise way to create dictionaries
- Dictionaries are perfect for structured data and lookups
