import sqlite3
from sqlite3 import Error

def __create_connection(db_file):
    """
    建立資料庫和連線至資料庫
    :param db_file: 資料庫的檔案名稱
    :return: Connection物件
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


def __select_continent(conn):
    """
    選取world資料表
    :param conn:Connection物件
    :return:list
    """
    cursor = conn.cursor()
    sql = '''
    SELECT DISTINCT 洲名
    FROM world
    WHERE 洲名 IS NOT NULL
    '''
    cursor.execute(sql)
    rows = cursor.fetchall()
    continents = [row for row in rows if row is not None]
    return continents

def __selected_country_by_continent(conn, continent):
    cursor = conn.cursor()
    sql = '''
        SELECT DISTINCT 國家
        FROM world
        WHERE 洲名 = ?
        '''
    cursor.execute(sql,(continent,))
    rows = cursor.fetchall()
    selected_country = [row[0] for row in rows]
    return selected_country

def __selected_country_detail(conn,country_name):
    cursor = conn.cursor()
    sql = '''
    SELECT 國家,日期,總確診數,新增確診數,總死亡數,新增死亡數
    FROM world
    WHERE 國家 = ?
    ORDER BY 日期 DESC
    '''
    cursor.execute(sql, (country_name,))
    rows = cursor.fetchall()
    country_details = [row for row in rows]
    return country_details

def get_continent():
    database = "world.db"
    #建立資料庫和Connection物件
    conn = __create_connection(database)
    with conn:
        continents = __select_continent(conn)
        return continents
    return []

def get_country_by_continent(continent):
    database = "world.db"
    # 建立資料庫和Connection物件
    conn = __create_connection(database)
    with conn:
        countries = __selected_country_by_continent(conn,continent)
        return countries
    return []

def get_country_detailData(country):
    database = "world.db"
    # 建立資料庫和Connection物件
    conn = __create_connection(database)
    with conn:
        country_details =  __selected_country_detail(conn, country)
        return country_details
    return []