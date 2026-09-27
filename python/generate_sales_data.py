import pandas as pd
import numpy as np

# Make the data reproducible
np.random.seed(42)

# Number of sales transactions
n = 1500

# Product catalogue
products = {
    "Laptop": ("Electronics", 650),
    "Smartphone": ("Electronics", 450),
    "Headphones": ("Electronics", 80),
    "Monitor": ("Electronics", 220),
    "Keyboard": ("Electronics", 45),
    "Office Chair": ("Furniture", 180),
    "Desk": ("Furniture", 250),
    "Bookshelf": ("Furniture", 140),
    "Running Shoes": ("Sports", 90),
    "Yoga Mat": ("Sports", 35),
    "Dumbbells": ("Sports", 60),
    "Backpack": ("Accessories", 50),
    "Watch": ("Accessories", 120),
    "Sunglasses": ("Accessories", 70),
}

product_names = list(products.keys())

regions = ["North", "South", "East", "West", "Central"]

payment_methods = [
    "Credit Card",
    "Debit Card",
    "UPI",
    "Cash",
    "Net Banking"
]

customers = [f"CUST{str(i).zfill(4)}" for i in range(1, 301)]

# Generate random data
data = []

for i in range(1, n + 1):

    product = np.random.choice(product_names)
    category, base_price = products[product]

    quantity = np.random.randint(1, 6)
    discount = np.random.choice(
        [0, 5, 10, 15, 20],
        p=[0.20, 0.30, 0.30, 0.15, 0.05]
    )

    unit_price = round(
        base_price * np.random.uniform(0.90, 1.10),
        2
    )

    sales = round(
        quantity * unit_price * (1 - discount / 100),
        2
    )

    cost = round(
        quantity * unit_price * np.random.uniform(0.55, 0.75),
        2
    )

    profit = round(sales - cost, 2)

    data.append([
        f"ORD{str(i).zfill(5)}",
        np.random.choice(
            pd.date_range("2025-01-01", "2025-12-31")
        ),
        np.random.choice(customers),
        category,
        product,
        np.random.choice(regions),
        quantity,
        unit_price,
        discount,
        sales,
        cost,
        profit,
        np.random.choice(payment_methods)
    ])

# Create DataFrame
columns = [
    "order_id",
    "order_date",
    "customer_id",
    "category",
    "product",
    "region",
    "quantity",
    "unit_price",
    "discount",
    "sales",
    "cost",
    "profit",
    "payment_method"
]

df = pd.DataFrame(data, columns=columns)

# Sort by date
df = df.sort_values("order_date").reset_index(drop=True)

# Save raw dataset
output_path = "data/raw/sales_data.csv"
df.to_csv(output_path, index=False)

print(f"Dataset created successfully!")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"Saved to: {output_path}")
print("\nFirst 5 rows:")
print(df.head())