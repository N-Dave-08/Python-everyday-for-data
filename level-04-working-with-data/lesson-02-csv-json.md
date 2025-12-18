# Lesson 4.2: Working with CSV and JSON

## CSV Files

**CSV (Comma-Separated Values)** is the most common format for data files. Each line represents a row, and values are separated by commas.

### Reading CSV with Built-in `csv` Module

```python
import csv

# Reading CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list
```

### Reading CSV as Dictionary

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"])  # Access by column name
        print(row)  # Each row is a dictionary
```

### Writing CSV

```python
import csv

data = [
    ["Name", "Age", "City"],
    ["John", "30", "New York"],
    ["Alice", "25", "Boston"]
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

### Writing CSV as Dictionary

```python
import csv

data = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Alice", "age": 25, "city": "Boston"}
]

with open("output.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
```

## Reading CSV with pandas (Recommended)

Pandas makes CSV handling much easier:

```python
import pandas as pd

# Read CSV
df = pd.read_csv("data.csv")

# Display first few rows
print(df.head())

# Get basic info
print(df.info())

# Get statistics
print(df.describe())
```

### Common pandas CSV Options

```python
# Read with specific options
df = pd.read_csv("data.csv", 
                 sep=",",           # Separator
                 header=0,          # Row to use as header
                 index_col=0,       # Column to use as index
                 na_values=["N/A"]) # Values to treat as NaN
```

### Writing CSV with pandas

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "name": ["John", "Alice"],
    "age": [30, 25],
    "city": ["New York", "Boston"]
})

# Write to CSV
df.to_csv("output.csv", index=False)  # index=False avoids writing row numbers
```

## JSON Files

**JSON (JavaScript Object Notation)** is a common format for structured data, especially from APIs.

### Reading JSON

```python
import json

# Read JSON file
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)
```

### Writing JSON

```python
import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "coding"]
}

with open("output.json", "w") as file:
    json.dump(data, file, indent=2)  # indent makes it readable
```

### JSON Strings

```python
import json

# Convert Python object to JSON string
data = {"name": "John", "age": 30}
json_string = json.dumps(data)
print(json_string)  # '{"name": "John", "age": 30}'

# Convert JSON string to Python object
python_obj = json.loads(json_string)
print(python_obj)  # {'name': 'John', 'age': 30}
```

## Working with Data from Files

### Processing CSV Data

```python
import csv

# Read and process
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    total_salary = 0
    count = 0
    
    for row in reader:
        salary = float(row["salary"])
        total_salary += salary
        count += 1
    
    average = total_salary / count
    print(f"Average salary: ${average:.2f}")
```

### Filtering CSV Data

```python
import csv

# Filter employees with salary > 50000
high_earners = []

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if float(row["salary"]) > 50000:
            high_earners.append(row)

print(f"Found {len(high_earners)} high earners")
```

### Working with JSON Data

```python
import json

# Read JSON
with open("data.json", "r") as file:
    data = json.load(file)

# Process data
for person in data["people"]:
    print(f"{person['name']}: {person['age']}")

# Modify and save
data["people"].append({"name": "Bob", "age": 35})

with open("data.json", "w") as file:
    json.dump(data, file, indent=2)
```

## Best Practices

1. **Use pandas for CSV**: Much easier than csv module
2. **Handle missing data**: Check for empty values
3. **Validate data**: Check data types and formats
4. **Use context managers**: Always use `with` statement
5. **Handle encoding**: Specify encoding if needed (`encoding="utf-8"`)
6. **Use `index=False`**: When writing CSV with pandas

## Common Patterns

### Reading Multiple Files

```python
import pandas as pd
import glob

# Read all CSV files in directory
files = glob.glob("data/*.csv")
dataframes = []

for file in files:
    df = pd.read_csv(file)
    dataframes.append(df)

# Combine all dataframes
combined = pd.concat(dataframes, ignore_index=True)
```

### Data Validation

```python
import pandas as pd

df = pd.read_csv("data.csv")

# Check for missing values
print(df.isnull().sum())

# Check data types
print(df.dtypes)

# Check for duplicates
print(df.duplicated().sum())
```

## Next Steps

You now know how to work with files! In the next level, you'll dive deep into pandas, which is the most powerful tool for data analysis in Python.

---

**Key Takeaways:**
- Use `csv` module for basic CSV operations
- Use `pandas.read_csv()` for easier CSV handling (recommended)
- Use `json` module for JSON files
- Always use `with` statement for file operations
- Validate and check data after reading
- Use pandas for complex data operations
