import pymysql
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# 開啟資料庫連接
try:
    db = pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        port=int(os.getenv('DB_PORT', '3306'))  # Default to 3306 if DB_PORT is not set
    )
    print('連線成功！')
except Exception as e:
    print(f'連線失敗: {str(e)}')

# 使用cursor() 方法建立一個遊標物件cursor
cursor = db.cursor()

# 使用execute() 方法執行SQL 查詢
cursor.execute("SELECT VERSION()")

# 使用fetchone() 方法取得單一資料.
data = cursor.fetchone()

print("Database version : %s " % data)

# 關閉資料庫連接
db.close()

'''
連結成功！
Database version : 8.0.25
'''
