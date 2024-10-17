from mysql_operations import (
    connect_to_database,
    create_tables,
    insert_sample_data,
    basic_sales_analysis,
    customer_analysis,
    time_based_analysis,
    advanced_analysis,
    aggregate_function_analysis
)
from pymysql import OperationalError

def main():
    """
    Main function to execute the sales analysis program.
    """
    conn = connect_to_database()
    if conn is None:
        return

    try:
        # Create tables and insert sample data
        create_tables(conn)
        insert_sample_data(conn)

        # Run various sales analysis operations
        print("Basic Sales Analysis:", basic_sales_analysis(conn))
        print("Customer Analysis:", customer_analysis(conn))
        print("Time-based Analysis:", time_based_analysis(conn))
        print("Advanced Analysis:", advanced_analysis(conn))
        print("Aggregate Function Analysis:", aggregate_function_analysis(conn))

    except OperationalError as e:
        print(f"Error: {e}")
    finally:
        conn.close()
        print("MySQL connection is closed")

if __name__ == '__main__':
    main()
