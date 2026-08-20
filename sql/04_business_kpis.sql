-- 4. Business KPIs
-- Key performance indicators for decision-making

-- 4.1 Overall Churn Rate
SELECT
    COUNT(CASE WHEN Churn = 1 THEN 1 END) AS churned_customers,
    COUNT(*) AS total_customers,
    ROUND(COUNT(CASE WHEN Churn = 1 THEN 1 END) * 100.0 / COUNT(*), 2) AS churn_rate_percentage
FROM customers;

-- 4.2 Revenue Analysis
SELECT
    ROUND(SUM([Total day charge] + [Total eve charge] + [Total night charge] + [Total intl charge]), 2) AS total_revenue,
    ROUND(AVG([Total day charge] + [Total eve charge] + [Total night charge] + [Total intl charge]), 2) AS avg_revenue_per_customer,
    COUNT(*) AS total_customers
FROM customers;

-- 4.3 High-value customers by state (charges > $60)
SELECT
    State,
    COUNT(*) AS high_value_customers,
    ROUND(AVG([Total day charge] + [Total eve charge] + [Total night charge]), 2) AS avg_charges
FROM customers
WHERE ([Total day charge] + [Total eve charge] + [Total night charge]) > 60
GROUP BY State
ORDER BY high_value_customers DESC
LIMIT 10;
