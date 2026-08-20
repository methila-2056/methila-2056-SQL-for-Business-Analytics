import sqlite3
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from SQL_Analytics.sql_analysis import SQLBusinessAnalytics


TEST_DB = "test_analytics.db"


def setup():
    """Create a test database with sample data."""
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

    conn = sqlite3.connect(TEST_DB)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE customers (
            State TEXT,
            "Account length" INTEGER,
            "Area code" INTEGER,
            "International plan" TEXT,
            "Voice mail plan" TEXT,
            "Number vmail messages" INTEGER,
            "Total day minutes" REAL,
            "Total day calls" INTEGER,
            "Total day charge" REAL,
            "Total eve minutes" REAL,
            "Total eve calls" INTEGER,
            "Total eve charge" REAL,
            "Total night minutes" REAL,
            "Total night calls" INTEGER,
            "Total night charge" REAL,
            "Total intl minutes" REAL,
            "Total intl calls" INTEGER,
            "Total intl charge" REAL,
            "Customer service calls" INTEGER,
            Churn INTEGER
        )
    """)

    sample_data = [
        ("KS", 128, 415, "No", "Yes", 25, 265.1, 110, 45.07, 197.4, 99, 16.78, 244.7, 91, 11.01, 10.0, 3, 2.70, 1, 0),
        ("OH", 107, 415, "No", "Yes", 26, 161.6, 123, 27.47, 195.5, 103, 16.62, 254.4, 103, 11.45, 13.7, 3, 3.70, 1, 0),
        ("NJ", 137, 415, "No", "No", 0, 243.4, 114, 41.38, 121.2, 110, 10.30, 162.6, 104, 7.32, 12.2, 5, 3.29, 0, 0),
        ("OH", 84, 408, "Yes", "No", 0, 299.4, 71, 50.90, 61.9, 88, 5.26, 196.9, 89, 8.86, 6.6, 7, 1.78, 2, 0),
        ("NY", 95, 415, "Yes", "No", 0, 180.2, 100, 30.63, 175.3, 105, 14.90, 203.5, 95, 9.16, 8.5, 4, 2.29, 3, 1),
    ]
    cursor.executemany("INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", sample_data)
    conn.commit()
    conn.close()


def teardown():
    """Remove the test database."""
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)


def test_database_connection():
    """Test that the database connection works."""
    analytics = SQLBusinessAnalytics(TEST_DB)
    assert analytics.conn is not None
    analytics.close()
    print("PASS: test_database_connection")


def test_load_csv():
    """Test CSV loading into database."""
    analytics = SQLBusinessAnalytics(TEST_DB)
    data_path = Path(__file__).resolve().parent.parent / "datasets" / "Data Set For Task" / "Churn Prdiction Data" / "churn-bigml-80.csv"
    result = analytics.load_csv_to_db(str(data_path), "test_table")
    assert result is True
    analytics.close()
    print("PASS: test_load_csv")


def test_execute_query():
    """Test query execution returns a DataFrame."""
    import pandas as pd
    analytics = SQLBusinessAnalytics(TEST_DB)
    df = analytics.execute_query("SELECT COUNT(*) as cnt FROM customers", "test query")
    assert df is not None
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    analytics.close()
    print("PASS: test_execute_query")


def test_customer_count():
    """Test that customer count is correct."""
    analytics = SQLBusinessAnalytics(TEST_DB)
    df = analytics.execute_query("SELECT COUNT(*) as cnt FROM customers", "count")
    assert df["cnt"].iloc[0] == 5
    analytics.close()
    print("PASS: test_customer_count")


def test_aggregation():
    """Test aggregation query returns expected columns."""
    analytics = SQLBusinessAnalytics(TEST_DB)
    df = analytics.execute_query(
        """SELECT
            ROUND(AVG([Total day charge]), 2) as avg_day_charge,
            ROUND(AVG([Total eve charge]), 2) as avg_eve_charge
        FROM customers""",
        "aggregation",
    )
    assert "avg_day_charge" in df.columns
    assert "avg_eve_charge" in df.columns
    analytics.close()
    print("PASS: test_aggregation")


def test_churn_filter():
    """Test churn filtering works."""
    analytics = SQLBusinessAnalytics(TEST_DB)
    df = analytics.execute_query(
        "SELECT COUNT(*) as cnt FROM customers WHERE Churn = 1",
        "churn filter",
    )
    assert df["cnt"].iloc[0] == 1
    analytics.close()
    print("PASS: test_churn_filter")


if __name__ == "__main__":
    setup()
    try:
        test_database_connection()
        test_execute_query()
        test_customer_count()
        test_aggregation()
        test_churn_filter()
        test_load_csv()
        print("\nAll tests passed!")
    finally:
        teardown()
