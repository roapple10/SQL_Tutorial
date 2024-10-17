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

# Connect to the database
try:
    conn = pymysql.connect(**db_config, database=db_name)
    print('連線成功！')
    
    with conn.cursor() as cursor:
        # 多筆資料
        employees = [
            ('Mac', 'Mohan', 20, 'M', 2000),
            ('Lisa', 'Chen', 25, 'F', 2500),
            ('John', 'Smith', 30, 'M', 3000),
            ('Emma', 'Watson', 28, 'F', 3500),
            ('Michael', 'Johnson', 35, 'M', 4000),
            ('Sophia', 'Lee', 22, 'F', 2200)
        ]
        
        inserted_count = 0
        for employee in employees:
            # 檢查是否已存在相同的 FIRST_NAME 和 LAST_NAME
            check_sql = "SELECT COUNT(*) FROM EMPLOYEE WHERE FIRST_NAME = %s AND LAST_NAME = %s"
            cursor.execute(check_sql, (employee[0], employee[1]))
            if cursor.fetchone()[0] == 0:
                # 如果不存在，則插入新記錄
                insert_sql = """INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
                                VALUES (%s, %s, %s, %s, %s)"""
                cursor.execute(insert_sql, employee)
                inserted_count += 1
        
        # 提交到資料庫執行
        conn.commit()
        print(f'成功插入 {inserted_count} 筆新資料！')

except Exception as e:
    # 如果發生錯誤則回滾
    if 'conn' in locals() and conn.open:
        conn.rollback()
    print(f'資料插入錯誤：{str(e)}')

finally:
    # 關閉資料庫連接
    if 'conn' in locals() and conn.open:
        conn.close()
        print('資料庫連接已關閉')
