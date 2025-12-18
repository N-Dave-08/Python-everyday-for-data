"""
Setup script to create sample datasets for the Python for Data Analysis Course.
Run this script to generate all CSV files needed for the exercises.
"""

import pandas as pd
import os
from datetime import datetime, timedelta

# Create datasets directory if it doesn't exist
os.makedirs('datasets', exist_ok=True)

print("Creating sample datasets...")
print("=" * 50)

# ============================================
# 1. Employees Dataset
# ============================================
print("Creating employees dataset...")

employees_data = {
    'employee_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    'first_name': ['John', 'Sarah', 'Michael', 'Emily', 'David', 'Jessica', 'Robert', 'Amanda', 'James', 'Lisa', 'William', 'Jennifer', 'Richard', 'Michelle', 'Joseph'],
    'last_name': ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White'],
    'email': ['john.smith@company.com', 'sarah.johnson@company.com', 'michael.williams@company.com', 'emily.brown@company.com', 'david.jones@company.com', 'jessica.garcia@company.com', 'robert.miller@company.com', 'amanda.davis@company.com', 'james.wilson@company.com', 'lisa.moore@company.com', 'william.taylor@company.com', 'jennifer.anderson@company.com', 'richard.thomas@company.com', 'michelle.jackson@company.com', 'joseph.white@company.com'],
    'phone': ['555-0101', '555-0102', '555-0103', '555-0104', '555-0105', '555-0106', '555-0107', '555-0108', '555-0109', '555-0110', '555-0111', '555-0112', '555-0113', '555-0114', '555-0115'],
    'hire_date': ['2020-01-15', '2019-03-20', '2021-06-10', '2020-11-05', '2018-09-12', '2022-02-28', '2019-07-18', '2021-04-22', '2020-08-30', '2019-12-14', '2021-10-05', '2020-05-19', '2018-11-25', '2022-01-08', '2021-03-15'],
    'job_title': ['Software Engineer', 'Data Analyst', 'Marketing Manager', 'Software Engineer', 'Sales Manager', 'Junior Developer', 'HR Specialist', 'Data Analyst', 'Senior Engineer', 'Marketing Specialist', 'Software Engineer', 'Sales Manager', 'Senior Engineer', 'Data Analyst', 'Marketing Manager'],
    'salary': [85000.00, 72000.00, 78000.00, 82000.00, 75000.00, 55000.00, 65000.00, 70000.00, 95000.00, 68000.00, 88000.00, 73000.00, 92000.00, 71000.00, 76000.00],
    'department_id': [1, 2, 3, 1, 4, 1, 5, 2, 1, 3, 1, 4, 1, 2, 3]
}

employees_df = pd.DataFrame(employees_data)
employees_df.to_csv('datasets/employees.csv', index=False)
print(f"✓ Created employees.csv with {len(employees_df)} rows")

# ============================================
# 2. Products Dataset
# ============================================
print("Creating products dataset...")

products_data = {
    'product_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'product_name': ['Laptop Pro', 'Wireless Mouse', 'Mechanical Keyboard', 'Monitor 27"', 'USB-C Cable', 'Webcam HD', 'Headphones Wireless', 'Tablet Stand', 'Laptop Stand', 'Desk Mat', 'Monitor Stand', 'Cable Organizer'],
    'category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories', 'Electronics', 'Electronics', 'Accessories', 'Accessories', 'Accessories', 'Accessories', 'Accessories'],
    'price': [1299.99, 29.99, 89.99, 349.99, 19.99, 79.99, 149.99, 39.99, 59.99, 24.99, 49.99, 14.99],
    'stock_quantity': [25, 150, 80, 40, 200, 60, 90, 120, 100, 180, 70, 250],
    'supplier_id': [1, 2, 2, 1, 3, 1, 1, 3, 3, 2, 3, 2],
    'created_date': ['2020-01-10', '2019-05-15', '2020-03-20', '2021-01-05', '2019-08-12', '2020-11-18', '2021-02-14', '2020-07-22', '2021-04-30', '2019-12-08', '2020-09-25', '2021-06-12']
}

products_df = pd.DataFrame(products_data)
products_df.to_csv('datasets/products.csv', index=False)
print(f"✓ Created products.csv with {len(products_df)} rows")

# ============================================
# 3. Customers Dataset
# ============================================
print("Creating customers dataset...")

customers_data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'first_name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Edward', 'Fiona', 'George', 'Hannah', 'Ian', 'Julia'],
    'last_name': ['Adams', 'Baker', 'Clark', 'Davis', 'Evans', 'Foster', 'Green', 'Harris', 'Irwin', 'Jones'],
    'email': ['alice.adams@email.com', 'bob.baker@email.com', 'charlie.clark@email.com', 'diana.davis@email.com', 'edward.evans@email.com', 'fiona.foster@email.com', 'george.green@email.com', 'hannah.harris@email.com', 'ian.irwin@email.com', 'julia.jones@email.com'],
    'phone': ['555-1001', '555-1002', '555-1003', '555-1004', '555-1005', '555-1006', '555-1007', '555-1008', '555-1009', '555-1010'],
    'address': ['123 Main St', '456 Oak Ave', '789 Pine Rd', '321 Elm St', '654 Maple Dr', '987 Cedar Ln', '147 Birch Way', '258 Spruce Ct', '369 Willow Pl', '741 Ash Blvd'],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'],
    'state': ['NY', 'CA', 'IL', 'TX', 'AZ', 'PA', 'TX', 'CA', 'TX', 'CA'],
    'zip_code': ['10001', '90001', '60601', '77001', '85001', '19101', '78201', '92101', '75201', '95101'],
    'registration_date': ['2020-01-05', '2019-06-12', '2021-03-18', '2020-08-25', '2019-11-30', '2022-02-14', '2021-07-22', '2020-04-10', '2019-09-05', '2021-12-20']
}

customers_df = pd.DataFrame(customers_data)
customers_df.to_csv('datasets/customers.csv', index=False)
print(f"✓ Created customers.csv with {len(customers_df)} rows")

# ============================================
# 4. Departments Dataset
# ============================================
print("Creating departments dataset...")

departments_data = {
    'department_id': [1, 2, 3, 4, 5],
    'department_name': ['Engineering', 'Data Science', 'Marketing', 'Sales', 'Human Resources'],
    'location': ['Building A, Floor 3', 'Building B, Floor 2', 'Building A, Floor 1', 'Building C, Floor 1', 'Building A, Floor 2'],
    'budget': [500000.00, 300000.00, 250000.00, 400000.00, 200000.00],
    'manager_id': [1, 2, 3, 5, 7]
}

departments_df = pd.DataFrame(departments_data)
departments_df.to_csv('datasets/departments.csv', index=False)
print(f"✓ Created departments.csv with {len(departments_df)} rows")

# ============================================
# 5. Suppliers Dataset
# ============================================
print("Creating suppliers dataset...")

suppliers_data = {
    'supplier_id': [1, 2, 3],
    'supplier_name': ['TechSupply Co', 'Accessory World', 'ElectroParts Inc'],
    'contact_name': ['John Tech', 'Mary Access', 'Tom Electro'],
    'email': ['contact@techsupply.com', 'info@accessoryworld.com', 'sales@electroparts.com'],
    'phone': ['555-2001', '555-2002', '555-2003'],
    'address': ['100 Tech Street', '200 Accessory Ave', '300 Electro Blvd']
}

suppliers_df = pd.DataFrame(suppliers_data)
suppliers_df.to_csv('datasets/suppliers.csv', index=False)
print(f"✓ Created suppliers.csv with {len(suppliers_df)} rows")

# ============================================
# 6. Orders Dataset
# ============================================
print("Creating orders dataset...")

orders_data = {
    'order_id': list(range(1, 21)),
    'customer_id': [1, 2, 1, 3, 4, 2, 5, 1, 6, 3, 7, 4, 8, 2, 9, 5, 10, 1, 3, 6],
    'order_date': ['2023-01-15', '2023-01-18', '2023-02-05', '2023-02-12', '2023-02-20', '2023-03-01', '2023-03-10', '2023-03-15', '2023-03-22', '2023-04-05', '2023-04-12', '2023-04-18', '2023-05-01', '2023-05-10', '2023-05-15', '2023-05-22', '2023-06-01', '2023-06-10', '2023-06-15', '2023-06-20'],
    'total_amount': [1299.99, 29.99, 89.99, 349.99, 19.99, 79.99, 149.99, 39.99, 59.99, 24.99, 49.99, 14.99, 1299.99, 29.99, 89.99, 349.99, 19.99, 79.99, 149.99, 39.99],
    'status': ['Completed', 'Completed', 'Completed', 'Completed', 'Completed', 'Completed', 'Completed', 'Completed', 'Completed', 'Completed', 'Completed', 'Completed', 'Completed', 'Completed', 'Completed', 'Completed', 'Completed', 'Completed', 'Completed', 'Completed'],
    'shipping_address': ['123 Main St, New York, NY 10001', '456 Oak Ave, Los Angeles, CA 90001', '123 Main St, New York, NY 10001', '789 Pine Rd, Chicago, IL 60601', '321 Elm St, Houston, TX 77001', '456 Oak Ave, Los Angeles, CA 90001', '654 Maple Dr, Phoenix, AZ 85001', '123 Main St, New York, NY 10001', '987 Cedar Ln, Philadelphia, PA 19101', '789 Pine Rd, Chicago, IL 60601', '147 Birch Way, San Antonio, TX 78201', '321 Elm St, Houston, TX 77001', '258 Spruce Ct, San Diego, CA 92101', '456 Oak Ave, Los Angeles, CA 90001', '369 Willow Pl, Dallas, TX 75201', '654 Maple Dr, Phoenix, AZ 85001', '741 Ash Blvd, San Jose, CA 95101', '123 Main St, New York, NY 10001', '789 Pine Rd, Chicago, IL 60601', '987 Cedar Ln, Philadelphia, PA 19101']
}

orders_df = pd.DataFrame(orders_data)
orders_df.to_csv('datasets/orders.csv', index=False)
print(f"✓ Created orders.csv with {len(orders_df)} rows")

# ============================================
# 7. Order Items Dataset
# ============================================
print("Creating order_items dataset...")

order_items_data = {
    'order_item_id': list(range(1, 46)),
    'order_id': [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2],
    'product_id': [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 2, 3, 4, 5, 6, 7, 8, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'quantity': [1, 2, 1, 1, 1, 3, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'unit_price': [1299.99, 29.99, 29.99, 89.99, 349.99, 19.99, 19.99, 79.99, 149.99, 39.99, 59.99, 24.99, 49.99, 14.99, 1299.99, 29.99, 29.99, 89.99, 349.99, 19.99, 79.99, 149.99, 39.99, 89.99, 89.99, 349.99, 19.99, 79.99, 149.99, 39.99, 59.99, 24.99, 49.99, 14.99, 1299.99, 29.99, 89.99, 349.99, 19.99, 79.99, 149.99, 39.99, 59.99, 24.99, 49.99],
    'subtotal': [1299.99, 59.98, 29.99, 89.99, 349.99, 59.97, 39.98, 79.99, 149.99, 39.99, 59.99, 49.98, 49.99, 14.99, 1299.99, 29.99, 29.99, 89.99, 349.99, 19.99, 79.99, 149.99, 39.99, 89.99, 89.99, 349.99, 19.99, 79.99, 149.99, 39.99, 59.99, 24.99, 49.99, 14.99, 1299.99, 29.99, 89.99, 349.99, 19.99, 79.99, 149.99, 39.99, 59.99, 24.99, 49.99]
}

order_items_df = pd.DataFrame(order_items_data)
order_items_df.to_csv('datasets/order_items.csv', index=False)
print(f"✓ Created order_items.csv with {len(order_items_df)} rows")

# ============================================
# 8. Sales Dataset
# ============================================
print("Creating sales dataset...")

sales_data = {
    'sale_id': list(range(1, 31)),
    'employee_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    'product_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6],
    'sale_date': ['2023-01-10', '2023-01-12', '2023-01-15', '2023-01-18', '2023-01-20', '2023-01-22', '2023-01-25', '2023-01-28', '2023-02-01', '2023-02-03', '2023-02-05', '2023-02-08', '2023-02-10', '2023-02-12', '2023-02-15', '2023-02-18', '2023-02-20', '2023-02-22', '2023-02-25', '2023-02-28', '2023-03-01', '2023-03-03', '2023-03-05', '2023-03-08', '2023-03-10', '2023-03-12', '2023-03-15', '2023-03-18', '2023-03-20', '2023-03-22'],
    'quantity': [1, 2, 1, 1, 3, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1],
    'unit_price': [1299.99, 29.99, 89.99, 349.99, 19.99, 79.99, 149.99, 39.99, 59.99, 24.99, 49.99, 14.99, 1299.99, 29.99, 89.99, 349.99, 19.99, 79.99, 149.99, 39.99, 59.99, 24.99, 49.99, 14.99, 1299.99, 29.99, 89.99, 349.99, 19.99, 79.99],
    'total_amount': [1299.99, 59.98, 89.99, 349.99, 59.97, 79.99, 149.99, 79.98, 59.99, 49.98, 49.99, 14.99, 1299.99, 29.99, 89.99, 349.99, 39.98, 79.99, 149.99, 39.99, 59.99, 49.98, 49.99, 14.99, 1299.99, 29.99, 89.99, 349.99, 39.98, 79.99],
    'region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South']
}

sales_df = pd.DataFrame(sales_data)
sales_df.to_csv('datasets/sales.csv', index=False)
print(f"✓ Created sales.csv with {len(sales_df)} rows")

# ============================================
# Setup Complete
# ============================================
print("=" * 50)
print("Setup complete! All datasets have been created.")
print(f"Total datasets: 8")
print(f"Location: datasets/")
print("\nYou can now start working through the course exercises!")
