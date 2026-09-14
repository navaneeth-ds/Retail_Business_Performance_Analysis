-- Retail Business Performance & Profitability Analysis
-- Dataset: Superstore

CREATE DATABASE IF NOT EXISTS retail_analysis;
USE retail_analysis;

-- Import the Superstore CSV into a table named superstore
-- After importing the data, run the analysis queries below.

-- 1. View the dataset
SELECT *
FROM superstore
LIMIT 10;

-- 2. Total sales and total profit
SELECT
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM superstore;

-- 3. Sales and profit by category
SELECT
    Category,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM superstore
GROUP BY Category
ORDER BY total_sales DESC;

-- 4. Sales and profit by region
SELECT
    Region,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM superstore
GROUP BY Region
ORDER BY total_sales DESC;

-- 5. Sales by sub-category
SELECT
    `Sub-Category`,
    SUM(Sales) AS total_sales
FROM superstore
GROUP BY `Sub-Category`
ORDER BY total_sales DESC;

-- 6. Profit by sub-category
SELECT
    `Sub-Category`,
    SUM(Profit) AS total_profit
FROM superstore
GROUP BY `Sub-Category`
ORDER BY total_profit DESC;

-- 7. Top 10 products by sales
SELECT
    Product_Name,
    SUM(Sales) AS total_sales
FROM superstore
GROUP BY Product_Name
ORDER BY total_sales DESC
LIMIT 10;

-- 8. Loss-making products
SELECT
    Product_Name,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM superstore
GROUP BY Product_Name
HAVING total_profit < 0
ORDER BY total_profit ASC
LIMIT 10;

-- 9. Average discount by category
SELECT
    Category,
    AVG(Discount) AS average_discount
FROM superstore
GROUP BY Category
ORDER BY average_discount DESC;

-- 10. Discount versus profit summary
SELECT
    Discount,
    SUM(Profit) AS total_profit,
    SUM(Sales) AS total_sales
FROM superstore
GROUP BY Discount
ORDER BY Discount;