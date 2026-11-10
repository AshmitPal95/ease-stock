import mysql.connector
import main
import config

def check(user_input):
   conn=config.db_connector()
   cursor=conn.cursor()
   cursor.execute("SELECT COUNT(*) FROM GODOWN_LIST WHERE GODOWN_NAME=%s",(user_input,))
   result = cursor.fetchone() 
   cursor.close()
   conn.close()
   return result[0]

def add(user_input):
   conn=config.db_connector()
   cursor=conn.cursor()
   cursor.execute("INSERT INTO GODOWN_LIST(GODOWN_NAME) VALUES (%s)",(user_input,))
   conn.commit()
   cursor.close()
   conn.close()
def fetch():
    conn = config.db_connector()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            g.GODOWN_ID,
            g.GODOWN_NAME,
            COALESCE(
                SUM(
                    (i.NUM_OF_UNITS - i.NUM_OF_UNITS_WITHDRAWN)*
                    i.UNIT_WT*
                    i.RATE
                ),
                0)
                AS TOTAL_WORTH
        FROM GODOWN_LIST g
        LEFT JOIN CURRENT_INVENTORY i
            ON g.GODOWN_ID=i.GODOWN_ID
        GROUP BY
            g.GODOWN_ID,
            g.GODOWN_NAME
        ORDER BY
            g.GODOWN_NAME
    """)
    rows = cursor.fetchall() 
    cursor.close()
    conn.close() 
    return rows

def update(new_name,godown_id):

    conn =config.db_connector()
    cursor = conn.cursor()
    cursor.execute("UPDATE GODOWN_LIST SET GODOWN_NAME=%s WHERE GODOWN_ID=%s",
                    (new_name, godown_id))
    conn.commit()
    cursor.close()
    conn.close() 
def delete(godown_id):
    conn =config.db_connector()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM GODOWN_LIST WHERE GODOWN_ID=%s", (godown_id,))
    conn.commit()
    cursor.close()
    conn.close()
