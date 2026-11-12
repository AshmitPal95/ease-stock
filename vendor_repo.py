import mysql.connector
import main
import config

def check(user_input):
   conn=config.db_connector()
   cursor=conn.cursor()
   cursor.execute("SELECT COUNT(*) FROM VENDOR_LIST WHERE VENDOR_NAME=%s",(user_input,))
   result = cursor.fetchone() 
   cursor.close()
   conn.close()
   return result[0]

def add(user_input,user_address):
   conn=config.db_connector()
   cursor=conn.cursor()
   cursor.execute("INSERT INTO VENDOR_LIST(VENDOR_NAME,VENDOR_ADDRESS) VALUES (%s,%s)",(user_input,user_address))
   conn.commit()
   cursor.close()
   conn.close()   
   
def fetch():
    conn = config.db_connector()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            v.VENDOR_ID,
            v.VENDOR_NAME,
            v.VENDOR_ADDRESS,
            COALESCE(
            SUM(
            (c.NUM_OF_UNITS-c.NUM_OF_UNITS_WITHDRAWN)*
            c.UNIT_WT*
            c.RATE),0
            ) AS TOTAL_WORTH
        FROM VENDOR_LIST v
        LEFT JOIN CURRENT_INVENTORY c
            ON v.VENDOR_ID = c.VENDOR_ID
        GROUP BY
            v.VENDOR_ID,
            v.VENDOR_NAME,
            v.VENDOR_ADDRESS
        ORDER BY
            v.VENDOR_NAME
    """)
    rows = cursor.fetchall()
    cursor.close() 
    conn.close() 
    return rows
def update(new_name,new_address,vendor_id):

    conn =config.db_connector()
    cursor = conn.cursor()
    cursor.execute("UPDATE VENDOR_LIST SET VENDOR_NAME=%s,VENDOR_ADDRESS=%s WHERE VENDOR_ID=%s",
                    (new_name,new_address,vendor_id))
    conn.commit()
    cursor.close()
    conn.close() 
def delete(vendor_id):
    conn =config.db_connector()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM VENDOR_LIST WHERE VENDOR_ID=%s", (vendor_id,))
    conn.commit()
    cursor.close()
    conn.close()

