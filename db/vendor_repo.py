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
   cursor.execute("SELECT COUNT(*) FROM VENDOR_LIST WHERE VENDOR_NAME=%s",(user_input,))
   result = cursor.fetchone() 
   cursor.close()
   conn.close()
   return result[0]
def add(user_input,user_address):
   conn=connect()
   cursor=conn.cursor()
   cursor.execute("INSERT INTO VENDOR_LIST(VENDOR_NAME,VENDOR_ADDRESS) VALUES (%s,%s)",(user_input,user_address))
   conn.commit()
   cursor.close()
   conn.close()   
   
def fetch():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM VENDOR_LIST")
    rows = cursor.fetchall()
    cursor.close() 
    conn.close() 
    return rows
def update(new_name,new_address,vendor_id):

    conn =connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE VENDOR_LIST SET VENDOR_NAME=%s,VENDOR_ADDRESS=%s WHERE VENDOR_ID=%s",
                    (new_name,new_address,vendor_id))
    conn.commit()
    cursor.close()
    conn.close() 
def delete(vendor_id):
    conn =connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM VENDOR_LIST WHERE VENDOR_ID=%s", (vendor_id,))
    conn.commit()
    cursor.close()
    conn.close()

