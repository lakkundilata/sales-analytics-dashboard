import pandas as pd

# Load sales data
df = pd.read_csv("data/raw/sales_data.csv")

print("===== SALES DATA ANALYSIS =====")

# Basic information
print("\nDataset shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Basic statistics
print("\nBasic statistics:")
print(df.describe())

# Total sales
total_sales = df["sales"].sum()
print(f"\nTotal Sales: {total_sales:,.2f}")

# Total profit
total_profit = df["profit"].sum()
print(f"Total Profit: {total_profit:,.2f}")

# Profit margin
profit_margin = (total_profit / total_sales) * 100
print(f"Profit Margin: {profit_margin:.2f}%")

# Sales by category
category_analysis = (
    df.groupby("category")
    .agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum"),
        total_orders=("order_id", "count")
    )
    .sort_values("total_sales", ascending=False)
)

print("\n===== SALES BY CATEGORY =====")
print(category_analysis)

# Sales by region
region_analysis = (
    df.groupby("region")
    .agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum"),
        total_orders=("order_id", "count")
    )
    .sort_values("total_sales", ascending=False)
)

print("\n===== SALES BY REGION =====")
print(region_analysis)

# Sales by payment method
payment_analysis = (
    df.groupby("payment_method")
    .agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum"),
        total_orders=("order_id", "count")
    )
    .sort_values("total_sales", ascending=False)
)

print("\n===== SALES BY PAYMENT METHOD =====")
print(payment_analysis)

# Monthly analysis
df["order_date"] = pd.to_datetime(df["order_date"])

monthly_analysis = (
    df.groupby(df["order_date"].dt.to_period("M"))
    .agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum"),
        total_orders=("order_id", "count")
    )
)

print("\n===== MONTHLY SALES =====")
print(monthly_analysis)

print("\n===== ANALYSIS COMPLETED SUCCESSFULLY =====")