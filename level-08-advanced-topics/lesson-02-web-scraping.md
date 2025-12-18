# Lesson 8.2: Web Scraping Basics

## What is Web Scraping?

**Web scraping** is extracting data from websites. It's useful when APIs aren't available.

### Installing BeautifulSoup

```bash
pip install beautifulsoup4 requests
```

## Basic Web Scraping

### Fetching HTML

```python
import requests
from bs4 import BeautifulSoup

# Fetch webpage
url = 'https://example.com'
response = requests.get(url)
html = response.text

# Parse HTML
soup = BeautifulSoup(html, 'html.parser')
```

### Finding Elements

```python
# Find first element
title = soup.find('h1')
print(title.text)

# Find all elements
paragraphs = soup.find_all('p')
for p in paragraphs:
    print(p.text)

# Find by class
items = soup.find_all('div', class_='item')

# Find by ID
header = soup.find(id='header')
```

### Extracting Data

```python
# Get text
text = soup.find('p').text

# Get attributes
link = soup.find('a')
url = link['href']

# Get all links
links = soup.find_all('a')
for link in links:
    print(link['href'], link.text)
```

## Scraping Tables

### Extracting Table Data

```python
import pandas as pd

# Find table
table = soup.find('table')

# Convert to DataFrame
df = pd.read_html(str(table))[0]
print(df)
```

## Best Practices

1. **Respect robots.txt**: Check website's scraping policy
2. **Add delays**: Don't overload servers
3. **Handle errors**: Websites change structure
4. **Use headers**: Some sites block default user agents
5. **Be ethical**: Don't scrape personal data without permission

## Example: Scraping a Simple Page

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://example.com/data'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data
data = []
for item in soup.find_all('div', class_='data-item'):
    name = item.find('h3').text
    value = item.find('span').text
    data.append({'name': name, 'value': value})

# Convert to DataFrame
df = pd.DataFrame(data)
print(df)
```

## Next Steps

In the final lesson, you'll get an introduction to machine learning basics.

---

**Key Takeaways:**
- Use `requests` to fetch web pages
- Use `BeautifulSoup` to parse HTML
- Use `find()` and `find_all()` to locate elements
- Extract text and attributes from elements
- Convert tables to DataFrames with `pd.read_html()`
- Always be respectful and ethical when scraping
