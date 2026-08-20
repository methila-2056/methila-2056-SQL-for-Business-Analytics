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

### Data Aggregation

```
QUERY: 2.1 - Total number of customers
   total_customers
0             2666

QUERY: 2.2 - Average charges by time period
   avg_day_charge  avg_eve_charge  avg_night_charge
0           30.51           17.03              9.05

QUERY: 2.3 - Customer count by state (Top 10)
  State  customer_count
0    WV              88
1    MN              70
2    NY              68
3    VA              67
4    WY              66
5    OH              66
6    AL              66
7    OR              62
8    WI              61
9    NV              61

QUERY: 2.5 - Analysis by International Plan
  International plan  total_customers  avg_intl_charge  total_intl_revenue
0                 No             2396             2.75             6591.61
1                Yes              270             2.88              778.52
```

### Advanced Queries

```
QUERY: 3.1 - Categorize customers by service calls
   Customer service calls  customer_count call_category
0                       0             555      No Calls
1                       1             945           Low
2                       2             608           Low
3                       3             348           Low
4                       4             133        Medium
5                       5              49        Medium
6                       6              17        Medium
7                       7               8          High
8                       8               1          High
9                       9               2          High

QUERY: 3.3 - Churn analysis with multiple metrics
   Churn  count  avg_account_length  avg_total_charge  avg_service_calls
0      0   2278              100.33             55.69               1.45
1      1    388              102.32             61.92               2.21
```

### Business KPIs

```
QUERY: 4.2 - Revenue Analysis
   total_revenue  avg_revenue_per_customer  total_customers
0      158260.84                     59.36             2666

QUERY: 4.3 - High-value customers by state (charges > $60)
  State  high_value_customers  avg_charges
0    WY                    29        65.79
1    WV                    28        65.82
2    OH                    28        67.68
3    MN                    28        67.28
4    KS                    27        68.33
5    IN                    27        67.20
6    NJ                    26        67.02
7    MD                    26        68.94
8    FL                    26        66.41
9    AL                    26        66.67
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built by [Methila](https://github.com/methila-2056)**

</div>
