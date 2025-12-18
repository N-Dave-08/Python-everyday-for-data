# Lesson 2.3: Sets and Tuples

## Sets

A **set** is an unordered collection of unique elements. Sets are useful for membership testing, removing duplicates, and mathematical set operations.

### Creating Sets

```python
# Empty set (note: use set(), not {})
my_set = set()

# Set with items
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}

# From a list (removes duplicates)
unique_numbers = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}

# Set comprehension
squares = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}
```

### Set Characteristics

- **Unordered**: No indexing, elements have no position
- **Unique**: No duplicate elements
- **Mutable**: Can add/remove elements

```python
my_set = {1, 2, 3}
my_set.add(4)  # {1, 2, 3, 4}
my_set.add(2)  # Still {1, 2, 3, 4} (duplicate ignored)
```

## Set Operations

### Adding and Removing

```python
fruits = {"apple", "banana"}

# Add single element
fruits.add("cherry")  # {"apple", "banana", "cherry"}

# Add multiple elements
fruits.update(["date", "elderberry"])  # Adds multiple

# Remove element (raises KeyError if not found)
fruits.remove("banana")

# Discard element (no error if not found)
fruits.discard("banana")

# Pop (removes and returns arbitrary element)
fruit = fruits.pop()

# Clear all
fruits.clear()  # set()
```

### Set Methods

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union (all elements from both sets)
union = set1 | set2  # {1, 2, 3, 4, 5, 6}
union = set1.union(set2)

# Intersection (common elements)
intersection = set1 & set2  # {3, 4}
intersection = set1.intersection(set2)

# Difference (elements in set1 but not in set2)
difference = set1 - set2  # {1, 2}
difference = set1.difference(set2)

# Symmetric difference (elements in either set, but not both)
sym_diff = set1 ^ set2  # {1, 2, 5, 6}
sym_diff = set1.symmetric_difference(set2)

# Check subset/superset
{1, 2}.issubset({1, 2, 3})  # True
{1, 2, 3}.issuperset({1, 2})  # True
```

### Membership Testing

```python
fruits = {"apple", "banana", "cherry"}

"apple" in fruits   # True
"orange" in fruits  # False
"apple" not in fruits  # False
```

## Common Set Use Cases

### Removing Duplicates

```python
# Remove duplicates from a list
numbers = [1, 2, 2, 3, 3, 3, 4, 5]
unique = list(set(numbers))  # [1, 2, 3, 4, 5]
```

### Fast Membership Testing

```python
# Sets are faster for membership testing than lists
large_list = list(range(1000000))
large_set = set(range(1000000))

# Much faster with sets
999999 in large_set  # Very fast
999999 in large_list  # Slower (has to check each element)
```

## Tuples

A **tuple** is an ordered, immutable collection of elements. Tuples are like lists but cannot be modified after creation.

### Creating Tuples

```python
# Empty tuple
my_tuple = ()

# Tuple with items
coordinates = (10, 20)
person = ("John", 30, "New York")

# Single element tuple (note the comma)
single = (42,)  # Not (42) which is just 42

# Without parentheses (tuple packing)
point = 10, 20  # (10, 20)

# From iterable
tuple_from_list = tuple([1, 2, 3])  # (1, 2, 3)
```

### Tuple Characteristics

- **Ordered**: Elements have positions
- **Immutable**: Cannot modify after creation
- **Can contain any types**: Including other tuples

```python
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment
```

## Accessing Tuple Elements

### Indexing and Slicing

```python
person = ("John", 30, "New York", "Engineer")

# Indexing
name = person[0]      # "John"
age = person[1]         # 30
last = person[-1]      # "Engineer"

# Slicing
first_two = person[:2]  # ("John", 30)
last_two = person[2:]   # ("New York", "Engineer")
```

### Unpacking

```python
# Unpack tuple into variables
person = ("John", 30, "New York")
name, age, city = person
# name = "John", age = 30, city = "New York"

# Unpack with * (collect remaining)
first, *rest = (1, 2, 3, 4, 5)
# first = 1, rest = [2, 3, 4, 5]

# Swap variables
a, b = b, a  # Swaps values
```

## Tuple Operations

### Concatenation and Repetition

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2  # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = tuple1 * 3  # (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

### Tuple Methods

```python
numbers = (1, 2, 3, 2, 4, 2)

# Count occurrences
count = numbers.count(2)  # 3

# Find index
index = numbers.index(3)  # 2

# Length
length = len(numbers)  # 6
```

## When to Use Tuples vs Lists

### Use Tuples When:
- Data shouldn't change (immutability)
- Returning multiple values from a function
- Using as dictionary keys (must be immutable)
- Performance matters (slightly faster than lists)

### Use Lists When:
- Data needs to be modified
- Order matters and may change
- Need to add/remove elements frequently

## Common Patterns

### Returning Multiple Values

```python
def get_name_age():
    return "John", 30  # Returns tuple

name, age = get_name_age()  # Unpacking
```

### Dictionary Keys

```python
# Tuples can be dictionary keys (lists cannot)
locations = {
    (0, 0): "Origin",
    (10, 20): "Point A",
    (30, 40): "Point B"
}
```

### Named Tuples

```python
from collections import namedtuple

# Create a named tuple type
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create instances
person = Person("John", 30, "New York")
print(person.name)  # "John"
print(person.age)    # 30
```

## Best Practices

1. **Use tuples for fixed data**: Coordinates, configurations
2. **Use sets for unique collections**: Removing duplicates, membership testing
3. **Use lists for mutable sequences**: When you need to modify
4. **Use tuple unpacking**: Clean way to assign multiple variables
5. **Use sets for fast lookups**: When membership testing is frequent

## Common Pitfalls

### Modifying Tuples

```python
# ❌ Can't modify tuples
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # TypeError

# ✅ Create a new tuple
my_tuple = (10, 2, 3)
```

### Empty Set vs Empty Dict

```python
# Empty set
my_set = set()  # set()

# Empty dict
my_dict = {}  # {}

# Not this:
# my_set = {}  # This is a dict, not a set!
```

## Next Steps

You now know all the core data structures in Python! In the next level, you'll learn about control flow (if/else, loops) and functions, which will let you write more complex programs.

---

**Key Takeaways:**
- Sets are unordered collections of unique elements
- Sets are great for removing duplicates and fast membership testing
- Tuples are ordered, immutable collections
- Use tuples when data shouldn't change
- Tuple unpacking is a powerful feature
- Sets support mathematical set operations (union, intersection, etc.)
