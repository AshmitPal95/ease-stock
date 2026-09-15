import mysql.connector
import main
def connect():
   return mysql.connector.connect(
        host="localhost",
        user="root",
        password="HelloWorld",
        database="ACCOUNTING_RECORDS"
    )

def check(user_input):
   conn=connect()
   cursor=conn.cursor()
   cursor.execute("SELECT COUNT(*) FROM CATEGORY_LIST WHERE CATEGORY_NAME=%s",(user_input,))
   result = cursor.fetchone() 
   cursor.close()
   conn.close()
   return result[0]

def add(user_input):
   conn=connect()
   cursor=conn.cursor()
   cursor.execute("INSERT INTO CATEGORY_LIST(CATEGORY_NAME) VALUES (%s)",(user_input,))
   conn.commit()
   cursor.close()
   conn.close()
def fetch():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CATEGORY_LIST")
    rows = cursor.fetchall() 
    cursor.close()
    conn.close() 
    return rows
def update(new_name,category_id):

    conn =connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE CATEGORY_LIST SET CATEGORY_NAME=%s WHERE CATEGORY_ID=%s",
                    (new_name, category_id))
    conn.commit()
    cursor.close()
    conn.close() 
def delete(category_id):
    conn =connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM CATEGORY_LIST WHERE CATEGORY_ID=%s", (category_id,))
    conn.commit()
    cursor.close()
    conn.close()
