import mysql.connector
import datetime
import main

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="HelloWorld",
        database="ACCOUNTING_RECORDS"
    )

def check(invoice_num):
   conn=connect()
   cursor=conn.cursor()
   cursor.execute("SELECT COUNT(*) FROM CURRENT_INVENTORY WHERE INVOICE_NUMBER=%s",(invoice_num,))
   result = cursor.fetchone() 
   cursor.close()
   conn.close()
   return result[0]

def add(invoice_num, category_id, grade, garden_name, vendor_id, num_of_units, unit_wt, rate):
    conn = connect()
    cursor = conn.cursor()
    current_date = datetime.date.today()

    # Insert into CURRENT_INVENTORY
    cursor.execute("""
        INSERT INTO CURRENT_INVENTORY ( INVOICE_NUMBER, CATEGORY_ID,
            GRADE, GARDEN_NAME, VENDOR_ID, NUM_OF_UNITS,
            NUM_OF_UNITS_WITHDRAWN, UNIT_WT, RATE )
        VALUES (%s, %s, %s, %s, %s, %s,0, %s, %s)
    """, (
        invoice_num, category_id, grade, garden_name,
        vendor_id, num_of_units, unit_wt, rate ))

    # Insert into HISTORY
    cursor.execute("""
        INSERT INTO HISTORY (
            INVOICE_NUMBER,
            CATEGORY_ID,
            GRADE,
            GARDEN_NAME,
            VENDOR_ID,
            NUM_OF_UNITS,
            UNIT_WT,
            RATE,
            TRANSACTION_DATE,
            OPERATION_TYPE
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, 'Entry')
    """, (
        invoice_num,
        category_id,
        grade,
        garden_name,
        vendor_id,
        num_of_units,
        unit_wt,
        rate,
        current_date
    ))

    conn.commit()
    cursor.close()
    conn.close()



def fetch():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""SELECT 
            ci.ENTRY_ID,
            ci.INVOICE_NUMBER,
            cl.CATEGORY_NAME,
            ci.GRADE,
            ci.GARDEN_NAME,
            vl.VENDOR_NAME,
            ci.NUM_OF_UNITS,
            ci.UNIT_WT,
            ci.RATE,
            (ci.NUM_OF_UNITS * ci.UNIT_WT * ci.RATE) AS WORTH
        FROM CURRENT_INVENTORY ci
        JOIN CATEGORY_LIST cl ON ci.CATEGORY_ID = cl.CATEGORY_ID
        JOIN VENDOR_LIST vl ON ci.VENDOR_ID = vl.VENDOR_ID
          """)
    rows = cursor.fetchall() 
    cursor.close()
    conn.close() 
    return rows


def update(invoice_num, category_id, grade, garden_name, vendor_id, num_of_units, unit_wt, rate, entry_id):
    conn = connect()
    cursor = conn.cursor()
    current_date = datetime.date.today()

    # Update CURRENT_INVENTORY
    cursor.execute("""
        UPDATE CURRENT_INVENTORY 
        SET INVOICE_NUMBER=%s,
            CATEGORY_ID=%s,
            GRADE=%s,
            GARDEN_NAME=%s,
            VENDOR_ID=%s,
            NUM_OF_UNITS=%s,
            UNIT_WT=%s,
            RATE=%s
        WHERE ENTRY_ID=%s
    """, (
        invoice_num,
        category_id,
        grade,
        garden_name,
        vendor_id,
        num_of_units,
        unit_wt,
        rate,
        entry_id
    ))

    # Log update into HISTORY
    cursor.execute("""
        INSERT INTO HISTORY (
            INVOICE_NUMBER,
            CATEGORY_ID,
            GRADE,
            GARDEN_NAME,
            VENDOR_ID,
            NUM_OF_UNITS,
            UNIT_WT,
            RATE,
            TRANSACTION_DATE,
            OPERATION_TYPE
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, 'Update')
    """, (
        invoice_num,
        category_id,
        grade,
        garden_name,
        vendor_id,
        num_of_units,
        unit_wt,
        rate,
        current_date
    ))

    conn.commit()
    cursor.close()
    conn.close()

def withdraw(num_of_units, entry_id):

    conn = connect()
    cursor = conn.cursor()

    # Fetch current units
    cursor.execute("SELECT NUM_OF_UNITS FROM CURRENT_INVENTORY WHERE ENTRY_ID=%s", (entry_id,))
    current_units = cursor.fetchone()[0]

    # Calculate new balance
    new_num_of_units = int(current_units) - int(num_of_units)

    # Update table
    cursor.execute(
        "UPDATE CURRENT_INVENTORY SET NUM_OF_UNITS=%s WHERE ENTRY_ID=%s",
        (new_num_of_units, entry_id)
    )

    conn.commit()
    cursor.close()
    conn.close()


def delete(entry_id):
    conn =connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM CURRENT_INVENTORY WHERE ENTRY_ID=%s", (entry_id,))
    conn.commit()
    cursor.close()
    conn.close()


    