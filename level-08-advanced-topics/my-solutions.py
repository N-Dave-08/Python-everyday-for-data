# Exercise 1: Basic API Request
# Difficulty: Beginner

#   1. Use the JSONPlaceholder API (https://jsonplaceholder.typicode.com/posts)
#   2. Fetch the first 10 posts
#   3. Convert the data to a pandas DataFrame
#   4. Display the title and body of each post

# Expected Output Format:

# Post 1: sunt aut facere...
# Body: quia et suscipit...
# ---
# Post 2: qui est esse...
# ...

import requests
import pandas as pd

res = requests.get('https://jsonplaceholder.typicode.com/posts')

if res.status_code == 200:
    data = res.json()
else:
    print(f"Error: {res.status_code}")

df = pd.DataFrame(data)

for _, row in df.iterrows():
    print(f"Post {row['id']}: {row['title']}\nBody: {row['body']}\n")

# =================================================================================

# Exercise 2: API Data Analysis
# Difficulty: Intermediate

#   1. Fetch all posts from JSONPlaceholder API
#   2. Count posts by user ID
#   3. Find the user with the most posts
#   4. Calculate average post title length
#   5. Create a visualization showing posts per user

# Expected Output Format:

# Total posts: 100
# User with most posts: User 1 (10 posts)
# Average title length: 44.5 characters

import requests

res = requests.get('https://jsonplaceholder.typicode.com/posts')
res.raise_for_status() # stop if request fails

data = res.json()

# Count posts per userId
post_count = {}

for post in data:
    user_id = post['userId']
    if user_id in post_count:
        post_count[user_id] += 1
    else:
        post_count[user_id] = 1

for user_id, count in sorted(post_count.items()):
    print(f"{user_id}: {count} posts")
# Total number of posts
print(f"Total posts: {len(data)}")

# Find the user with the most posts
max_posts = max(post_count.values())
top_users = [
    user for user, count in post_count.items() if count == max_posts
]
users_str = ", ".join(str(user) for user in top_users)
print(f"User with the most posts: users {users_str} ({max_posts} posts)")

title_lengths = [len(post['title']) for post in data]
avg_length = sum(title_lengths) / len(title_lengths)
print(f"Average title length: {avg_length} characters")

# =================================================================================

# Exercise 3: Error Handling for APIs
# Difficulty: Intermediate

#   1. Create a function that fetches data from an API
#   2. Handle connection errors
#   3. Handle timeout errors
#   4. Handle invalid status codes
#   5. Test with both valid and invalid URLs

# Expected Output Format:

# Successfully fetched data
# Error: Connection timeout
# Error: Invalid status code: 404

# =================================================================================

# Exercise 4: Web Scraping Basics
# Difficulty: Intermediate

#   1. Scrape a simple webpage (use a test site or create your own)
#   2. Extract all headings (h1, h2, h3)
#   3. Extract all links
#   4. Extract all paragraph text
#   5. Save the extracted data to a CSV file

# Note: Be respectful - only scrape sites that allow it or use test pages.

# Expected Output Format:

# Found 3 headings
# Found 10 links
# Found 5 paragraphs
# Data saved to scraped_data.csv

# =================================================================================

# Exercise 5: Scraping Tables
# Difficulty: Intermediate

#   1. Find a webpage with a table (or use a test page)
#   2. Extract the table data
#   3. Convert to pandas DataFrame
#   4. Perform basic analysis (mean, sum, etc.)
#   5. Save to CSV

# Expected Output Format:

# Table extracted: 10 rows, 5 columns
# Average value: 42.5
# Data saved to table_data.csv

# =================================================================================

# Exercise 6: Simple Linear Regression
# Difficulty: Intermediate

# Using your employees dataset:

#   1. Prepare data: Use 'age' as feature, 'salary' as target
#   2. Split data into train/test sets (80/20)
#   3. Train a linear regression model
#   4. Make predictions on test set
#   5. Calculate and display error metrics (MSE, R²)

# Expected Output Format:

# Training samples: 12
# Test samples: 3
# Mean Squared Error: 1234567.89
# R² Score: 0.75

# =================================================================================

# Exercise 7: Classification
# Difficulty: Advanced

# Create a simple classification problem:

#   1. Use employees data
#   2. Create a binary target: 'high_earner' (salary > 75000)
#   3. Use 'age' and 'department_id' as features
#   4. Train a logistic regression model
#   5. Evaluate with accuracy score and classification report

# Expected Output Format:

# Accuracy: 0.87
# Classification Report:
#               precision    recall  f1-score   support
#        False       0.85      0.92      0.88         6
#         True       0.90      0.82      0.86         6

# =================================================================================

# Exercise 8: Data Preprocessing
# Difficulty: Intermediate

#   1. Load a dataset with missing values
#   2. Check for missing values
#   3. Fill missing values (use appropriate strategy)
#   4. Scale the numerical features
#   5. Prepare data for ML model

# Expected Output Format:

# Missing values:
#   age: 2
#   salary: 1
# After preprocessing:
#   Missing values: 0
#   Features scaled: Yes

# =================================================================================

# Exercise 9: Clustering
# Difficulty: Advanced

# Using employees data:

#   1. Select numerical features (age, salary)
#   2. Scale the features
#   3. Apply K-Means clustering (k=3)
#   4. Visualize clusters with scatter plot
#   5. Analyze cluster characteristics

# Expected Output Format:

# Cluster 0: 5 employees, avg salary: $65000
# Cluster 1: 6 employees, avg salary: $80000
# Cluster 2: 4 employees, avg salary: $90000

# =================================================================================

# Exercise 10: Complete ML Pipeline
# Difficulty: Advanced

# Create a complete machine learning pipeline:

#   1. Load and explore data
#   2. Handle missing values and outliers
#   3. Feature engineering (create new features if needed)
#   4. Split data
#   5. Train multiple models (Linear Regression, Random Forest)
#   6. Compare model performance
#   7. Make predictions and visualize results

# Expected Output Format:

# Data loaded: 15 samples
# Features prepared: 3 features
# Model Comparison:
#   Linear Regression: MSE = 1234567, R² = 0.75
#   Random Forest: MSE = 987654, R² = 0.82
# Best model: Random Forest
