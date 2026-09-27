import pandas as pd
import pyodbc

# Load CSV
csv_path = "data/raw/sales_data.csv"
df = pd.read_csv(csv_path)

# SQL Server connection
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=sales_analytics;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

cursor = conn.cursor()

# Insert data
sql = """
INSERT INTO sales (
    order_id,
    order_date,
    customer_id,
    category,
    product,
    region,
    quantity,
    unit_price,
    discount_pct,
    sales,
    cost,
    profit,
    payment_method
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

for _, row in df.iterrows():
    cursor.execute(
        sql,
        row["order_id"],
        row["order_date"],
        row["customer_id"],
        row["category"],
        row["product"],
        row["region"],
        int(row["quantity"]),
        float(row["unit_price"]),
        int(row["discount"]),
        float(row["sales"]),
        float(row["cost"]),
        float(row["profit"]),
        row["payment_method"]
    )

conn.commit()

print(f"Successfully loaded {len(df)} rows into SQL Server.")

cursor.close()
conn.close()