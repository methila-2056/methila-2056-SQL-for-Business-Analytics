"""
SQL for Business Analytics - Codveda Internship Task 2

A comprehensive SQL analytics project that demonstrates data querying,
aggregation, and business insight generation using Python and SQLite.

Author: Methila
Date: 2026
"""

import argparse
import pandas as pd
import sqlite3
import sys
from datetime import datetime
from pathlib import Path


class SQLBusinessAnalytics:
    """Performs SQL-based business analytics on telecom customer churn data."""

    def __init__(self, db_name="business_analytics.db"):
        """Initialize database connection.

        Args:
            db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        print(f"Database '{db_name}' connected successfully.")

    def load_csv_to_db(self, csv_file, table_name):
        """Load a CSV file into the SQLite database as a table.

        Args:
            csv_file: Path to the CSV file.
            table_name: Name of the table to create.

        Returns:
            True if successful, False otherwise.
        """
        try:
            df = pd.read_csv(csv_file)
            df.to_sql(table_name, self.conn, if_exists="replace", index=False)
            print(f"Table '{table_name}' created with {len(df)} rows.")
            return True
        except Exception as e:
            print(f"Error loading {csv_file}: {e}")
            return False

    def execute_query(self, query, description=""):
        """Execute a SQL query and print results.

        Args:
            query: SQL query string to execute.
            description: Human-readable description of the query.

        Returns:
            DataFrame with query results, or None on error.
        """
        print(f"\n{'=' * 80}")
        print(f"QUERY: {description}")
        print(f"{'=' * 80}")
        print(f"SQL:\n{query}\n")

        try:
            df = pd.read_sql_query(query, self.conn)
            print(df.to_string())
            print(f"\nRows returned: {len(df)}")
            return df
        except Exception as e:
            print(f"Error: {e}")
            return None

    def basic_queries(self):
        """Execute basic SQL queries for data exploration."""
        print("\n" + "=" * 80)
        print("1. BASIC SQL QUERIES")
        print("=" * 80)

        self.execute_query(
            "SELECT * FROM customers LIMIT 10",
            "1.1 - Select first 10 customers",
        )

        self.execute_query(
            "SELECT State, [Account length], [Total day charge] FROM customers LIMIT 10",
            "1.2 - Select specific columns",
        )

        self.execute_query(
            "SELECT * FROM customers WHERE Churn = 1 LIMIT 10",
            "1.3 - Filter customers who churned",
        )

        self.execute_query(
            """SELECT State, [Total day charge]
               FROM customers
               ORDER BY [Total day charge] DESC
               LIMIT 10""",
            "1.4 - Top 10 customers by day charge",
        )

    def aggregation_queries(self):
        """Perform data aggregation with SUM, AVG, COUNT, and GROUP BY."""
        print("\n" + "=" * 80)
        print("2. DATA AGGREGATION QUERIES (SUM, AVG, COUNT, GROUP BY)")
        print("=" * 80)

        self.execute_query(
            "SELECT COUNT(*) as total_customers FROM customers",
            "2.1 - Total number of customers",
        )

        self.execute_query(
            """SELECT
                ROUND(AVG([Total day charge]), 2) as avg_day_charge,
                ROUND(AVG([Total eve charge]), 2) as avg_eve_charge,
                ROUND(AVG([Total night charge]), 2) as avg_night_charge
               FROM customers""",
            "2.2 - Average charges by time period",
        )

        self.execute_query(
            """SELECT State, COUNT(*) as customer_count
               FROM customers
               GROUP BY State
               ORDER BY customer_count DESC
               LIMIT 10""",
            "2.3 - Customer count by state (Top 10)",
        )

        self.execute_query(
            """SELECT
                State,
                ROUND(SUM([Total day charge]), 2) as total_revenue,
                COUNT(*) as customers
               FROM customers
               GROUP BY State
               ORDER BY total_revenue DESC
               LIMIT 10""",
            "2.4 - Total revenue by state (Top 10)",
        )

        self.execute_query(
            """SELECT
                [International plan],
                COUNT(*) as total_customers,
                ROUND(AVG([Total intl charge]), 2) as avg_intl_charge,
                ROUND(SUM([Total intl charge]), 2) as total_intl_revenue
               FROM customers
               GROUP BY [International plan]""",
            "2.5 - Analysis by International Plan",
        )

        self.execute_query(
            """SELECT
                State,
                COUNT(*) as churn_count,
                ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM customers), 2) as churn_percentage
               FROM customers
               WHERE Churn = 1
               GROUP BY State
               HAVING churn_count > 5
               ORDER BY churn_count DESC""",
            "2.6 - States with high churn (>5 customers)",
        )

    def advanced_queries(self):
        """Execute advanced SQL queries including subqueries and CASE logic."""
        print("\n" + "=" * 80)
        print("3. ADVANCED SQL QUERIES")
        print("=" * 80)

        self.execute_query(
            """SELECT
                [Customer service calls],
                COUNT(*) as customer_count,
                CASE
                    WHEN [Customer service calls] = 0 THEN 'No Calls'
                    WHEN [Customer service calls] BETWEEN 1 AND 3 THEN 'Low'
                    WHEN [Customer service calls] BETWEEN 4 AND 6 THEN 'Medium'
                    ELSE 'High'
                END as call_category
               FROM customers
               GROUP BY [Customer service calls]
               ORDER BY [Customer service calls]""",
            "3.1 - Categorize customers by service calls",
        )

        self.execute_query(
            """SELECT State, [Total day charge]
               FROM customers
               WHERE [Total day charge] > (
                   SELECT AVG([Total day charge]) FROM customers
               )
               ORDER BY [Total day charge] DESC
               LIMIT 10""",
            "3.2 - Customers with above-average charges",
        )

        self.execute_query(
            """SELECT
                Churn,
                COUNT(*) as count,
                ROUND(AVG([Account length]), 2) as avg_account_length,
                ROUND(AVG([Total day charge] + [Total eve charge] + [Total night charge]), 2) as avg_total_charge,
                ROUND(AVG([Customer service calls]), 2) as avg_service_calls
               FROM customers
               GROUP BY Churn""",
            "3.3 - Churn analysis with multiple metrics",
        )

    def business_insights(self):
        """Generate business insights and key performance indicators."""
        print("\n" + "=" * 80)
        print("4. BUSINESS INSIGHTS & KPIs")
        print("=" * 80)

        self.execute_query(
            """SELECT
                COUNT(CASE WHEN Churn = 1 THEN 1 END) as churned_customers,
                COUNT(*) as total_customers,
                ROUND(COUNT(CASE WHEN Churn = 1 THEN 1 END) * 100.0 / COUNT(*), 2) as churn_rate_percentage
               FROM customers""",
            "4.1 - Overall Churn Rate (KEY METRIC)",
        )

        self.execute_query(
            """SELECT
                ROUND(SUM([Total day charge] + [Total eve charge] + [Total night charge] + [Total intl charge]), 2) as total_revenue,
                ROUND(AVG([Total day charge] + [Total eve charge] + [Total night charge] + [Total intl charge]), 2) as avg_revenue_per_customer,
                COUNT(*) as total_customers
               FROM customers""",
            "4.2 - Revenue Analysis",
        )

        self.execute_query(
            """SELECT
                State,
                COUNT(*) as high_value_customers,
                ROUND(AVG([Total day charge] + [Total eve charge] + [Total night charge]), 2) as avg_charges
               FROM customers
               WHERE ([Total day charge] + [Total eve charge] + [Total night charge]) > 60
               GROUP BY State
               ORDER BY high_value_customers DESC
               LIMIT 10""",
            "4.3 - High-value customers by state (charges > $60)",
        )

    def run_full_analysis(self, data_path):
        """Run the complete analysis pipeline.

        Args:
            data_path: Path to the CSV dataset.
        """
        print("\n" + "=" * 80)
        print("LOADING DATA INTO DATABASE")
        print("=" * 80)

        if self.load_csv_to_db(data_path, "customers"):
            self.basic_queries()
            self.aggregation_queries()
            self.advanced_queries()
            self.business_insights()

    def close(self):
        """Close the database connection."""
        self.conn.close()
        print("\nDatabase connection closed.")


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="SQL for Business Analytics - Telecom Churn Analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python sql_analysis.py                          Run full analysis
  python sql_analysis.py --section basic          Run only basic queries
  python sql_analysis.py --section kpi            Run only KPI queries
  python sql_analysis.py --data path/to/file.csv  Use custom dataset
  python sql_analysis.py --db custom.db           Use custom database
        """,
    )
    parser.add_argument(
        "--data",
        type=str,
        default=None,
        help="Path to CSV dataset (default: datasets/Data Set For Task/Churn Prdiction Data/churn-bigml-80.csv)",
    )
    parser.add_argument(
        "--db",
        type=str,
        default="business_analytics.db",
        help="SQLite database file (default: business_analytics.db)",
    )
    parser.add_argument(
        "--section",
        choices=["basic", "aggregation", "advanced", "kpi", "all"],
        default="all",
        help="Which query section to run (default: all)",
    )
    return parser.parse_args()


def main():
    """Main entry point for the analytics pipeline."""
    args = parse_args()

    print("=" * 80)
    print("CODVEDA INTERNSHIP - TASK 2: SQL FOR BUSINESS ANALYTICS")
    print("=" * 80)
    print(f"Execution Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    project_root = Path(__file__).resolve().parent.parent
    data_path = Path(args.data) if args.data else (
        project_root / "datasets" / "Data Set For Task" / "Churn Prdiction Data" / "churn-bigml-80.csv"
    )
    db_path = Path(args.db) if os.path.isabs(args.db) else project_root / args.db

    sql_analytics = SQLBusinessAnalytics(str(db_path))

    if not data_path.exists():
        print(f"Error: Dataset not found at {data_path}")
        sql_analytics.close()
        sys.exit(1)

    sql_analytics.load_csv_to_db(str(data_path), "customers")

    sections = {
        "basic": sql_analytics.basic_queries,
        "aggregation": sql_analytics.aggregation_queries,
        "advanced": sql_analytics.advanced_queries,
        "kpi": sql_analytics.business_insights,
    }

    if args.section == "all":
        for section_fn in sections.values():
            section_fn()
    else:
        sections[args.section]()

    sql_analytics.close()

    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETED SUCCESSFULLY!")
    print("=" * 80)


if __name__ == "__main__":
    main()
