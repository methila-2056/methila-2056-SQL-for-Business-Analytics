-- 1. Basic Queries
-- Data exploration and filtering

-- 1.1 Select first 10 customers
SELECT * FROM customers LIMIT 10;

-- 1.2 Select specific columns
SELECT State, [Account length], [Total day charge]
FROM customers
LIMIT 10;

-- 1.3 Filter customers who churned
SELECT * FROM customers
WHERE Churn = 1
LIMIT 10;

-- 1.4 Top 10 customers by day charge
SELECT State, [Total day charge]
FROM customers
ORDER BY [Total day charge] DESC
LIMIT 10;
