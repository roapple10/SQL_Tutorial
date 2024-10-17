import pymysql
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection details
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'port': int(os.getenv('DB_PORT', '3306'))
}

# Database name
db_name = os.getenv('DB_NAME')

# Connect without specifying a database
try:
    conn = pymysql.connect(**db_config)
    print('連線成功！')
    
    with conn.cursor() as cursor:
        # Create the database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"資料庫 '{db_name}' 已創建或已存在")
        
        # Switch to the database
        conn.select_db(db_name)
        
        # Create EMPLOYEE table
        cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
        sql = """CREATE TABLE EMPLOYEE (
                 FIRST_NAME CHAR(20) NOT NULL,
                 LAST_NAME CHAR(20),
                 AGE INT,  
                 SEX CHAR(1),
                 INCOME FLOAT )"""
        cursor.execute(sql)
        print('建表成功！')
    
    conn.commit()
except Exception as e:
    print(f'操作失敗: {str(e)}')
finally:
    if 'conn' in locals() and conn.open:
        conn.close()
        print('資料庫連接已關閉')

'''
連結成功！
建表成功！
'''
