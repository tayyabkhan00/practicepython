import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set a style for better-looking plots
plt.style.use('seaborn-v0_8') # or 'ggplot', 'seaborn'

# Generate sample sales data
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
print("Sample of Raw Data:")
print(df.head())

# 1. Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 2. Check data types
print("\nData Types:")
print(df.dtypes)

# 3. Handle potential issues (example: convert date, though ours is already fine)
# df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# 4. Remove duplicates (if any)
initial_count = len(df)
df = df.drop_duplicates()
print(f"\nRemoved {initial_count - len(df)} duplicate rows.")

# 5. Check for negative sales/quantities (invalid data)
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

print(f"\nFinal dataset shape: {df.shape}")

# Add a 'YearMonth' column for trend analysis
df['YearMonth'] = df['OrderDate'].dt.to_period('M')
df['Year'] = df['OrderDate'].dt.year
df['Month'] = df['OrderDate'].dt.month

# 1. Overall Sales Summary
total_sales = df['TotalSales'].sum()
total_orders = len(df)
avg_order_value = total_sales / total_orders

print("\n--- Overall Sales Summary ---")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Average Order Value: ${avg_order_value:.2f}")

# 2. Top-Performing Products (by Total Sales)
print("\n--- Top 10 Products by Revenue ---")
top_products_sales = df.groupby('ProductName').agg({
    'TotalSales': 'sum',
    'Quantity': 'sum',
    'OrderDate': 'count' # Count of orders
}).rename(columns={'OrderDate': 'OrderCount'})
top_products_sales = top_products_sales.sort_values('TotalSales', ascending=False)
print(top_products_sales.head(10))

# 3. Top-Performing Products (by Quantity Sold)
print("\n--- Top 10 Products by Quantity Sold ---")
top_products_quantity = df.groupby('ProductName')['Quantity'].sum().sort_values(ascending=False)
print(top_products_quantity.head(10))

# 4. Top-Performing Categories
print("\n--- Sales by Category ---")
sales_by_category = df.groupby('ProductCategory')['TotalSales'].sum().sort_values(ascending=False)
print(sales_by_category)

# 5. Monthly Sales Trends
print("\n--- Monthly Sales Trends ---")
monthly_sales = df.groupby('YearMonth')['TotalSales'].sum()
print(monthly_sales.tail(12)) # Last 12 months

# Create a figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Sales Data Analysis Dashboard', fontsize=16, fontweight='bold')

# 1. Top 10 Products by Sales (Bar Plot)
top_10_products = top_products_sales.head(10)
axes[0, 0].barh(top_10_products.index, top_10_products['TotalSales'] / 1000, color='skyblue')
axes[0, 0].set_title('Top 10 Products by Revenue')
axes[0, 0].set_xlabel('Total Sales (Thousands $)')
axes[0, 0].invert_yaxis() # Highest value at the top

# 2. Sales by Category (Pie Chart)
axes[0, 1].pie(sales_by_category.values, labels=sales_by_category.index, autopct='%1.1f%%', startangle=90)
axes[0, 1].set_title('Sales Distribution by Category')

# 3. Monthly Sales Trend (Line Plot)
# Convert YearMonth period to string for plotting
monthly_sales.index = monthly_sales.index.astype(str)
axes[1, 0].plot(monthly_sales.index, monthly_sales.values / 1000, marker='o', linewidth=2)
axes[1, 0].set_title('Monthly Sales Trend')
axes[1, 0].set_xlabel('Month')
axes[1, 0].set_ylabel('Sales (Thousands $)')
axes[1, 0].tick_params(axis='x', rotation=45)

# 4. Sales by Month (to see seasonality - Box Plot)
df['MonthName'] = df['OrderDate'].dt.month_name()
monthly_order = ['January', 'February', 'March', 'April', 'May', 'June',
                 'July', 'August', 'September', 'October', 'November', 'December']
sns.boxplot(data=df, x='MonthName', y='TotalSales', ax=axes[1, 1], order=monthly_order)
axes[1, 1].set_title('Sales Distribution by Month (Seasonality)')
axes[1, 1].set_xlabel('Month')
axes[1, 1].set_ylabel('Sales per Order ($)')
axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

# 5. (Bonus) Year-over-Year Sales Growth
yearly_sales = df.groupby('Year')['TotalSales'].sum()
growth_rate = ((yearly_sales.iloc[-1] - yearly_sales.iloc[-2]) / yearly_sales.iloc[-2]) * 100

print(f"\n--- Year-over-Year Growth ---")
print(f"Sales Growth from {yearly_sales.index[-2]} to {yearly_sales.index[-1]}: {growth_rate:.1f}%")

# Create a Pandas ExcelWriter object
with pd.ExcelWriter('sales_analysis_report.xlsx') as writer:
    
    # Export raw data (or cleaned data) to a sheet
    df.to_excel(writer, sheet_name='Cleaned_Sales_Data', index=False)
    
    # Export top products summary
    top_products_sales.head(10).to_excel(writer, sheet_name='Top_Products')
    
    # Export monthly sales trend
    monthly_sales.to_excel(writer, sheet_name='Monthly_Trend', header=['TotalSales'])
    
    # Export category performance
    sales_by_category.to_excel(writer, sheet_name='Category_Performance', header=['TotalSales'])


