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
from mysql.connector import Error

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
        basic_sales_analysis(conn)
        customer_analysis(conn)
        time_based_analysis(conn)
        advanced_analysis(conn)
        aggregate_function_analysis(conn)

    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            conn.close()
            print("MySQL connection is closed")

if __name__ == '__main__':
    main()