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
        # SQL 更新語句
        sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = %s"
        
        # 執行SQL語句
        cursor.execute(sql, ('M',))
        
        # 提交到資料庫執行
        conn.commit()
        print(f'成功更新 {cursor.rowcount} 筆資料！')

except Exception as e:
    # 如果發生錯誤則回滾
    if 'conn' in locals() and conn.open:
        conn.rollback()
    print(f'資料更新錯誤：{str(e)}')

finally:
    # 關閉資料庫連接
    if 'conn' in locals() and conn.open:
        conn.close()
        print('資料庫連接已關閉')
