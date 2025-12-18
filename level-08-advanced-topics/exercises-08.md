# Level 8 Exercises: Advanced Topics

Complete these exercises to practice working with APIs, web scraping, and machine learning basics.

## Exercise 1: Basic API Request
**Difficulty: Beginner**

1. Use the JSONPlaceholder API (https://jsonplaceholder.typicode.com/posts)
2. Fetch the first 10 posts
3. Convert the data to a pandas DataFrame
4. Display the title and body of each post

**Expected Output Format:**
```
Post 1: sunt aut facere...
Body: quia et suscipit...
---
Post 2: qui est esse...
...
```

---

## Exercise 2: API Data Analysis
**Difficulty: Intermediate**

1. Fetch all posts from JSONPlaceholder API
2. Count posts by user ID
3. Find the user with the most posts
4. Calculate average post title length
5. Create a visualization showing posts per user

**Expected Output Format:**
```
Total posts: 100
User with most posts: User 1 (10 posts)
Average title length: 44.5 characters
```

---

## Exercise 3: Error Handling for APIs
**Difficulty: Intermediate**

1. Create a function that fetches data from an API
2. Handle connection errors
3. Handle timeout errors
4. Handle invalid status codes
5. Test with both valid and invalid URLs

**Expected Output Format:**
```
Successfully fetched data
Error: Connection timeout
Error: Invalid status code: 404
```

---

## Exercise 4: Web Scraping Basics
**Difficulty: Intermediate**

1. Scrape a simple webpage (use a test site or create your own)
2. Extract all headings (h1, h2, h3)
3. Extract all links
4. Extract all paragraph text
5. Save the extracted data to a CSV file

**Note**: Be respectful - only scrape sites that allow it or use test pages.

**Expected Output Format:**
```
Found 3 headings
Found 10 links
Found 5 paragraphs
Data saved to scraped_data.csv
```

---

## Exercise 5: Scraping Tables
**Difficulty: Intermediate**

1. Find a webpage with a table (or use a test page)
2. Extract the table data
3. Convert to pandas DataFrame
4. Perform basic analysis (mean, sum, etc.)
5. Save to CSV

**Expected Output Format:**
```
Table extracted: 10 rows, 5 columns
Average value: 42.5
Data saved to table_data.csv
```

---

## Exercise 6: Simple Linear Regression
**Difficulty: Intermediate**

Using your employees dataset:
1. Prepare data: Use 'age' as feature, 'salary' as target
2. Split data into train/test sets (80/20)
3. Train a linear regression model
4. Make predictions on test set
5. Calculate and display error metrics (MSE, R²)

**Expected Output Format:**
```
Training samples: 12
Test samples: 3
Mean Squared Error: 1234567.89
R² Score: 0.75
```

---

## Exercise 7: Classification
**Difficulty: Advanced**

Create a simple classification problem:
1. Use employees data
2. Create a binary target: 'high_earner' (salary > 75000)
3. Use 'age' and 'department_id' as features
4. Train a logistic regression model
5. Evaluate with accuracy score and classification report

**Expected Output Format:**
```
Accuracy: 0.87
Classification Report:
              precision    recall  f1-score   support
       False       0.85      0.92      0.88         6
        True       0.90      0.82      0.86         6
```

---

## Exercise 8: Data Preprocessing
**Difficulty: Intermediate**

1. Load a dataset with missing values
2. Check for missing values
3. Fill missing values (use appropriate strategy)
4. Scale the numerical features
5. Prepare data for ML model

**Expected Output Format:**
```
Missing values:
  age: 2
  salary: 1
After preprocessing:
  Missing values: 0
  Features scaled: Yes
```

---

## Exercise 9: Clustering
**Difficulty: Advanced**

Using employees data:
1. Select numerical features (age, salary)
2. Scale the features
3. Apply K-Means clustering (k=3)
4. Visualize clusters with scatter plot
5. Analyze cluster characteristics

**Expected Output Format:**
```
Cluster 0: 5 employees, avg salary: $65000
Cluster 1: 6 employees, avg salary: $80000
Cluster 2: 4 employees, avg salary: $90000
```

---

## Exercise 10: Complete ML Pipeline
**Difficulty: Advanced**

Create a complete machine learning pipeline:
1. Load and explore data
2. Handle missing values and outliers
3. Feature engineering (create new features if needed)
4. Split data
5. Train multiple models (Linear Regression, Random Forest)
6. Compare model performance
7. Make predictions and visualize results

**Expected Output Format:**
```
Data loaded: 15 samples
Features prepared: 3 features
Model Comparison:
  Linear Regression: MSE = 1234567, R² = 0.75
  Random Forest: MSE = 987654, R² = 0.82
Best model: Random Forest
```

---

## Hints

<details>
<summary>Hint for Exercise 1</summary>
Use `requests.get()`, check status code, use `response.json()`, convert to DataFrame with `pd.DataFrame()`.
</details>

<details>
<summary>Hint for Exercise 2</summary>
Group by user ID, count posts, find max, calculate string lengths, create bar chart.
</details>

<details>
<summary>Hint for Exercise 3</summary>
Use try/except, catch `requests.exceptions.RequestException`, check `response.raise_for_status()`.
</details>

<details>
<summary>Hint for Exercise 4</summary>
Use `requests.get()`, `BeautifulSoup`, `find_all()` for different tags, extract text and attributes.
</details>

<details>
<summary>Hint for Exercise 5</summary>
Use `pd.read_html()` or find table with BeautifulSoup and convert, analyze with pandas methods.
</details>

<details>
<summary>Hint for Exercise 6</summary>
Use `train_test_split()`, `LinearRegression()`, `fit()`, `predict()`, `mean_squared_error()`, `r2_score()`.
</details>

<details>
<summary>Hint for Exercise 7</summary>
Create binary target column, use `LogisticRegression()`, evaluate with `accuracy_score()` and `classification_report()`.
</details>

<details>
<summary>Hint for Exercise 8</summary>
Use `isnull().sum()`, `SimpleImputer()`, `StandardScaler()`, fit and transform data.
</details>

<details>
<summary>Hint for Exercise 9</summary>
Select columns, scale with `StandardScaler()`, use `KMeans()`, visualize with scatter plot colored by cluster.
</details>

<details>
<summary>Hint for Exercise 10</summary>
Combine all previous steps: load, preprocess, engineer features, train multiple models, compare with metrics.
</details>

---

**Good luck!** These exercises combine many concepts. Take your time and refer back to previous lessons as needed.

---

**Congratulations on completing the Python for Data Analysis course!** 🎉

You've learned:
- Python fundamentals
- Data structures
- Control flow and functions
- Working with files and data
- Pandas for data manipulation
- Data analysis techniques
- Data visualization
- Advanced topics (APIs, web scraping, ML basics)

Continue practicing and building projects to solidify your skills!
