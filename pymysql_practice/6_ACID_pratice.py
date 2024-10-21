import pymysql
import os
from dotenv import load_dotenv


"""
這個腳本演示了事務的基本概念和ACID特性：
原子性 (Atomicity):
transfer_money 函數中的兩個更新操作（扣款和增加金額）被包裝在一個事務中。
如果任何一步失敗，整個事務都會回滾（使用 conn.rollback()）。
一致性 (Consistency):
轉帳操作保證了總金額不變。從 Alice 扣除的金額與 Bob 增加的金額相同。
如果發生錯誤，回滾操作確保數據庫保持一致狀態。
3. 隔離性 (Isolation):
雖然這個例子沒有展示並發操作，但 PyMySQL 默認使用的隔離級別確保了基本的隔離性。
在實際應用中，可能需要根據需求調整隔離級別。
持久性 (Durability):
成功提交的事務（使用 conn.commit()）確保了數據的持久化存儲。
即使系統崩潰，提交的更改也不會丟失。
5. 錯誤處理和回滾:
使用 try-except 塊來捕獲可能的錯誤。
如果發生錯誤，使用 conn.rollback() 來撤銷事務中的所有更改。
6. 模擬錯誤:
注釋掉的 raise Exception 行可以用來模擬轉帳過程中的系統崩潰。
取消注釋這行可以測試錯誤處理和回滾機制。
這個例子展示了如何在 Python 中使用 PyMySQL 實現基本的事務處理。
"""

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

# 連接到資料庫
try:
    conn = pymysql.connect(**db_config, database=db_name)
    print('連線成功！')
    
    # 創建一個游標對象
    cursor = conn.cursor()
    
    # 創建帳戶表（如果不存在）
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        balance DECIMAL(10, 2)
    )
    """)
    
    # 插入帳戶數據，僅當帳戶不存在時
    def insert_account_if_not_exists(account_name, initial_balance):
        cursor.execute("SELECT 1 FROM accounts WHERE name = %s LIMIT 1", (account_name,))
        
        if cursor.fetchone() is None:  # 如果帳戶不存在
            cursor.execute("INSERT INTO accounts (name, balance) VALUES (%s, %s)", (account_name, initial_balance))
            conn.commit()
            print(f"帳戶 {account_name} 已插入")
        else:
            print(f"帳戶 {account_name} 已存在，無需插入")

    # 檢查並插入 Alice 和 Bob
    insert_account_if_not_exists('Alice', 1000)
    insert_account_if_not_exists('Bob', 500)


    # 定義轉帳函數
    def transfer_money(from_account, to_account, amount):
        try:
            # 開始事務
            conn.begin()

            # 步驟1：獲取 from_account 的當前餘額，並檢查是否足夠
            cursor.execute("SELECT balance FROM accounts WHERE name = %s", (from_account,))
            from_balance = cursor.fetchone()[0]

            if from_balance < amount:
                raise Exception(f"{from_account} 餘額不足，無法轉帳 {amount} 元")

            # 步驟2：從 from_account 扣款
            cursor.execute("UPDATE accounts SET balance = balance - %s WHERE name = %s", (amount, from_account))

            # 模擬可能發生的錯誤（可選）
            # if True:
            #     raise Exception("模擬錯誤：系統崩潰")

            # 步驟3：檢查 to_account 是否存在
            cursor.execute("SELECT balance FROM accounts WHERE name = %s", (to_account,))
            to_balance = cursor.fetchone()

            if to_balance is None:
                raise Exception(f"{to_account} 帳戶不存在")

            # 步驟4：給 to_account 增加金額
            cursor.execute("UPDATE accounts SET balance = balance + %s WHERE name = %s", (amount, to_account))

            # 提交事務
            conn.commit()
            print(f"成功從 {from_account} 轉帳 {amount} 元給 {to_account}")

        except Exception as e:
            # 如果發生錯誤，回滾事務
            conn.rollback()
            print(f"轉帳失敗：{str(e)}")


    # 執行轉帳操作
    transfer_money('Alice', 'Bob', 20000)

    # 檢查帳戶餘額
    cursor.execute("SELECT name, balance FROM accounts")
    for account in cursor.fetchall():
        print(f"帳戶: {account[0]}, 餘額: {account[1]}")

except Exception as e:
    print(f'操作失敗: {str(e)}')

finally:
    # 關閉游標和數據庫連接
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.open:
        conn.close()
        print('資料庫連接已關閉')
