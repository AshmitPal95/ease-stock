import mysql.connector
import main_ui as userinterface
import config
def main_function():
    
    create_db()
    userinterface.main()


def create_db():
    print("creating DB tables")
    conn=config.db_connector()
    cursor = conn.cursor()
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS ACCOUNTING_RECORDS")
    cursor.execute("USE ACCOUNTING_RECORDS")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CATEGORY_LIST (
            CATEGORY_ID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
            CATEGORY_NAME VARCHAR(50) NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS VENDOR_LIST (
            VENDOR_ID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            VENDOR_NAME VARCHAR(50) NOT NULL,
            VENDOR_ADDRESS VARCHAR(255) NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CURRENT_INVENTORY (
            ENTRY_ID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
            INVOICE_NUMBER INT NOT NULL,
            CATEGORY_ID INT UNSIGNED NOT NULL,
            GRADE VARCHAR(50) NOT NULL,
            GARDEN_NAME VARCHAR(50) NOT NULL,
            VENDOR_ID INT UNSIGNED NOT NULL,
            NUM_OF_UNITS INT NOT NULL,
            NUM_OF_UNITS_WITHDRAWN INT NOT NULL,
            UNIT_WT FLOAT NOT NULL,
            RATE FLOAT NOT NULL,
            FOREIGN KEY (CATEGORY_ID) REFERENCES CATEGORY_LIST(CATEGORY_ID),
            FOREIGN KEY (VENDOR_ID) REFERENCES VENDOR_LIST(VENDOR_ID)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS HISTORY (
            HISTORY_ID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            INVOICE_NUMBER INT UNSIGNED NOT NULL,
            CATEGORY_ID INT UNSIGNED NOT NULL,
            GRADE VARCHAR(50),
            GARDEN_NAME VARCHAR(50),
            VENDOR_ID INT UNSIGNED NOT NULL,
            NUM_OF_UNITS INT UNSIGNED NOT NULL,
            UNIT_WT FLOAT NOT NULL,
            RATE FLOAT NOT NULL,
            OPERATION_TYPE VARCHAR(20) NOT NULL,
            TRANSACTION_DATE DATE NOT NULL,
            FOREIGN KEY (CATEGORY_ID) REFERENCES CATEGORY_LIST(CATEGORY_ID),
            FOREIGN KEY (VENDOR_ID) REFERENCES VENDOR_LIST(VENDOR_ID)
        )
    """)


    conn.commit()
    cursor.close()
    conn.close()



