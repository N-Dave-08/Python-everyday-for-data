import pandas as pd
import numpy as np

# Test reading data
df = pd.read_csv('data/datasets/employees.csv')
print(f"✓ Employees dataset: {len(df)} rows")
print(f"✓ Setup successful!")