import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Generate sample sales data
@st.cache_data
def generate_sample_data():
    np.random.seed(42)
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
    
    # Data cleaning
    df = df.drop_duplicates()
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
    
    # Add time-based features
    df['YearMonth'] = df['OrderDate'].dt.to_period('M')
    df['Year'] = df['OrderDate'].dt.year
    df['Month'] = df['OrderDate'].dt.month
    df['MonthName'] = df['OrderDate'].dt.month_name()
    
    return df

# Main dashboard
def main():
    st.title("🚀 Sales Analytics Dashboard")
    st.markdown("---")
    
    # Generate data
    df = generate_sample_data()
    
    # Sidebar filters
    st.sidebar.header("🔧 Filters")
    
    # Date range filter
    min_date = df['OrderDate'].min().date()
    max_date = df['OrderDate'].max().date()
    start_date, end_date = st.sidebar.date_input(
        "Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Category filter
    categories = df['ProductCategory'].unique()
    selected_categories = st.sidebar.multiselect(
        "Product Categories",
        categories,
        default=categories
    )
    
    # Apply filters
    filtered_df = df[
        (df['OrderDate'].dt.date >= start_date) & 
        (df['OrderDate'].dt.date <= end_date) &
        (df['ProductCategory'].isin(selected_categories))
    ]
    
    # KPI Metrics
    st.header("📊 Key Performance Indicators")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_sales = filtered_df['TotalSales'].sum()
        st.metric("Total Revenue", f"${total_sales:,.2f}")
    
    with col2:
        total_orders = len(filtered_df)
        st.metric("Total Orders", f"{total_orders:,}")
    
    with col3:
        avg_order_value = total_sales / total_orders
        st.metric("Average Order Value", f"${avg_order_value:.2f}")
    
    with col4:
        unique_products = filtered_df['ProductName'].nunique()
        st.metric("Unique Products", unique_products)
    
    st.markdown("---")
    
    # Charts Row 1
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Monthly Sales Trend")
        monthly_sales = filtered_df.groupby('YearMonth')['TotalSales'].sum()
        monthly_sales.index = monthly_sales.index.astype(str)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(monthly_sales.index, monthly_sales.values / 1000, marker='o', linewidth=2, color='#FF6B6B')
        ax.set_xlabel('Month')
        ax.set_ylabel('Sales (Thousands $)')
        ax.tick_params(axis='x', rotation=45)
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
    
    with col2:
        st.subheader("🏷️ Sales by Category")
        sales_by_category = filtered_df.groupby('ProductCategory')['TotalSales'].sum()
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.pie(sales_by_category.values, labels=sales_by_category.index, autopct='%1.1f%%', 
               startangle=90, colors=sns.color_palette("Set2"))
        ax.set_title('Sales Distribution by Category')
        st.pyplot(fig)
    
    # Charts Row 2
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("🏆 Top 10 Products by Revenue")
        top_products = filtered_df.groupby('ProductName').agg({
            'TotalSales': 'sum',
            'Quantity': 'sum'
        }).nlargest(10, 'TotalSales')
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(range(len(top_products)), top_products['TotalSales'] / 1000, 
                color=plt.cm.viridis(np.linspace(0, 1, len(top_products))))
        ax.set_yticks(range(len(top_products)))
        ax.set_yticklabels(top_products.index)
        ax.set_xlabel('Total Sales (Thousands $)')
        ax.invert_yaxis()
        st.pyplot(fig)
    
    with col4:
        st.subheader("📅 Sales Seasonality")
        monthly_order = ['January', 'February', 'March', 'April', 'May', 'June',
                        'July', 'August', 'September', 'October', 'November', 'December']
        
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(data=filtered_df, x='MonthName', y='TotalSales', ax=ax, order=monthly_order)
        ax.set_xlabel('Month')
        ax.set_ylabel('Sales per Order ($)')
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig)
    
    st.markdown("---")
    
    # Data Summary Section
    st.header("📋 Data Summary")
    
    col5, col6 = st.columns(2)
    
    with col5:
        st.subheader("Top Products by Quantity")
        top_quantity = filtered_df.groupby('ProductName')['Quantity'].sum().nlargest(5)
        st.dataframe(top_quantity)
    
    with col6:
        st.subheader("Category Performance")
        category_perf = filtered_df.groupby('ProductCategory').agg({
            'TotalSales': 'sum',
            'Quantity': 'sum',
            'OrderDate': 'count'
        }).rename(columns={'OrderDate': 'OrderCount'})
        st.dataframe(category_perf)
    
    # Year-over-Year Growth
    st.subheader("📈 Growth Analysis")
    yearly_sales = filtered_df.groupby('Year')['TotalSales'].sum()
    if len(yearly_sales) > 1:
        growth_rate = ((yearly_sales.iloc[-1] - yearly_sales.iloc[-2]) / yearly_sales.iloc[-2]) * 100
        st.metric(
            f"Year-over-Year Growth ({yearly_sales.index[-2]} to {yearly_sales.index[-1]})",
            f"{growth_rate:.1f}%"
        )
    else:
        st.info("Not enough data for year-over-year comparison")
    
    # Raw Data Preview
    st.markdown("---")
    st.header("🔍 Data Preview")
    
    with st.expander("View Raw Data"):
        st.dataframe(filtered_df.head(100))
        
        # Download button
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="📥 Download Data as CSV",
            data=csv,
            file_name="sales_data.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    main()