<div align="center">

# SQL for Business Analytics

**SQL-based Business Analytics project performing data querying, aggregation, and business insights generation using Python and SQLite.**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

</div>

---

## Overview

This project demonstrates the application of SQL for analyzing **telecom customer churn data**. It extracts business insights, calculates key performance metrics, and supports data-driven decision-making through structured querying and aggregation using Python and SQLite.

## Objectives

- Write basic and advanced SQL queries
- Perform data aggregation using `SUM`, `AVG`, `COUNT`, and `GROUP BY`
- Analyze customer churn patterns across multiple dimensions
- Generate key business KPIs (Churn Rate, Revenue, High-Value Customers)

## Project Structure

```
SQL-for-Business-Analytics/
├── datasets/
│   └── Data Set For Task/
│       ├── Churn Prdiction Data/
│       │   ├── churn-bigml-80.csv      # Training data (80%)
│       │   └── churn-bigml-20.csv      # Test data (20%)
│       ├── 1) iris.csv
│       ├── 3) Sentiment dataset.csv
│       └── 4) house Prediction Data Set.csv
├── SQL_Analytics/
│   ├── sql_analysis.py                  # Main analysis script
│   ├── sql_queries_output.txt           # Query output reference
│   └── SQL_Report.pdf                   # Generated report
├── business_analytics.db                # SQLite database (generated)
├── requirements.txt
├── .gitignore
└── README.md
```

## Tools & Technologies

| Tool | Purpose |
|------|---------|
| **SQL (SQLite)** | Data querying and aggregation |
| **Python** | Scripting and automation |
| **Pandas** | Data manipulation and analysis |

## Analysis Performed

### 1. Basic Queries
- Data exploration with `SELECT`, `WHERE`, `ORDER BY`
- Customer segmentation and churn filtering

### 2. Aggregation Queries
- Revenue and usage analysis by time period
- State-wise customer distribution
- International plan impact analysis
- High-churn state identification

### 3. Advanced Queries
- `CASE` expression for customer categorization
- Subqueries for above-average charge analysis
- Multi-metric churn comparison

### 4. Business KPIs
- **Churn Rate**: Overall customer attrition percentage
- **Revenue Analysis**: Total and per-customer revenue
- **High-Value Customers**: Customers with charges > $60

## Key Insights

- Higher service call frequency is **strongly associated** with churn.
- International plan subscribers show **higher churn probability**.
- Revenue contribution varies significantly across states.

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/methila-2056/methila-2056-SQL-for-Business-Analytics.git
   cd methila-2056-SQL-for-Business-Analytics
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the analysis**
   ```bash
   python SQL_Analytics/sql_analysis.py
   ```

### Redirecting Output

```bash
python SQL_Analytics/sql_analysis.py > SQL_Analytics/sql_queries_output.txt
```

## Sample Output

```
================================================================================
QUERY: 4.1 - Overall Churn Rate (KEY METRIC)
================================================================================
SQL:
SELECT
    COUNT(CASE WHEN Churn = 'True' THEN 1 END) as churned_customers,
    COUNT(*) as total_customers,
    ROUND(COUNT(CASE WHEN Churn = 'True' THEN 1 END) * 100.0 / COUNT(*), 2) as churn_rate_percentage
FROM customers

   churned_customers  total_customers  churn_rate_percentage
0                388             2666                  14.55
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built by [Methila](https://github.com/methila-2056)**

</div>
