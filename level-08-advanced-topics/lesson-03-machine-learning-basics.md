# Lesson 8.3: Introduction to Machine Learning

## What is Machine Learning?

**Machine Learning (ML)** is a subset of AI that enables computers to learn from data without being explicitly programmed.

## Types of Machine Learning

### Supervised Learning

Learning from labeled data (input-output pairs):
- **Classification**: Predicting categories (e.g., spam/not spam)
- **Regression**: Predicting continuous values (e.g., price, temperature)

### Unsupervised Learning

Finding patterns in unlabeled data:
- **Clustering**: Grouping similar data points
- **Dimensionality Reduction**: Reducing number of features

## Scikit-learn

**Scikit-learn** is Python's main ML library.

### Installing

```bash
pip install scikit-learn
```

### Basic Workflow

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd

# Load data
df = pd.read_csv('data.csv')

# Prepare features and target
X = df[['feature1', 'feature2']]  # Features
y = df['target']  # What we want to predict

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate
error = mean_squared_error(y_test, predictions)
print(f"Error: {error}")
```

## Common Algorithms

### Linear Regression

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

### Classification

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

### Clustering

```python
from sklearn.cluster import KMeans

model = KMeans(n_clusters=3)
model.fit(X)
labels = model.predict(X)
```

## Data Preprocessing

### Scaling

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### Handling Missing Values

```python
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)
```

## Model Evaluation

### For Regression

```python
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
```

### For Classification

```python
from sklearn.metrics import accuracy_score, classification_report

accuracy = accuracy_score(y_test, predictions)
print(classification_report(y_test, predictions))
```

## Best Practices

1. **Split data**: Always use train/test split
2. **Preprocess data**: Scale, handle missing values
3. **Start simple**: Try linear models first
4. **Evaluate properly**: Use appropriate metrics
5. **Avoid overfitting**: Don't memorize training data

## Next Steps

This is just an introduction! Continue learning:
- More algorithms (Random Forest, SVM, Neural Networks)
- Feature engineering
- Model selection and tuning
- Deep learning with TensorFlow/PyTorch

---

**Key Takeaways:**
- Machine learning learns patterns from data
- Use scikit-learn for ML in Python
- Always split data into train/test sets
- Preprocess data (scale, handle missing values)
- Evaluate models with appropriate metrics
- Start with simple models before trying complex ones
