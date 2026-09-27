USE sales_analytics;

BULK INSERT sales
FROM 'C:\Users\LENOVO\Documents\GitHub\sales-analytics-dashboard\data\raw\sales_data.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    TABLOCK
);

SELECT COUNT(*) AS total_rows
FROM sales;