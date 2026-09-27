USE sales_analytics;
-- 3. Total Sales
SELECT
    SUM(sales) AS total_sales
FROM sales;

-- 4. Total Profit
SELECT
    SUM(profit) AS total_profit
FROM sales;

-- 5. Profit Margin
SELECT
    ROUND(SUM(profit) * 100.0 / SUM(sales), 2) AS profit_margin_pct
FROM sales;

-- 6. Sales by Category
SELECT
    category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales
GROUP BY category
ORDER BY total_sales DESC;

-- 7. Sales by Region
SELECT
    region,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales
GROUP BY region
ORDER BY total_sales DESC;

-- 8. Monthly Sales
SELECT
    YEAR(order_date) AS sales_year,
    MONTH(order_date) AS sales_month,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales
GROUP BY
    YEAR(order_date),
    MONTH(order_date)
ORDER BY
    sales_year,
    sales_month;

    -- 9. Sales by Payment Method
SELECT
    payment_method,
    COUNT(*) AS total_orders,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales
GROUP BY payment_method
ORDER BY total_sales DESC;

-- 10. Monthly Sales and Profit
SELECT
    YEAR(order_date) AS sales_year,
    MONTH(order_date) AS sales_month,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales
GROUP BY
    YEAR(order_date),
    MONTH(order_date)
ORDER BY
    sales_year,
    sales_month;

SELECT COUNT(*) AS total_rows
FROM sales;

SELECT TOP 10 *
FROM sales
ORDER BY order_date;