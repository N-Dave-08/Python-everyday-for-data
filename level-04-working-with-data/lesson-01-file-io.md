# Lesson 4.1: File I/O

## Reading and Writing Files

Python provides built-in functions to work with files. This is essential for data analysis since data often comes from files.

## Opening Files

### Basic File Operations

```python
# Open file for reading
file = open("data.txt", "r")
content = file.read()
file.close()

# Open file for writing
file = open("output.txt", "w")
file.write("Hello, World!")
file.close()
```

### File Modes

- `"r"` - Read (default)
- `"w"` - Write (overwrites existing)
- `"a"` - Append (adds to end)
- `"x"` - Exclusive creation (fails if exists)
- `"b"` - Binary mode
- `"t"` - Text mode (default)
- `"+"` - Read and write

## Using `with` Statement (Recommended)

The `with` statement automatically closes files, even if errors occur:

```python
# Reading
with open("data.txt", "r") as file:
    content = file.read()
# File automatically closed here

# Writing
with open("output.txt", "w") as file:
    file.write("Hello, World!")
# File automatically closed here
```

## Reading Files

### Read Entire File

```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

### Read Line by Line

```python
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes newline
```

### Read All Lines into List

```python
with open("data.txt", "r") as file:
    lines = file.readlines()
    # lines is a list of strings
```

### Read Specific Number of Characters

```python
with open("data.txt", "r") as file:
    first_100 = file.read(100)  # First 100 characters
```

## Writing Files

### Write Text

```python
with open("output.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
```

### Write Multiple Lines

```python
lines = ["Line 1", "Line 2", "Line 3"]

with open("output.txt", "w") as file:
    file.writelines([line + "\n" for line in lines])

# Or use write with join
with open("output.txt", "w") as file:
    file.write("\n".join(lines))
```

### Append to File

```python
with open("output.txt", "a") as file:
    file.write("New line\n")
```

## Working with Paths

### Using `os.path`

```python
import os

# Join paths
path = os.path.join("data", "files", "data.txt")

# Check if file exists
if os.path.exists("data.txt"):
    print("File exists!")

# Get file size
size = os.path.getsize("data.txt")

# Get directory
directory = os.path.dirname("data/files/data.txt")
```

### Using `pathlib` (Modern Approach)

```python
from pathlib import Path

# Create path object
file_path = Path("data") / "files" / "data.txt"

# Check if exists
if file_path.exists():
    print("File exists!")

# Read file
content = file_path.read_text()

# Write file
file_path.write_text("Hello, World!")
```

## Error Handling for Files

```python
try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print(f"Error: {e}")
```

## Common File Operations

### Check File Exists

```python
import os

if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File does not exist")
```

### List Files in Directory

```python
import os

# List all files
files = os.listdir(".")
for file in files:
    print(file)

# List only .txt files
txt_files = [f for f in os.listdir(".") if f.endswith(".txt")]
```

## Best Practices

1. **Always use `with` statement**: Automatic file closing
2. **Handle file errors**: Use try/except for file operations
3. **Use appropriate modes**: "r" for read, "w" for write, "a" for append
4. **Close files explicitly** if not using `with`
5. **Check file existence** before reading
6. **Use pathlib** for modern path handling

## Next Steps

In the next lesson, you'll learn how to work with CSV files, which is the most common format for data analysis.

---

**Key Takeaways:**
- Use `open()` to open files, always close them or use `with`
- File modes: "r" (read), "w" (write), "a" (append)
- Use `with` statement for automatic file closing
- Handle FileNotFoundError and PermissionError
- Use `pathlib` for modern path handling
