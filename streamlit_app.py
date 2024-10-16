import streamlit as st
import mysql.connector
import pandas as pd
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

# Set page configuration
st.set_page_config(page_title="SQL Tutorial: Sales Analysis", page_icon="📊", layout="wide")

# Custom CSS to improve the look
st.markdown("""
    <style>
    .main {
        background-color: #f0f5ff;
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stDataFrame {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #1e3799;
        font-size: 3rem;
        text-align: center;
        padding: 1rem;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    h2 {
        color: #3c6382;
        border-bottom: 2px solid #3c6382;
        padding-bottom: 10px;
    }
    .stAlert {
        background-color: #e3f2fd;
        color: #1565c0;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #1565c0;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("📊 SQL Tutorial: Sales Analysis")

    # Establish database connection
    conn = connect_to_database()
    if conn is None:
        st.error("Failed to connect to the database. Please check your connection settings.")
        return

    # Sidebar for navigation
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/000000/sql.png", width=100)
        page = st.radio(
            "Choose a section",
            ["Introduction", "Setup Database", "Basic Analysis", "Customer Analysis", 
             "Time-based Analysis", "Advanced Analysis", "Aggregate Functions"]
        )

    if page == "Introduction":
        st.header("🎓 Welcome to the SQL Tutorial")
        st.write("This interactive app will guide you through various SQL operations and analyses on a sample sales database.")
        st.info("Use the sidebar to navigate through different sections of the tutorial.")

    elif page == "Setup Database":
        st.header("🛠️ Setting up the Database")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Create Tables"):
                create_tables(conn)
                st.success("Tables created successfully!")
        with col2:
            if st.button("Insert Sample Data"):
                insert_sample_data(conn)
                st.success("Sample data inserted successfully!")

    elif page == "Basic Analysis":
        st.header("📈 Basic Sales Analysis")
        if st.button("Run Basic Analysis"):
            results = basic_sales_analysis(conn)
            for title, data in results:
                st.subheader(title)
                df = pd.DataFrame(data)
                st.dataframe(df)
        st.info("This section demonstrates simple SQL queries for basic sales analysis.")

    elif page == "Customer Analysis":
        st.header("👥 Customer Analysis")
        if st.button("Run Customer Analysis"):
            results = customer_analysis(conn)
            for title, data in results:
                st.subheader(title)
                df = pd.DataFrame(data)
                st.dataframe(df)
        st.info("Here we focus on customer-centric analyses using more complex SQL queries.")

    elif page == "Time-based Analysis":
        st.header("⏳ Time-based Analysis")
        if st.button("Run Time-based Analysis"):
            results = time_based_analysis(conn)
            for title, data in results:
                st.subheader(title)
                df = pd.DataFrame(data)
                st.line_chart(df.set_index(df.columns[0]))
        st.info("This section shows how to perform time-based analyses on sales data.")

    elif page == "Advanced Analysis":
        st.header("🚀 Advanced Analysis")
        if st.button("Run Advanced Analysis"):
            results = advanced_analysis(conn)
            for title, data in results:
                st.subheader(title)
                df = pd.DataFrame(data)
                st.dataframe(df)
        st.info("Here we demonstrate advanced SQL techniques like window functions and CTEs.")

    elif page == "Aggregate Functions":
        st.header("🧮 Aggregate Function Analysis")
        if st.button("Run Aggregate Function Analysis"):
            results = aggregate_function_analysis(conn)
            for title, data in results:
                st.subheader(title)
                df = pd.DataFrame(data)
                st.dataframe(df)
        st.info("This section covers various aggregate functions and their applications in SQL.")

    # Close the database connection when the app is done
    if conn.is_connected():
        conn.close()

if __name__ == "__main__":
    main()