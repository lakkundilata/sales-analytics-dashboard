# Sales Analytics Dashboard

Sales data analysis and interactive dashboard built using **Python, SQL Server, and Power BI**.

## 📌 Project Overview

This project analyzes sales transaction data to identify sales performance, profitability, product trends, regional performance, and payment-method patterns.

The project demonstrates an end-to-end data analytics workflow:

**Data → Python → SQL → Power BI → Business Insights**

## 🛠️ Tools & Technologies

- Python
  - Pandas
  - NumPy
  - Matplotlib
  - Seaborn
- SQL Server
- Power BI
- Git & GitHub

## 📊 Dataset

- **Records:** 1,500
- **Columns:** 13
- **Missing values:** 0
- **Duplicate rows:** 0

Key fields include:

- Order ID
- Order Date
- Customer ID
- Category
- Product
- Region
- Quantity
- Unit Price
- Discount
- Sales
- Cost
- Profit
- Payment Method

## 📈 Key Performance Indicators

| KPI | Value |
|---|---:|
| Total Sales | 734,252.94 |
| Total Profit | 218,727.10 |
| Total Orders | 1,500 |
| Total Quantity | 45,571 |
| Profit Margin | 29.79% |

## 🔎 Analysis Performed

### Python

- Data loading and validation
- Missing-value analysis
- Descriptive statistics
- Sales and profit analysis
- Category analysis
- Regional analysis
- Monthly sales analysis
- Payment-method analysis

### SQL Server

Analytical SQL queries were created to analyze:

- Total sales
- Total profit
- Profit margin
- Top-performing products
- Sales by category
- Sales by region
- Monthly sales and profit
- Sales by payment method

### Power BI

The interactive dashboard includes:

- Total Sales KPI
- Total Profit KPI
- Total Orders KPI
- Profit Margin KPI
- Sales by Category
- Profit by Product
- Sales by Region
- Profit by Region
- Quantity by Product
- Monthly Sales Trend
- Region slicer
- Category slicer
- Order Date slicer

## 🏆 Top Sales Categories

| Category | Sales |
|---|---:|
| Electronics | 430,618.00 |
| Furniture | 177,351.12 |
| Accessories | 70,879.42 |
| Sports | 55,404.40 |

## 📁 Project Structure

```text
sales-analytics-dashboard/
│
├── data/
│   └── raw/
│       └── sales_data.csv
│
├── docs/
│
├── powerbi/
│   └── Sales_Analytics_Dashboard.pbix
│
├── python/
│   ├── generate_sales_data.py
│   ├── load_sales_to_sql.py
│   └── analyze_sales.py
│
├── sql/
│   ├── 01_create_sales_table.sql
│   ├── 02_load_sales_data.sql
│   └── 03_analysis_queries.sql
│
├── .gitignore
├── .gitattributes
└── README.md

## Hwow to Run

1. Clone the repository

```markdown
```bash
git clone https://github.com/lakkundilata/sales-analytics-dashboard.git

2. Create a Python virtual environment

* python -m venv .venv

3. Intall required Python packages

* pip install pandas numpy matplotlib seaborn openpyxl pyodbc

4. Run the python analysis

* python python/analyze_sales.py

5. SQL Analysis

Open the SQL files in SQL Server Management Studio or VS Code with the SQL Server extension and execute the scripts against the sales_analytics database.

6. Power BI

Open:

powerbi/Sales_Analytics_Dashboard.pbix

to explore the interactive dashboard.

####Project Objective

The objective of this project is to demonstrate practical skills in data cleaning, exploratory analysis, SQL querying, business intelligence, dashboard development, and data storytelling using a complete end-to-end sales analytics workflow.
