import mysql.connector
import main
def connect():
   return mysql.connector.connect(
        host="localhost",
        user="root",
        password="HelloWorld",
        database="ACCOUNTING_RECORDS"
    )

def fetch_history():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            h.HISTORY_ID,
            h.INVOICE_NUMBER,
            cl.CATEGORY_NAME,
            h.GRADE,
            h.GARDEN_NAME,
            vl.VENDOR_NAME,
            h.NUM_OF_UNITS,
            h.UNIT_WT,
            h.RATE,
            h.OPERATION_TYPE,
            h.TRANSACTION_DATE
        FROM HISTORY h
        JOIN CATEGORY_LIST cl ON h.CATEGORY_ID = cl.CATEGORY_ID
        JOIN VENDOR_LIST vl ON h.VENDOR_ID = vl.VENDOR_ID
        ORDER BY h.HISTORY_ID DESC
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
