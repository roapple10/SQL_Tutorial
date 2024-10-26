# SQL Tutorial

This project demonstrates how to interact with an MS SQL Database using Python and Jupyter Notebooks.

## Project Structure

The project consists of three main Jupyter notebooks:

1. `1-connect-sql.ipynb`: Demonstrates how to connect to an MS SQL Database.
2. `2-insert-data-sql.ipynb`: Shows how to insert data into the database.
3. `3-manipulate-data-sql.ipynb`: Illustrates various data manipulation operations.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/roapple10/SQL_Tutorial.git
   cd MS_SQL_Tutorial
   ```

2. Create and activate a Python virtual environment:
   ```
   python -m venv venv
   
   # On Windows:
   Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
   venv\Scripts\activate
   
   # On Unix or MacOS:
   source venv/bin/activate
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Open the Jupyter notebooks in order and follow the instructions within each notebook to learn how to:

1. Connect to an Azure SQL Database
2. Insert data into tables
3. Perform various data manipulation operations like updating, deleting, and querying data

Make sure to update the connection details in the notebooks with your own Azure SQL Database credentials before running the code.

## Requirements

- Python 3.8+
- Jupyter Notebook
- pyodbc
- pandas

See `requirements.txt` for a full list of dependencies.
