import mysql.connector
import main
import config

def fetch_history():
    conn = config.db_connector()
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

def fetch_history_date(start_date,end_date):
    conn = config.db_connector()
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
        WHERE h.TRANSACTION_DATE BETWEEN %s AND %s
        ORDER BY h.HISTORY_ID DESC
    """, (start_date, end_date))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows