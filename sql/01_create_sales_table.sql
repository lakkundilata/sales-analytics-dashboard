USE sales_analytics;

DROP TABLE IF EXISTS sales;

CREATE TABLE sales (
    order_id VARCHAR(20),
    order_date DATE,
    customer_id VARCHAR(20),
    category VARCHAR(50),
    product VARCHAR(100),
    region VARCHAR(50),
    quantity INT,
    unit_price DECIMAL(10,2),
    discount_pct INT,
    sales DECIMAL(12,2),
    cost DECIMAL(12,2),
    profit DECIMAL(12,2),
    payment_method VARCHAR(30)
);