import mysql.connector
import config

def fetch_start_date():
    conn=config.db_connector()
    cursor=conn.cursor()
    cursor.execute("SELECT DATE FROM DATES WHERE TYPE=%s",("START",))
    start_date=cursor.fetchone()
    cursor.close()
    conn.close()
    if start_date:
        return start_date[0]
    return None
    

def fetch_end_date():
    conn=config.db_connector()
    cursor=conn.cursor()
    cursor.execute("SELECT DATE FROM DATES WHERE TYPE=%s",("END",))
    end_date=cursor.fetchone()
    cursor.close()
    conn.close()
    if end_date:
        return end_date[0]
    return None
    

def change_start_date(start_date):
    conn=config.db_connector()
    cursor=conn.cursor()
    cursor.execute("UPDATE DATES SET DATE=%s WHERE TYPE=%s",(start_date,"START"))
    conn.commit()
    cursor.close()
    conn.close()


def change_end_date(end_date):
    conn=config.db_connector()
    cursor=conn.cursor()
    cursor.execute("UPDATE DATES SET DATE=%s WHERE TYPE=%s",(end_date,"END"))
    conn.commit()
    cursor.close()
    conn.close()





    