# Data Dictionary

## customers Table

The primary dataset used for churn analysis. Each row represents one telecom customer.

| Column | Type | Description |
|--------|------|-------------|
| `State` | TEXT | Two-letter US state code (e.g., KS, OH, NJ) |
| `Account length` | INTEGER | Number of months the customer has been with the company |
| `Area code` | INTEGER | Telephone area code |
| `International plan` | TEXT | Whether the customer has an international calling plan (`Yes`/`No`) |
| `Voice mail plan` | TEXT | Whether the customer has a voice mail plan (`Yes`/`No`) |
| `Number vmail messages` | INTEGER | Number of voice mail messages |
| `Total day minutes` | REAL | Total minutes used during the day |
| `Total day calls` | INTEGER | Total number of calls made during the day |
| `Total day charge` | REAL | Total charges for daytime calls ($) |
| `Total eve minutes` | REAL | Total minutes used during the evening |
| `Total eve calls` | INTEGER | Total number of calls made during the evening |
| `Total eve charge` | REAL | Total charges for evening calls ($) |
| `Total night minutes` | REAL | Total minutes used during the night |
| `Total night calls` | INTEGER | Total number of calls made during the night |
| `Total night charge` | REAL | Total charges for nighttime calls ($) |
| `Total intl minutes` | REAL | Total minutes used for international calls |
| `Total intl calls` | INTEGER | Total number of international calls |
| `Total intl charge` | REAL | Total charges for international calls ($) |
| `Customer service calls` | INTEGER | Number of calls made to customer service |
| `Churn` | INTEGER | Whether the customer churned (`1` = churned, `0` = retained) |

## Source

- **Dataset**: [Telco Customer Churn](https://www.kaggle.com/datasets/mnassrib/telecom-churn)
- **Training set**: `churn-bigml-80.csv` (2,666 rows)
- **Test set**: `churn-bigml-20.csv` (667 rows)

## Key Metrics Derived

| Metric | Formula | Description |
|--------|---------|-------------|
| Churn Rate | `COUNT(Churn=1) / COUNT(*) * 100` | Percentage of customers who left |
| Total Revenue | `SUM(day_charge + eve_charge + night_charge + intl_charge)` | Combined revenue from all charge types |
| Avg Revenue per Customer | `Total Revenue / Total Customers` | Mean revenue per customer |
| High-Value Customer | `day_charge + eve_charge + night_charge > 60` | Customers spending above $60 |
