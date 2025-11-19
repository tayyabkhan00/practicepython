import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 

np.random.seed(42) # For reproducible results
dates = pd.date_range(start='2022-01-01', end='2023-12-31', freq='D')
product_categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Beauty']
products = {
    'Electronics': ['Wireless Earbuds', 'Smartphone', 'Laptop'],
    'Clothing': ['T-Shirt', 'Jeans', 'Jacket'],
    'Home & Kitchen': ['Coffee Maker', 'Blender', 'Air Fryer'],
    'Books': ['Python Crash Course', 'Deep Learning', 'The Alchemist'],
    'Beauty': ['Face Cream', 'Shampoo', 'Perfume']
}

data = []
for date in dates:
    category = np.random.choice(product_categories)
    product = np.random.choice(products[category])
    quantity = np.random.randint(1, 5)
    unit_price = np.random.uniform(10, 500)
    # Simulate some seasonal trends (e.g., higher sales in December)
    if date.month == 12:
        quantity = int(quantity * np.random.uniform(1.5, 3))
    total_sales = quantity * unit_price
    
    data.append({
        'OrderDate': date,
        'ProductCategory': category,
        'ProductName': product,
        'Quantity': quantity,
        'UnitPrice': unit_price,
        'TotalSales': total_sales
    })

df = pd.DataFrame(data) 

