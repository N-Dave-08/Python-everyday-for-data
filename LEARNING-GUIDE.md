# Learning Guide: How to Use This Course

This guide explains the complete learning workflow: how to progress, where to save solutions, how to run Python code, and how to validate your answers.

## 📚 Learning Flow

### Step 1: Set Up Your Environment

1. **Install Python** (Recommended: Python 3.8 or higher)
   - **Download**: https://www.python.org/downloads/
   - **Windows**: 
     - Download the installer from python.org
     - **Important**: Check "Add Python to PATH" during installation
     - Verify installation: Open Command Prompt and type `python --version`
   - **macOS**: 
     - `brew install python3` or download from python.org
     - Verify: `python3 --version`
   - **Linux**: 
     - `sudo apt-get install python3 python3-pip` (Ubuntu/Debian)
     - Verify: `python3 --version`
   
   **Verify Python is installed:**
   - **Windows**: Open Command Prompt → `python --version` (should show Python 3.x.x)
   - **macOS/Linux**: Open Terminal → `python3 --version` (should show Python 3.x.x)

2. **Set Up the Course Data**

   **Method A: Using Python Script (Recommended - Easiest!)**

   This is the easiest method - you can do everything from VS Code/Cursor!

   **Step 2A.1: Install Required Packages**
   - Open VS Code/Cursor
   - Open a terminal in VS Code/Cursor (`Ctrl+`` or `View → Terminal`)
   - Navigate to the course directory:
     ```bash
     cd d:\DIRECTORY\projects\Python-everyday-for-data
     ```
   - Install required packages:
     ```bash
     pip install pandas numpy matplotlib seaborn requests beautifulsoup4
     ```
     Or if using Python 3 specifically:
     ```bash
     pip3 install pandas numpy matplotlib seaborn requests beautifulsoup4
     ```

   **Step 2A.2: Run the Setup Script**
   - Navigate to the `data/` folder in your terminal
   - Run the setup script:
     ```bash
     python setup.py
     ```
     Or:
     ```bash
     python3 setup.py
     ```
   - The script will create sample datasets in CSV format
   - You should see messages like:
     - "Creating employees dataset..."
     - "Creating products dataset..."
     - "Setup complete!"

   **Step 2A.3: Verify Setup**
   - Check that CSV files exist in `data/datasets/`:
     - `employees.csv`
     - `products.csv`
     - `customers.csv`
     - `orders.csv`
     - etc.
   - You can verify by opening one file or running:
     ```python
     import pandas as pd
     df = pd.read_csv('data/datasets/employees.csv')
     print(f"Employees dataset: {len(df)} rows")
     ```

   **Method B: Using Command Line (Alternative)**

   If you prefer using the command line:

   ```bash
   # Navigate to course directory
   cd d:\DIRECTORY\projects\Python-everyday-for-data
   
   # Install packages
   pip install pandas numpy matplotlib seaborn requests beautifulsoup4
   
   # Run setup
   cd data
   python setup.py
   ```

3. **Verify Setup**

   Create a test file `test_setup.py`:
   ```python
   import pandas as pd
   import numpy as np
   
   # Test reading data
   df = pd.read_csv('data/datasets/employees.csv')
   print(f"✓ Employees dataset: {len(df)} rows")
   print(f"✓ Setup successful!")
   ```

   Run it:
   ```bash
   python test_setup.py
   ```

   **Quick Verification Checklist:**
   - [ ] Python 3.8+ is installed
   - [ ] Required packages are installed (pandas, numpy, matplotlib, seaborn)
   - [ ] CSV files exist in `data/datasets/`
   - [ ] Can import pandas and read CSV files without errors

### Step 2: Follow the Learning Path

For each level, follow this sequence:

1. **Read the Lessons** (in order)
   - Start with `lesson-01-*.md`
   - Read through all lessons in the level
   - Type out and run the example code yourself
   - Experiment with modifying the examples

2. **Attempt the Exercises**
   - Open `exercises-*.md`
   - Read each exercise carefully
   - Write your Python solution in a `.py` file in the same level folder
   - Run it directly in your IDE or terminal (see "How to Run Your Python Code" below)

3. **Run Your Solution**
   - Execute your Python script
   - Check for syntax errors
   - Review the output

4. **Validate Your Solution**
   - Compare your output with expected format
   - Check data correctness
   - Verify calculations
   - Use validation techniques (see below)

5. **Iterate if Needed**
   - If code doesn't work, read the error message carefully
   - Review relevant lesson sections
   - Check hints (only if stuck)
   - Refine until correct

6. **Move to Next Level**
   - Once all exercises are complete and validated
   - Move to the next level

## 💾 Where to Save Your Solutions

### Recommended: Save in Level Folders

Save your solutions directly in each level's folder:

```
Python-everyday-for-data/
├── level-01-fundamentals/
│   ├── lesson-01-introduction.md
│   ├── lesson-02-variables-types.md
│   ├── exercises-01.md
│   └── my-solutions-01.py  ← Your solutions here
├── level-02-data-structures/
│   ├── lesson-01-lists.md
│   ├── lesson-02-dictionaries.md
│   ├── exercises-02.md
│   └── my-solutions-02.py  ← Your solutions here
└── ... (one solution file per level)
```

### Solution File Format

Save your solutions in `.py` files with clear comments:

```python
# ============================================
# Level 1: Python Fundamentals
# ============================================

# Exercise 1: Basic Variables
# Create variables for a person's name, age, and city.

name = "John Smith"
age = 30
city = "New York"

print(f"Name: {name}, Age: {age}, City: {city}")

# Exercise 2: Data Types
# Determine the type of different values.

value1 = 42
value2 = 3.14
value3 = "Hello"

print(f"Type of {value1}: {type(value1)}")
print(f"Type of {value2}: {type(value2)}")
print(f"Type of {value3}: {type(value3)}")

# Exercise 3: Basic Operations
# ... (continue for all exercises)
```

### Alternative: One File Per Exercise

If you prefer, create separate files in each level folder:

```
level-01-fundamentals/
├── exercises-01.md
├── my-exercise-01.py
├── my-exercise-02.py
└── ...
```

## 🚀 How to Run Your Python Code

### Recommended: Run Python Directly in Your IDE

**This is the easiest method!** Run Python code directly in VS Code/Cursor.

#### Complete Guide: Using VS Code/Cursor

**For Python:**

1. **Install Python Extension**
   - Open Extensions (`Ctrl+Shift+X` or `Cmd+Shift+X` on Mac)
   - Search for "Python" by Microsoft
   - Click "Install"
   - This extension provides syntax highlighting, IntelliSense, and debugging

2. **Select Python Interpreter**
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
   - Type "Python: Select Interpreter"
   - Choose your Python installation (should show Python 3.x.x)

3. **Run Python Code - Multiple Methods**

   **Method 1: Right-Click Menu (Easiest)**
   - Open your `.py` file (e.g., `level-01-fundamentals/my-solutions-01.py`)
   - Right-click in the editor
   - Choose "Run Python File in Terminal"
   - Results appear in the terminal below

   **Method 2: Run Button**
   - Look for a "Run" button (▶️) in the top-right corner of the editor
   - Click the "Run" button
   - Code executes in the terminal

   **Method 3: Keyboard Shortcut**
   - Press `F5` to run the current file
   - Or `Ctrl+F5` to run without debugging

   **Method 4: Terminal**
   - Open terminal (`Ctrl+`` or `View → Terminal`)
   - Navigate to the file's directory
   - Run: `python my-solutions-01.py` (or `python3` on Mac/Linux)

   **Method 5: Run Selection**
   - Select specific code lines
   - Right-click → "Run Selection/Line in Python Terminal"
   - Only the selected code runs

4. **View and Work with Output**
   - Output appears in the terminal panel below
   - **Print statements**: Display in terminal
   - **Errors**: Show with traceback information
   - **DataFrames**: Display as formatted tables (with pandas)
   - **Plots**: Open in separate windows (with matplotlib)

5. **Tips for Running Code**
   - **Save First**: Always save your `.py` file before running (`Ctrl+S`)
   - **Check Terminal**: Output and errors appear in the terminal
   - **Multiple Files**: You can run different files independently
   - **Interactive Mode**: Use `python` or `python3` in terminal for interactive sessions
   - **Jupyter Notebooks**: Can also use Jupyter for interactive coding (optional)

#### Quick Start Example: Complete Workflow

**Step-by-Step Example:**

1. **Install Python** (if not already installed)
   - Download from https://www.python.org/downloads/
   - Check "Add Python to PATH" during installation

2. **Install Python Extension**
   - Open Extensions (`Ctrl+Shift+X`)
   - Search "Python" by Microsoft
   - Click "Install"

3. **Select Python Interpreter**
   - Press `Ctrl+Shift+P`
   - Type "Python: Select Interpreter"
   - Choose Python 3.x.x

4. **Install Required Packages**
   - Open terminal (`Ctrl+``)
   - Run: `pip install pandas numpy matplotlib seaborn`

5. **Create and Run Your First Script**
   - Create `level-01-fundamentals/my-solutions-01.py`
   - Write your code:
     ```python
     # Exercise 1: Hello World
     print("Hello, Python!")
     ```
   - Right-click → "Run Python File in Terminal"
   - See output in terminal!

6. **Quick Tips for Python Extension:**
   - **IntelliSense**: Auto-completion as you type
   - **Syntax Highlighting**: Color-coded code
   - **Error Detection**: Red underlines for errors
   - **Debugging**: Set breakpoints and debug step-by-step
   - **Formatting**: Auto-format code (`Shift+Alt+F`)
   - **Linting**: Get suggestions for code improvements

### Alternative Methods

#### Method 1: Command Line

```bash
# Navigate to file directory
cd level-01-fundamentals

# Run Python file
python my-solutions-01.py

# Or on Mac/Linux
python3 my-solutions-01.py
```

#### Method 2: Interactive Python (REPL)

```bash
# Start Python interactive session
python

# Or
python3

# Then type code directly:
>>> print("Hello, Python!")
Hello, Python!
>>> exit()
```

#### Method 3: Jupyter Notebooks (Optional)

1. Install Jupyter:
   ```bash
   pip install jupyter
   ```

2. Start Jupyter:
   ```bash
   jupyter notebook
   ```

3. Create a new notebook and run cells

## ✅ How to Validate Your Solutions

### Validation Method 1: Compare Output Format

Check if your results match the expected format:

**Expected:**
```
Name: John Smith
Age: 30
City: New York
```

**Your Output Should:**
- Match the format exactly
- Have correct values
- Display properly formatted

### Validation Method 2: Check Data Correctness

```python
# Exercise asks for employees with salary > 75000
# First, check how many should be returned:
import pandas as pd
df = pd.read_csv('data/datasets/employees.csv')
high_salary = df[df['salary'] > 75000]
print(f"Expected count: {len(high_salary)}")

# Your solution should return the same count
```

### Validation Method 3: Verify Calculations

**For calculation exercises:**
```python
# Your solution
result = calculate_average([10, 20, 30, 40, 50])

# Validation: Manually verify
expected = (10 + 20 + 30 + 40 + 50) / 5
assert result == expected, f"Expected {expected}, got {result}"
print("✓ Calculation correct!")
```

### Validation Method 4: Use Test Queries

Create validation code to check your solution:

```python
# Exercise: Filter employees in department 1
# Your solution:
dept1_employees = df[df['department_id'] == 1]

# Validation:
print(f"Total rows: {len(dept1_employees)}")
print(f"Unique departments: {dept1_employees['department_id'].nunique()}")
print(f"All in dept 1: {(dept1_employees['department_id'] == 1).all()}")
# Should all be True
```

### Validation Method 5: Compare with Expected Logic

**For data manipulation exercises:**
```python
# Your solution processes data
processed_df = process_data(df)

# Validation: Check data integrity
assert len(processed_df) > 0, "Result should not be empty"
assert not processed_df.isnull().any().any(), "No null values expected"
print("✓ Data processing correct!")
```

### Validation Method 6: Check for Common Mistakes

**Missing imports:**
```python
# Wrong: Forgetting to import
df = read_csv('data.csv')  # Error: name 'read_csv' is not defined

# Correct:
import pandas as pd
df = pd.read_csv('data.csv')
```

**Wrong data types:**
```python
# Check if you're using correct types
print(type(variable))  # Verify it's what you expect
```

## 📝 Validation Checklist

For each exercise, verify:

- [ ] Code runs without errors
- [ ] Output matches expected format
- [ ] Data values are correct (not just structure)
- [ ] Calculations are accurate (if applicable)
- [ ] Data filtering is correct (if applicable)
- [ ] All required columns/fields are present (if applicable)

## 🔍 Debugging Tips

### If Your Code Doesn't Work

1. **Check Syntax**
   ```python
   # Common errors:
   # Missing colons after if/for/while
   # Incorrect indentation
   # Missing quotes around strings
   # Wrong variable names
   ```

2. **Test Incrementally**
   ```python
   # Start simple
   print("Hello")
   
   # Add complexity step by step
   name = "John"
   print(f"Hello, {name}")
   
   # Add more logic
   if name:
       print(f"Hello, {name}!")
   ```

3. **Use Print Statements**
   ```python
   # Add print statements to debug
   value = 42
   print(f"Value is: {value}")  # See what value actually is
   print(f"Type is: {type(value)}")  # Check the type
   ```

4. **Check Error Messages**
   - Python error messages are usually very helpful
   - Read the error message carefully
   - Check the line number mentioned
   - Look at the error type (SyntaxError, NameError, TypeError, etc.)

### Common Python Errors

**NameError: name 'x' is not defined**
- Variable not defined or typo in variable name

**TypeError: unsupported operand type**
- Trying to use incompatible types (e.g., string + int)

**IndentationError**
- Incorrect indentation (Python is indentation-sensitive)

**FileNotFoundError**
- File path is incorrect or file doesn't exist

**ImportError: No module named 'x'**
- Package not installed or wrong import name

## 🎯 Example: Complete Workflow

### Exercise: "Find employees with salary > 75000"

1. **Read the exercise** in `exercises-01.md`

2. **Write your solution** in `level-01-fundamentals/my-solutions-01.py`:
   ```python
   # Exercise 2: Filtering Data
   import pandas as pd
   
   # Read the data
   df = pd.read_csv('data/datasets/employees.csv')
   
   # Filter employees with salary > 75000
   high_salary = df[df['salary'] > 75000]
   
   # Display results
   print(high_salary[['first_name', 'last_name', 'salary']])
   ```

3. **Run the code** in your IDE:
   - Make sure you're in the correct directory
   - Right-click → "Run Python File in Terminal"
   - Results appear in the terminal

4. **Validate:**
   ```python
   # Check row count
   print(f"Number of employees: {len(high_salary)}")
   
   # Verify all salaries are actually > 75000
   print(f"Min salary: {high_salary['salary'].min()}")
   assert high_salary['salary'].min() > 75000
   ```

5. **Check output format:**
   - Correct columns displayed ✓
   - All salaries > 75000 ✓
   - Correct number of rows ✓

6. **Mark as complete** and move to next exercise

## 📊 Progress Tracking

Create a simple progress tracker:

```markdown
# My Progress

## Level 1: Fundamentals
- [x] Lesson 1.1: Introduction
- [x] Lesson 1.2: Variables and Types
- [x] Lesson 1.3: Basic Operations
- [x] Exercises 1-8: Completed

## Level 2: Data Structures
- [ ] Lesson 2.1: Lists
- [ ] Lesson 2.2: Dictionaries
- [ ] Exercises 1-9: In Progress
```

## 🆘 Getting Help

If you're stuck:

1. **Review the lesson** - Re-read relevant sections
2. **Check hints** - Expand hints in exercise file
3. **Test with simpler code** - Break down the problem
4. **Check Python syntax** - Refer to `resources/python-cheatsheet.md`
5. **Validate step by step** - Test each part of your code
6. **Read error messages** - Python errors are usually very descriptive

## 🎓 Next Steps After Completing

1. **Review your solutions** - Look for patterns and improvements
2. **Try variations** - Modify exercises with your own twists
3. **Build projects** - Apply Python to real problems
4. **Practice online** - Use platforms mentioned in `resources/practice-datasets.md`
5. **Continue learning** - Explore advanced Python features

---

**Remember**: The goal is understanding, not speed. Take your time, experiment, and validate thoroughly. Good luck with your Python learning journey! 🚀
