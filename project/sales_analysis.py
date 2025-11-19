import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Set up advanced styling
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Generate enhanced sample sales data
np.random.seed(42)
dates = pd.date_range(start='2022-01-01', end='2023-12-31', freq='D')
product_categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Beauty', 'Sports', 'Toys']
products = {
    'Electronics': ['Wireless Earbuds', 'Smartphone', 'Laptop', 'Tablet', 'Smartwatch'],
    'Clothing': ['T-Shirt', 'Jeans', 'Jacket', 'Dress', 'Sneakers'],
    'Home & Kitchen': ['Coffee Maker', 'Blender', 'Air Fryer', 'Vacuum Cleaner', 'Mixer'],
    'Books': ['Python Crash Course', 'Deep Learning', 'The Alchemist', 'Data Science', 'AI Fundamentals'],
    'Beauty': ['Face Cream', 'Shampoo', 'Perfume', 'Makeup Kit', 'Serum'],
    'Sports': ['Yoga Mat', 'Dumbbells', 'Running Shoes', 'Basketball', 'Tennis Racket'],
    'Toys': ['Lego Set', 'Action Figure', 'Board Game', 'Puzzle', 'Drone']
}

# Enhanced data generation with more realistic patterns
data = []
for date in dates:
    category = np.random.choice(product_categories, p=[0.25, 0.15, 0.15, 0.1, 0.15, 0.1, 0.1])
    product = np.random.choice(products[category])
    
    # More realistic pricing and quantity patterns
    base_prices = {
        'Electronics': (100, 2000), 'Clothing': (15, 150), 'Home & Kitchen': (30, 300),
        'Books': (10, 50), 'Beauty': (20, 200), 'Sports': (25, 250), 'Toys': (20, 300)
    }
    
    min_price, max_price = base_prices[category]
    unit_price = np.random.uniform(min_price, max_price)
    
    # Seasonal and weekday effects
    base_quantity = np.random.poisson(2) + 1
    if date.month == 12:  # December boost
        quantity = int(base_quantity * np.random.uniform(2, 4))
    elif date.month == 6:  # June boost
        quantity = int(base_quantity * np.random.uniform(1.5, 2.5))
    elif date.weekday() >= 5:  # Weekend boost
        quantity = int(base_quantity * np.random.uniform(1.2, 1.8))
    else:
        quantity = base_quantity
    
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

# Enhanced data preprocessing
print("🚀 ENHANCED SALES DATA ANALYSIS DASHBOARD")
print("=" * 50)

# Data quality checks
initial_count = len(df)
df = df.drop_duplicates()
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# Add enhanced time-based features
df['YearMonth'] = df['OrderDate'].dt.to_period('M')
df['Year'] = df['OrderDate'].dt.year
df['Month'] = df['OrderDate'].dt.month
df['Quarter'] = df['OrderDate'].dt.quarter
df['DayOfWeek'] = df['OrderDate'].dt.day_name()
df['Weekend'] = df['OrderDate'].dt.weekday >= 5
df['MonthName'] = df['OrderDate'].dt.month_name()

print(f"📊 Final dataset shape: {df.shape}")
print(f"📅 Date range: {df['OrderDate'].min().date()} to {df['OrderDate'].max().date()}")

# Calculate enhanced metrics
total_sales = df['TotalSales'].sum()
total_orders = len(df)
avg_order_value = total_sales / total_orders
unique_customers = np.random.randint(800, 1200)  # Simulated
avg_sales_per_customer = total_sales / unique_customers

# Enhanced KPI calculations
monthly_sales = df.groupby('YearMonth')['TotalSales'].sum()
sales_growth = ((monthly_sales.iloc[-1] - monthly_sales.iloc[-2]) / monthly_sales.iloc[-2]) * 100

print(f"\n🎯 KEY PERFORMANCE INDICATORS")
print(f"💰 Total Sales: ${total_sales:,.2f}")
print(f"📦 Total Orders: {total_orders:,}")
print(f"👥 Unique Customers: {unique_customers:,}")
print(f"💵 Average Order Value: ${avg_order_value:.2f}")
print(f"📈 Monthly Sales Growth: {sales_growth:.1f}%")

# Create FANTABULOUS VISUALIZATIONS
print("\n🎨 GENERATING FANTABULOUS VISUALIZATIONS...")

# 1. ENHANCED MATPLOTLIB DASHBOARD
fig = plt.figure(figsize=(20, 16))
fig.suptitle('🚀 ULTIMATE SALES ANALYTICS DASHBOARD', fontsize=24, fontweight='bold', y=0.98)

# Create grid specification for complex layout
gs = fig.add_gridspec(4, 4)

# 1.1 KPI Summary (Top Row)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[0, 2])
ax4 = fig.add_subplot(gs[0, 3])

kpi_axes = [ax1, ax2, ax3, ax4]
kpi_values = [total_sales/1e6, total_orders, avg_order_value, sales_growth]
kpi_labels = ['Total Sales ($M)', 'Total Orders', 'Avg Order Value ($)', 'Sales Growth (%)']
kpi_colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']

for ax, value, label, color in zip(kpi_axes, kpi_values, kpi_labels, kpi_colors):
    ax.text(0.5, 0.6, f'{value:,.1f}' if 'Growth' not in label else f'{value:.1f}%', 
            ha='center', va='center', fontsize=20, fontweight='bold', color=color)
    ax.text(0.5, 0.3, label, ha='center', va='center', fontsize=12)
    ax.set_facecolor('#f8f9fa')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    for spine in ax.spines.values():
        spine.set_color('#ddd')

# 1.2 Monthly Sales Trend with Annotations
ax5 = fig.add_subplot(gs[1, :2])
monthly_sales_plot = df.groupby('YearMonth')['TotalSales'].sum()
monthly_sales_plot.index = monthly_sales_plot.index.astype(str)

ax5.plot(monthly_sales_plot.index, monthly_sales_plot.values/1000, 
         linewidth=3, marker='o', markersize=6, color='#FF6B6B', alpha=0.8)
ax5.fill_between(monthly_sales_plot.index, monthly_sales_plot.values/1000, alpha=0.3, color='#FF6B6B')

# Highlight peak months
peak_month = monthly_sales_plot.idxmax()
peak_value = monthly_sales_plot.max()/1000
ax5.annotate(f'Peak: ${peak_value:,.0f}K', xy=(peak_month, peak_value), 
             xytext=(10, 10), textcoords='offset points',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

ax5.set_title('📈 Monthly Sales Trend (Thousands $)', fontsize=14, fontweight='bold', pad=20)
ax5.set_ylabel('Sales ($ Thousands)')
ax5.tick_params(axis='x', rotation=45)
ax5.grid(True, alpha=0.3)

# 1.3 Category Performance - Enhanced Pie Chart
ax6 = fig.add_subplot(gs[1, 2:])
sales_by_category = df.groupby('ProductCategory')['TotalSales'].sum().sort_values(ascending=False)

# Create donut chart
wedges, texts, autotexts = ax6.pie(sales_by_category.values, labels=sales_by_category.index, 
                                   autopct='%1.1f%%', startangle=90,
                                   colors=plt.cm.Set3(np.linspace(0, 1, len(sales_by_category))))
plt.setp(autotexts, size=10, weight="bold", color='white')
centre_circle = plt.Circle((0,0),0.70,fc='white')
ax6.add_artist(centre_circle)
ax6.set_title('🏷️ Sales Distribution by Category', fontsize=14, fontweight='bold', pad=20)

# 1.4 Top Products Horizontal Bar Chart
ax7 = fig.add_subplot(gs[2, :2])
top_products = df.groupby('ProductName').agg({'TotalSales': 'sum', 'Quantity': 'sum'}).nlargest(10, 'TotalSales')

bars = ax7.barh(range(len(top_products)), top_products['TotalSales']/1000, 
                color=plt.cm.viridis(np.linspace(0, 1, len(top_products))))
ax7.set_yticks(range(len(top_products)))
ax7.set_yticklabels(top_products.index, fontsize=10)
ax7.set_xlabel('Sales ($ Thousands)')
ax7.set_title('🏆 Top 10 Products by Revenue', fontsize=14, fontweight='bold', pad=20)

# Add value labels on bars
for i, bar in enumerate(bars):
    width = bar.get_width()
    ax7.text(width + 0.1, bar.get_y() + bar.get_height()/2, f'${width:,.0f}K', 
             ha='left', va='center', fontsize=9)

# 1.5 Daily Sales Pattern
ax8 = fig.add_subplot(gs[2, 2:])
daily_pattern = df.groupby('DayOfWeek')['TotalSales'].mean()
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
daily_pattern = daily_pattern.reindex(day_order)

bars = ax8.bar(range(len(daily_pattern)), daily_pattern, 
               color=plt.cm.coolwarm(np.linspace(0, 1, len(daily_pattern))))
ax8.set_xticks(range(len(daily_pattern)))
ax8.set_xticklabels([day[:3] for day in daily_pattern.index])
ax8.set_title('📅 Average Sales by Day of Week', fontsize=14, fontweight='bold', pad=20)
ax8.set_ylabel('Average Sales ($)')

# 1.6 Seasonal Heatmap
ax9 = fig.add_subplot(gs[3, :])
monthly_pivot = df.pivot_table(values='TotalSales', index='Year', columns='Month', aggfunc='sum')
monthly_pivot = monthly_pivot / 1000  # Convert to thousands

im = ax9.imshow(monthly_pivot.values, cmap='YlOrRd', aspect='auto')
ax9.set_xticks(range(12))
ax9.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax9.set_yticks(range(len(monthly_pivot.index)))
ax9.set_yticklabels(monthly_pivot.index)
ax9.set_title('🔥 Sales Heatmap by Year and Month ($ Thousands)', fontsize=14, fontweight='bold', pad=20)

# Add values to heatmap
for i in range(len(monthly_pivot.index)):
    for j in range(12):
        text = ax9.text(j, i, f'{monthly_pivot.iloc[i, j]:.0f}K',
                       ha="center", va="center", color="black" if monthly_pivot.iloc[i, j] > monthly_pivot.values.mean() else "white",
                       fontsize=8, fontweight='bold')

plt.colorbar(im, ax=ax9, label='Sales ($ Thousands)')

plt.tight_layout()
plt.subplots_adjust(top=0.94)
plt.show()

# 2. INTERACTIVE PLOTLY DASHBOARD
print("\n🔄 CREATING INTERACTIVE PLOTLY DASHBOARD...")

# Create interactive subplots
fig_interactive = make_subplots(
    rows=3, cols=2,
    subplot_titles=('📈 Monthly Sales Trend', '🏷️ Sales by Category', 
                   '🏆 Top Products', '📅 Daily Sales Pattern',
                   '🔥 Sales Heatmap', '📊 Quantity vs Price Distribution'),
    specs=[[{"type": "scatter"}, {"type": "pie"}],
           [{"type": "bar"}, {"type": "bar"}],
           [{"type": "heatmap"}, {"type": "scatter"}]],
    vertical_spacing=0.08,
    horizontal_spacing=0.08
)

# 2.1 Monthly Trend
fig_interactive.add_trace(
    go.Scatter(x=monthly_sales_plot.index, y=monthly_sales_plot.values/1000,
               mode='lines+markers', name='Monthly Sales',
               line=dict(width=4, color='#FF6B6B'),
               marker=dict(size=8)),
    row=1, col=1
)

# 2.2 Category Pie Chart
fig_interactive.add_trace(
    go.Pie(labels=sales_by_category.index, values=sales_by_category.values,
           name='Category Sales', hole=0.4,
           marker=dict(colors=px.colors.qualitative.Set3)),
    row=1, col=2
)

# 2.3 Top Products
fig_interactive.add_trace(
    go.Bar(x=top_products['TotalSales']/1000, y=top_products.index,
           orientation='h', name='Top Products',
           marker=dict(color=px.colors.sequential.Viridis)),
    row=2, col=1
)

# 2.4 Daily Pattern
fig_interactive.add_trace(
    go.Bar(x=day_order, y=daily_pattern.values,
           name='Daily Sales',
           marker=dict(color=px.colors.sequential.Plasma)),
    row=2, col=2
)

# 2.5 Heatmap
fig_interactive.add_trace(
    go.Heatmap(z=monthly_pivot.values,
               x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
               y=monthly_pivot.index.astype(str),
               colorscale='YlOrRd',
               showscale=False),
    row=3, col=1
)

# 2.6 Scatter plot - Price vs Quantity
fig_interactive.add_trace(
    go.Scatter(x=df['UnitPrice'], y=df['Quantity'],
               mode='markers', name='Price vs Quantity',
               marker=dict(size=8, color=df['TotalSales'],
                          colorscale='Viridis', showscale=True,
                          colorbar=dict(title="Total Sales"))),
    row=3, col=2
)

# Update layout for interactive dashboard
fig_interactive.update_layout(
    title_text='🚀 INTERACTIVE SALES ANALYTICS DASHBOARD',
    title_x=0.5,
    height=1200,
    showlegend=False,
    template='plotly_white',
    font=dict(size=12)
)

# Update axes labels
fig_interactive.update_xaxes(title_text="Month", row=1, col=1)
fig_interactive.update_yaxes(title_text="Sales ($ Thousands)", row=1, col=1)
fig_interactive.update_xaxes(title_text="Sales ($ Thousands)", row=2, col=1)
fig_interactive.update_yaxes(title_text="Products", row=2, col=1)
fig_interactive.update_xaxes(title_text="Day of Week", row=2, col=2)
fig_interactive.update_yaxes(title_text="Average Sales ($)", row=2, col=2)
fig_interactive.update_xaxes(title_text="Unit Price ($)", row=3, col=2)
fig_interactive.update_yaxes(title_text="Quantity", row=3, col=2)

fig_interactive.show()

# 3. ADVANCED ANALYTICS & INSIGHTS
print("\n🔍 GENERATING ADVANCED INSIGHTS...")

# Calculate advanced metrics
category_performance = df.groupby('ProductCategory').agg({
    'TotalSales': ['sum', 'mean'],
    'Quantity': 'sum',
    'OrderDate': 'count'
}).round(2)

category_performance.columns = ['Total_Sales', 'Avg_Transaction', 'Total_Quantity', 'Order_Count']
category_performance['Sales_Per_Order'] = category_performance['Total_Sales'] / category_performance['Order_Count']

# Seasonality analysis
monthly_analysis = df.groupby('MonthName').agg({
    'TotalSales': ['sum', 'mean', 'count']
}).round(2)
monthly_analysis.columns = ['Monthly_Sales', 'Avg_Order_Value', 'Order_Count']
monthly_analysis = monthly_analysis.reindex([
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
])

print("\n📋 CATEGORY PERFORMANCE SUMMARY:")
print(category_performance.sort_values('Total_Sales', ascending=False))

print("\n🌞 SEASONALITY ANALYSIS:")
print(monthly_analysis)

# 4. ENHANCED EXPORT WITH MULTIPLE SHEETS
print("\n💾 EXPORTING ENHANCED REPORT...")

with pd.ExcelWriter('fantabulous_sales_analysis_report.xlsx', engine='xlsxwriter') as writer:
    # Main data
    df.to_excel(writer, sheet_name='Raw_Data', index=False)
    
    # Summary sheets
    category_performance.to_excel(writer, sheet_name='Category_Performance')
    monthly_analysis.to_excel(writer, sheet_name='Seasonal_Analysis')
    top_products.to_excel(writer, sheet_name='Top_Products')
    monthly_sales_plot.to_excel(writer, sheet_name='Monthly_Trend', header=['TotalSales'])
    
    # Get workbook and add formatting
    workbook = writer.book
    
    # Add formats
    header_format = workbook.add_format({
        'bold': True, 'text_wrap': True, 'valign': 'top', 'fg_color': '#D7E4BC',
        'border': 1, 'font_color': '#000000'
    })
    
    money_format = workbook.add_format({'num_format': '$#,##0.00'})
    percent_format = workbook.add_format({'num_format': '0.0%'})
    
    # Apply formatting to sheets
    for sheet_name in writer.sheets:
        worksheet = writer.sheets[sheet_name]
        worksheet.set_column('A:Z', 15)  # Adjust column width
        
        # Add autofilter and format headers
        if sheet_name != 'Raw_Data':
            worksheet.autofilter(0, 0, 0, worksheet.dim_colmax)
        
        # Format headers
        for col_num, value in enumerate(worksheet.table[0]):
            worksheet.write(0, col_num, value, header_format)

print("✅ ANALYSIS COMPLETE!")
print("📊 Static Dashboard: Enhanced matplotlib visualizations")
print("🖱️  Interactive Dashboard: Plotly interactive charts")
print("💾 Excel Report: 'fantabulous_sales_analysis_report.xlsx'")
print("🎯 Key Insights: Category performance, seasonality, top products")

# Bonus: Print some fun insights
best_category = category_performance['Total_Sales'].idxmax()
worst_category = category_performance['Total_Sales'].idxmin()
best_month = monthly_analysis['Monthly_Sales'].idxmax()

print(f"\n🎉 FUN INSIGHTS:")
print(f"⭐ Best Performing Category: {best_category}")
print(f"📉 Category Needing Attention: {worst_category}")
print(f"🎄 Highest Sales Month: {best_month}")
print(f"💡 Weekend vs Weekday Sales Ratio: {(df[df['Weekend']]['TotalSales'].mean() / df[~df['Weekend']]['TotalSales'].mean()):.2f}x")