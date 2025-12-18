# Lesson 8.1: Working with APIs

## What is an API?

**API (Application Programming Interface)** allows programs to communicate with each other. Many services provide APIs to access their data.

## Making HTTP Requests

### Using `requests` Library

```python
import requests

# Install: pip install requests

# GET request
response = requests.get('https://api.example.com/data')
print(response.status_code)  # 200 means success
print(response.json())  # If response is JSON
```

### Handling Responses

```python
response = requests.get('https://api.example.com/data')

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### Query Parameters

```python
# Add parameters to URL
params = {'key': 'value', 'page': 1}
response = requests.get('https://api.example.com/data', params=params)
```

### Headers

```python
# Add headers (e.g., API keys)
headers = {'Authorization': 'Bearer YOUR_API_KEY'}
response = requests.get('https://api.example.com/data', headers=headers)
```

## Working with JSON APIs

### Fetching and Parsing Data

```python
import requests
import pandas as pd

# Fetch data
response = requests.get('https://api.example.com/users')
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data)
print(df.head())
```

### Error Handling

```python
try:
    response = requests.get('https://api.example.com/data', timeout=5)
    response.raise_for_status()  # Raises exception for bad status codes
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

## Example: Public APIs

### JSONPlaceholder (Testing)

```python
import requests
import pandas as pd

# Fetch posts
response = requests.get('https://jsonplaceholder.typicode.com/posts')
posts = response.json()

# Convert to DataFrame
df = pd.DataFrame(posts)
print(df.head())
```

### REST Countries API

```python
import requests

# Get country data
response = requests.get('https://restcountries.com/v3.1/name/usa')
data = response.json()
print(data[0]['name']['common'])
```

## Best Practices

1. **Handle errors**: Always check status codes
2. **Use timeouts**: Prevent hanging requests
3. **Respect rate limits**: Don't make too many requests
4. **Store API keys securely**: Never commit keys to git
5. **Cache responses**: When appropriate, to avoid repeated requests

## Next Steps

In the next lesson, you'll learn about web scraping, another way to gather data from the web.

---

**Key Takeaways:**
- Use `requests` library for HTTP requests
- Check `status_code` before processing responses
- Use `response.json()` to parse JSON data
- Add parameters with `params`, headers with `headers`
- Always handle errors and use timeouts
- Convert API responses to DataFrames for analysis
