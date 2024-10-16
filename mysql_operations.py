#!/usr/bin/env python

import mysql.connector
from mysql.connector import Error

# Database connection details
DB_CONFIG = {
    'host': 'localhost',
    'user': 'salesuser',
    'password': 'salespass',
    'database': 'sales_db'
}

def connect_to_database():
    """
    Establish a connection to the MySQL database.
    """
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            print("Successfully connected to MySQL database")
        return conn
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

def create_tables(conn):
    """
    Create sample tables for our sales analysis tutorial.
    """
    cursor = conn.cursor()
    
    # Create 'customers' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        city VARCHAR(50)
    )
    """)
    
    # Create 'stores' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stores (
        store_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        city VARCHAR(50)
    )
    """)
    
    # Create 'sales' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        sale_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id INT,
        store_id INT,
        date DATE,
        amount DECIMAL(10, 2),
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
        FOREIGN KEY (store_id) REFERENCES stores(store_id)
    )
    """)
    
    print("Tables created successfully")

def insert_sample_data(conn):
    """
    Insert sample data into our tables.
    """
    cursor = conn.cursor()
    
    # Insert data into 'customers'
    customers_data = [
        ("John Doe", "john@example.com", "New York"),
        ("Jane Smith", "jane@example.com", "Los Angeles"),
        ("Mike Johnson", "mike@example.com", "Chicago"),
        ("Emily Brown", "emily@example.com", "Houston"),
        ("David Lee", "david@example.com", "New York")
    ]
    cursor.executemany("INSERT INTO customers (name, email, city) VALUES (%s, %s, %s)", customers_data)
    
    # Insert data into 'stores'
    stores_data = [
        ("Downtown Store", "New York"),
        ("Westside Shop", "Los Angeles"),
        ("Central Market", "Chicago"),
        ("Harbor Point", "Houston")
    ]
    cursor.executemany("INSERT INTO stores (name, city) VALUES (%s, %s)", stores_data)
    
    # Insert data into 'sales'
    sales_data = [
        (1, 1, "2023-01-15", 150.00),
        (2, 2, "2023-01-16", 200.50),
        (3, 3, "2023-01-17", 75.25),
        (4, 4, "2023-01-18", 300.00),
        (5, 1, "2023-01-19", 125.75),
        (1, 1, "2023-01-20", 200.00),
        (2, 2, "2023-01-21", 150.50),
        (3, 3, "2023-01-22", 100.25),
        (4, 4, "2023-01-23", 250.00),
        (5, 1, "2023-01-24", 175.75)
    ]
    cursor.executemany("INSERT INTO sales (customer_id, store_id, date, amount) VALUES (%s, %s, %s, %s)", sales_data)
    
    conn.commit()
    print("Sample data inserted successfully")

def basic_sales_analysis(conn):
    cursor = conn.cursor()
    results = []
    
    cursor.execute("SELECT SUM(amount) as total_sales FROM sales")
    results.append(("Total Sales", cursor.fetchone()))

    cursor.execute("""
    SELECT s.name, SUM(sa.amount) as total_sales
    FROM stores s
    JOIN sales sa ON s.store_id = sa.store_id
    GROUP BY s.store_id
    ORDER BY total_sales DESC
    """)
    results.append(("Sales by Store", cursor.fetchall()))

    cursor.close()
    return results

def customer_analysis(conn):
    cursor = conn.cursor()
    results = []

    cursor.execute("""
    SELECT c.name, SUM(s.amount) as total_spent
    FROM customers c
    JOIN sales s ON c.customer_id = s.customer_id
    GROUP BY c.customer_id
    ORDER BY total_spent DESC
    LIMIT 3
    """)
    results.append(("Top 3 Customers by Sales", cursor.fetchall()))

    cursor.execute("""
    SELECT c.city, AVG(s.amount) as avg_sale
    FROM customers c
    JOIN sales s ON c.customer_id = s.customer_id
    GROUP BY c.city
    ORDER BY avg_sale DESC
    """)
    results.append(("Average Sale Amount by City", cursor.fetchall()))

    cursor.close()
    return results

def time_based_analysis(conn):
    cursor = conn.cursor()
    results = []

    cursor.execute("""
    SELECT date, SUM(amount) as daily_sales
    FROM sales
    GROUP BY date
    ORDER BY date
    """)
    results.append(("Daily Sales Trend", cursor.fetchall()))

    cursor.execute("""
    SELECT 
        YEAR(date) as year,
        MONTH(date) as month,
        SUM(amount) as monthly_sales
    FROM sales
    GROUP BY YEAR(date), MONTH(date)
    ORDER BY year, month
    """)
    results.append(("Monthly Sales Comparison", cursor.fetchall()))

    cursor.close()
    return results

def advanced_analysis(conn):
    cursor = conn.cursor()
    results = []

    # ... (keep all existing queries)

    cursor.execute("""
    SELECT 
        c.name,
        SUM(s.amount) as total_sales,
        PERCENT_RANK() OVER (ORDER BY SUM(s.amount)) as percentile
    FROM customers c
    JOIN sales s ON c.customer_id = s.customer_id
    GROUP BY c.customer_id
    ORDER BY total_sales DESC
    """)
    results.append(("Sales Percentile", cursor.fetchall()))

    cursor.close()
    return results

def aggregate_function_analysis(conn):
    cursor = conn.cursor()
    results = []

    # ... (keep all existing queries)

    cursor.execute("""
    SELECT 
        customer_id,
        SUM(amount) as total_spent,
        SUM(amount) / COUNT(*) as avg_transaction,
        GROUP_CONCAT(DISTINCT store_id ORDER BY store_id) as visited_stores
    FROM sales
    GROUP BY customer_id
    ORDER BY total_spent DESC
    LIMIT 5
    """)
    results.append(("Advanced Aggregate Functions", cursor.fetchall()))

    cursor.close()
    return results
