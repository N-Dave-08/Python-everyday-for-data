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

import requests

try:
    res = requests.get('https://jsonplaceholder.typicode.com/invalid', timeout=5)
    res.raise_for_status()
    data = res.json()
    print("Successfully fetched data")
except requests.exceptions.Timeout:
    print(f"Error: Connection Timeout")
except requests.exceptions.HTTPError as e:
    print(f"Error: Invalid status code: {e.response.status_code}")
except requests.exceptions.ConnectionError:
    print("Error: Connection Error")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

# Test cases
# https://jsonplaceholder.typicode.com/posts'       valid
# https://jsonplaceholder.typicode.com/invalid'     404
# https://this-url-does-not-exist.xyz'              connection error

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

import requests
from bs4 import BeautifulSoup
import csv

# fetch html
url = 'https://quotes.toscrape.com'
res = requests.get(url)
html = res.text

soup = BeautifulSoup(html, 'html.parser')

# headings
headings = soup.find_all(['h1', 'h2', 'h3'])

headings_num = len(headings)

print(f"Found {headings_num} headings")

# links
links = soup.find_all('a')

links_num = len(links)

print(f"Found {links_num} links")

# paragraphs
paragraphs = soup.find_all('p')

paragraphs_num = len(paragraphs)

print(f"Found {paragraphs_num} paragraphs")

# save to csv
with open('level-08-advanced-topics/scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Type', 'Content'])

    for h in headings:
        writer.writerow(['Heading', h.get_text(strip=True)])
    
    for l in links:
        writer.writerow(['Heading', l.get_text(strip=True)])

    for p in paragraphs:
        writer.writerow(['Heading', p.get_text(strip=True)])

print("Data saved to scraped_data.csv")

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

import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO

# Fetch HTML
url = 'https://www.w3schools.com/html/html_tables.asp'
res = requests.get(url)
res.raise_for_status()

html = res.text

# Parse HTML and extract the first table
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table')

# Convert to pandas DataFrame
df = pd.read_html(StringIO(str(table)))[0]

# Simple analysis
rows, cols = df.shape
print(f"Table extracted: {rows} rows, {cols} columns")

# For this table, we’ll treat the Contact and Country fields as non-numeric
# and only count lengths if there were numeric columns.
# As a placeholder average, we could use the length of company names:

df['Company_Length'] = df['Company'].str.len()
avg_length = df['Company_Length'].mean()

print(f"Average company name length: {avg_length:.2f} characters")

# Save to CSV
df.to_csv('level-08-advanced-topics/table_data.csv', index=False)
print("Data saved to table_data.csv")

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

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

employees = pd.read_csv('data/datasets/employees.csv')

# feature
X = employees[['age']]
# target
y = employees['salary']

# split into train and test sets (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# predictions
predictions = model.predict(X_test)

# calculate error metrics
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

results = pd.DataFrame({'Actual': y_test, 'Predicted': predictions})
print("\n Predictions vs Actual:")
print(results)

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

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

employees = pd.read_csv('data/datasets/employees.csv')

employees['high_earner'] = employees['salary'] > 75000

# features
X = employees[['age', 'department_id']]
y = employees['high_earner']

# split into train/test sets (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

# predictions
predictions = model.predict(X_test)

# evaluate
accuracy = accuracy_score(y_test, predictions)
report = classification_report(y_test, predictions)

print(f"Accuracy: {accuracy:.2f}")
print(f"Classification Report:")
print(report)

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

import pandas as pd
from sklearn.preprocessing import StandardScaler

employees = pd.read_csv('level-08-advanced-topics/employees_unclean.csv')

# check for missing values
print("Missing Values: \n")
print(employees.isna().sum())

# fill missing values
employees['salary'].fillna(employees['salary'].median(), inplace=True)
employees['age'].fillna(employees['age'].median(), inplace=True)
employees['phone'].fillna('Unknown', inplace=True)

# after processing
print("After preprocessing: ")
print(employees.isna().sum())

# scale the numerical features
scaler = StandardScaler()
numerical_features = ['age', 'salary']
employees[numerical_features] = scaler.fit_transform(employees[numerical_features])

print("\nNumerical features scaled: ")
print(employees[numerical_features].head())

# prepare date for model
employees['high_earner'] = employees['salary'] > 0

X = employees[['age', 'department_id']]
y = employees['high_earner']

print("\nPrepare data for ML model: ")
print(f"Features (X) shape: {X.shape}")
print(f"Target (y) shape: {y.shape}")

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

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

employees = pd.read_csv('level-08-advanced-topics/employees.csv')

# features
features = employees[['age', 'salary']]

# scale the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# apply k-Means clustering
k = 3
kmeans = KMeans(n_clusters=k, random_state=42)
employees['cluster'] = kmeans.fit_predict(scaled_features)

# visualize clusters
plt.figure(figsize=(8,6))
plt.scatter(employees['age'], employees['salary'], c=employees['cluster'], cmap='viridis', s=100)
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('K-Means Clustering of Employees')
plt.colorbar(label='Cluster')
plt.show()

for cluster_num in range(k):
    cluster_data = employees[employees['cluster'] == cluster_num]
    num_employees = len(cluster_data)
    avg_salary = cluster_data['salary'].mean()
    print(f"Cluster {cluster_num}: {num_employees} employees, average salary: ${avg_salary:,.0f}")

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

# Exercise 10: Complete ML Pipeline with employees.csv and departments.csv

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# ==========================================
# 1. Load data
# ==========================================
employees = pd.read_csv('data/datasets/employees.csv')
departments = pd.read_csv('data/datasets/departments.csv')

# Merge datasets to get department info
data = employees.merge(departments, on='department_id', how='left')
print(f"Data loaded: {data.shape[0]} samples")
print(data.head())

# ==========================================
# 2. Handle missing values and outliers
# ==========================================
# Fill missing numerical values with mean
num_cols = ['salary', 'age', 'budget']
data[num_cols] = data[num_cols].fillna(data[num_cols].mean())

# Clip salary and age to 1st-99th percentile to handle outliers
for col in ['salary', 'age']:
    lower = data[col].quantile(0.01)
    upper = data[col].quantile(0.99)
    data[col] = data[col].clip(lower, upper)

# ==========================================
# 3. Feature engineering
# ==========================================
# Encode categorical features
cat_features = ['job_title', 'department_name', 'location']
num_features = ['age', 'budget']

X = data[cat_features + num_features]
y = data['salary']

# ==========================================
# 4. Split data
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# ==========================================
# 5. Preprocessing and pipelines
# ==========================================
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features),
        ('num', 'passthrough', num_features)
    ]
)

# Linear Regression pipeline
lr_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Random Forest pipeline
rf_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# ==========================================
# 6. Train models
# ==========================================
lr_pipeline.fit(X_train, y_train)
rf_pipeline.fit(X_train, y_train)

# Predictions
y_pred_lr = lr_pipeline.predict(X_test)
y_pred_rf = rf_pipeline.predict(X_test)

# Model performance
mse_lr = mean_squared_error(y_test, y_pred_lr)
r2_lr = r2_score(y_test, y_pred_lr)

mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)

print("Model Comparison:")
print(f"  Linear Regression: MSE = {int(mse_lr)}, R² = {r2_lr:.2f}")
print(f"  Random Forest: MSE = {int(mse_rf)}, R² = {r2_rf:.2f}")

best_model = 'Linear Regression' if r2_lr > r2_rf else 'Random Forest'
print(f"Best model: {best_model}")

# ==========================================
# 7. Visualize results
# ==========================================
plt.figure(figsize=(10,5))
plt.plot(y_test.values, label='Actual', marker='o')
plt.plot(y_pred_lr, label='LR Predictions', marker='x')
plt.plot(y_pred_rf, label='RF Predictions', marker='s')
plt.title('Actual vs Predicted Salaries')
plt.xlabel('Sample')
plt.ylabel('Salary')
plt.legend()
plt.show()
