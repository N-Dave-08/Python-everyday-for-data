# Data Setup Instructions

This folder contains the data setup scripts and sample datasets for the Python for Data Analysis Course.

## Quick Start

### Prerequisites

1. **Install Python 3.8+**
   - Download from: https://www.python.org/downloads/
   - Make sure to check "Add Python to PATH" during installation

2. **Install Required Packages**
   ```bash
   pip install pandas numpy
   ```
   Or if using Python 3 specifically:
   ```bash
   pip3 install pandas numpy
   ```

### Setup Steps

1. **Run the setup script**:
   ```bash
   # Navigate to the data folder
   cd data
   
   # Run setup script
   python setup.py
   ```
   
   Or:
   ```bash
   python3 setup.py
   ```

2. **Verify the setup**:
   ```bash
   # Check that CSV files were created
   ls datasets/
   # Or on Windows:
   dir datasets
   ```
   
   You should see:
   - `employees.csv`
   - `products.csv`
   - `customers.csv`
   - `orders.csv`
   - `order_items.csv`
   - `departments.csv`
   - `sales.csv`
   - `suppliers.csv`

3. **Test reading the data**:
   ```python
   import pandas as pd
   df = pd.read_csv('data/datasets/employees.csv')
   print(f"Employees: {len(df)} rows")
   # Should output: Employees: 15 rows
   ```

## Dataset Overview

The course uses the following datasets, which progressively increase in complexity:

### Level 1-2: Basic Data
- `employees.csv` - Employee information (15 rows)
- `products.csv` - Product catalog (12 rows)

### Level 3-4: Relational Data
- `customers.csv` - Customer information (10 rows)
- `orders.csv` - Order records (20 rows)
- `order_items.csv` - Order line items (45 rows)
- `products.csv` - Product details (used in joins)

### Level 5-6: Complex Scenarios
- `departments.csv` - Department information (5 rows)
- `sales.csv` - Sales transactions with dates (30 rows)
- `employees.csv` with department relationships

### Level 7-8: Advanced Features
- All datasets for visualization
- Time series data in sales
- Complex relationships for analysis

## Dataset Schema

### employees.csv
- `employee_id` (int): Unique employee identifier
- `first_name` (str): Employee's first name
- `last_name` (str): Employee's last name
- `email` (str): Email address
- `phone` (str): Phone number
- `hire_date` (str): Date hired (YYYY-MM-DD)
- `job_title` (str): Job title
- `salary` (float): Annual salary
- `department_id` (int): Department ID (can be null)

### products.csv
- `product_id` (int): Unique product identifier
- `product_name` (str): Product name
- `category` (str): Product category
- `price` (float): Product price
- `stock_quantity` (int): Stock quantity
- `supplier_id` (int): Supplier ID
- `created_date` (str): Date created (YYYY-MM-DD)

### customers.csv
- `customer_id` (int): Unique customer identifier
- `first_name` (str): Customer's first name
- `last_name` (str): Customer's last name
- `email` (str): Email address
- `phone` (str): Phone number
- `address` (str): Street address
- `city` (str): City
- `state` (str): State
- `zip_code` (str): ZIP code
- `registration_date` (str): Registration date (YYYY-MM-DD)

### orders.csv
- `order_id` (int): Unique order identifier
- `customer_id` (int): Customer ID (foreign key)
- `order_date` (str): Order date (YYYY-MM-DD)
- `total_amount` (float): Total order amount
- `status` (str): Order status
- `shipping_address` (str): Shipping address

### order_items.csv
- `order_item_id` (int): Unique order item identifier
- `order_id` (int): Order ID (foreign key)
- `product_id` (int): Product ID (foreign key)
- `quantity` (int): Quantity ordered
- `unit_price` (float): Unit price
- `subtotal` (float): Line item total

### departments.csv
- `department_id` (int): Unique department identifier
- `department_name` (str): Department name
- `location` (str): Department location
- `budget` (float): Department budget
- `manager_id` (int): Manager employee ID

### sales.csv
- `sale_id` (int): Unique sale identifier
- `employee_id` (int): Employee ID (foreign key)
- `product_id` (int): Product ID (foreign key)
- `sale_date` (str): Sale date (YYYY-MM-DD)
- `quantity` (int): Quantity sold
- `unit_price` (float): Unit price
- `total_amount` (float): Total sale amount
- `region` (str): Sales region

### suppliers.csv
- `supplier_id` (int): Unique supplier identifier
- `supplier_name` (str): Supplier name
- `contact_name` (str): Contact person name
- `email` (str): Email address
- `phone` (str): Phone number
- `address` (str): Address

## Resetting the Data

If you need to reset the datasets to their original state:

```bash
# Delete existing datasets
rm -rf datasets/*

# Or on Windows:
del datasets\*

# Run setup again
python setup.py
```

## Notes

- All datasets are in CSV format for easy reading with pandas
- Dates are stored as strings in YYYY-MM-DD format
- The data is realistic but fictional
- The schema progressively increases in complexity to match course levels
- All relationships between tables are maintained (foreign keys)

## Troubleshooting

### "ModuleNotFoundError: No module named 'pandas'"
- Install pandas: `pip install pandas`

### "FileNotFoundError: [Errno 2] No such file or directory"
- Make sure you're running the script from the `data/` directory
- Or use absolute paths in your code

### "Permission denied" when creating files
- Check that you have write permissions in the `datasets/` folder
- On Windows, you might need to run as administrator

### CSV files not created
- Check that the `datasets/` folder exists
- Verify Python can write to the directory
- Check for error messages in the terminal
