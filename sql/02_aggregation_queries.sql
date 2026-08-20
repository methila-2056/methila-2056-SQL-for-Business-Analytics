-- 2. Aggregation Queries
-- SUM, AVG, COUNT, GROUP BY

-- 2.1 Total number of customers
SELECT COUNT(*) AS total_customers FROM customers;

-- 2.2 Average charges by time period
SELECT
    ROUND(AVG([Total day charge]), 2) AS avg_day_charge,
    ROUND(AVG([Total eve charge]), 2) AS avg_eve_charge,
    ROUND(AVG([Total night charge]), 2) AS avg_night_charge
FROM customers;

-- 2.3 Customer count by state (Top 10)
SELECT State, COUNT(*) AS customer_count
FROM customers
GROUP BY State
ORDER BY customer_count DESC
LIMIT 10;

-- 2.4 Total revenue by state (Top 10)
SELECT
    State,
    ROUND(SUM([Total day charge]), 2) AS total_revenue,
    COUNT(*) AS customers
FROM customers
GROUP BY State
ORDER BY total_revenue DESC
LIMIT 10;

-- 2.5 Analysis by International Plan
SELECT
    [International plan],
    COUNT(*) AS total_customers,
    ROUND(AVG([Total intl charge]), 2) AS avg_intl_charge,
    ROUND(SUM([Total intl charge]), 2) AS total_intl_revenue
FROM customers
GROUP BY [International plan];

-- 2.6 States with high churn (>5 customers)
SELECT
    State,
    COUNT(*) AS churn_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM customers), 2) AS churn_percentage
FROM customers
WHERE Churn = 1
GROUP BY State
HAVING churn_count > 5
ORDER BY churn_count DESC;
