# SQL Tutorial: Sales Analysis

This project is an interactive SQL tutorial focused on sales analysis using Python, MySQL, and Streamlit. It demonstrates various SQL operations and analyses on a sample sales database.

## Project Structure

- `main.py`: Entry point for running the analysis without the Streamlit interface
- `mysql_operations.py`: Contains functions for database operations and analysis
- `streamlit_app.py`: Streamlit app for interactive exploration of the SQL tutorial
- `example.env`: Example environment file with configuration settings
- `requirements.txt`: List of Python packages required for the project

## Setup

1. Create and activate a Python virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up a MySQL database and rename the configuration file:
   - Rename `example.env` to `.env` in the root folder
   - Update the values in `.env` with your MySQL database credentials

4. Run the Streamlit app:
   ```
   cd streamlit_app
   streamlit run streamlit_app.py
   ```

## Usage

The Streamlit app provides an interactive interface to:

1. Set up the database (create tables and insert sample data)
2. Perform various analyses:
   - Basic sales analysis
   - Customer analysis
   - Time-based analysis
   - Advanced analysis (using window functions)
   - Aggregate function analysis

Navigate through different sections using the sidebar and run analyses with the provided buttons.

## Features

- Database setup and sample data insertion
- Basic to advanced SQL queries
- Interactive Streamlit interface for easy exploration
- Comprehensive sales analysis including customer behavior, time trends, and advanced metrics
- Environment variable configuration for secure database connection

## Learning Outcomes

Users will learn:
- Basic to advanced SQL query writing
- Database setup and management
- Data analysis techniques using SQL
- Integration of SQL with Python and Streamlit for interactive data exploration

Explore the app to enhance your SQL skills and understand various aspects of sales data analysis!

## Deactivating the Virtual Environment

When you're done working on the project, you can deactivate the virtual environment:
```
deactivate
```

This will return you to your global Python environment.
