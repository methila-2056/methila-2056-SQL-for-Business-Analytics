-- 3. Advanced Queries
-- Subqueries, CASE expressions, window functions

-- 3.1 Categorize customers by service calls
SELECT
    [Customer service calls],
    COUNT(*) AS customer_count,
    CASE
        WHEN [Customer service calls] = 0 THEN 'No Calls'
        WHEN [Customer service calls] BETWEEN 1 AND 3 THEN 'Low'
        WHEN [Customer service calls] BETWEEN 4 AND 6 THEN 'Medium'
        ELSE 'High'
    END AS call_category
FROM customers
GROUP BY [Customer service calls]
ORDER BY [Customer service calls];

-- 3.2 Customers with above-average charges
SELECT State, [Total day charge]
FROM customers
WHERE [Total day charge] > (
    SELECT AVG([Total day charge]) FROM customers
)
ORDER BY [Total day charge] DESC
LIMIT 10;

-- 3.3 Churn analysis with multiple metrics
SELECT
    Churn,
    COUNT(*) AS count,
    ROUND(AVG([Account length]), 2) AS avg_account_length,
    ROUND(AVG([Total day charge] + [Total eve charge] + [Total night charge]), 2) AS avg_total_charge,
    ROUND(AVG([Customer service calls]), 2) AS avg_service_calls
FROM customers
GROUP BY Churn;
