import mysql.connector
import main
import config

def check(user_input):
   conn=config.db_connector()
   cursor=conn.cursor()
   cursor.execute("SELECT COUNT(*) FROM CATEGORY_LIST WHERE CATEGORY_NAME=%s",(user_input,))
   result = cursor.fetchone() 
   cursor.close()
   conn.close()
   return result[0]

def add(user_input):
   conn=config.db_connector()
   cursor=conn.cursor()
   cursor.execute("INSERT INTO CATEGORY_LIST(CATEGORY_NAME) VALUES (%s)",(user_input,))
   conn.commit()
   cursor.close()
   conn.close()
def fetch():
    conn = config.db_connector()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            c.CATEGORY_ID,
            c.CATEGORY_NAME,
            COALESCE(
                SUM(
                    (i.NUM_OF_UNITS - i.NUM_OF_UNITS_WITHDRAWN)*
                    i.UNIT_WT*
                    i.RATE
                ),
                0)
                AS TOTAL_WORTH
        FROM CATEGORY_LIST c
        LEFT JOIN CURRENT_INVENTORY i
            ON c.CATEGORY_ID=i.CATEGORY_ID
        GROUP BY
            c.CATEGORY_ID,
            c.CATEGORY_NAME
        ORDER BY
            c.CATEGORY_NAME
    """)
    rows = cursor.fetchall() 
    cursor.close()
    conn.close() 
    return rows

def update(new_name,category_id):

    conn =config.db_connector()
    cursor = conn.cursor()
    cursor.execute("UPDATE CATEGORY_LIST SET CATEGORY_NAME=%s WHERE CATEGORY_ID=%s",
                    (new_name, category_id))
    conn.commit()
    cursor.close()
    conn.close() 
def delete(category_id):
    conn =config.db_connector()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM CATEGORY_LIST WHERE CATEGORY_ID=%s", (category_id,))
    conn.commit()
    cursor.close()
    conn.close()
