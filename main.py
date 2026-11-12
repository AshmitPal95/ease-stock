import mysql.connector
import user_password_box
import config
import auto_log
import password_cryptography
def main_function():
    
    create_db()
    auto_log.main()
    user_password_box.main()


def create_db():
    print("creating DB tables")
    conn=config.db_connector_root()
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
            CREATE TABLE IF NOT EXISTS GODOWN_LIST(
            GODOWN_ID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
            GODOWN_NAME VARCHAR(50) NOT NULL
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
            GODOWN_ID INT UNSIGNED NOT NULL,
            NUM_OF_UNITS INT NOT NULL,
            NUM_OF_UNITS_WITHDRAWN INT NOT NULL,
            UNIT_WT FLOAT NOT NULL,
            RATE FLOAT NOT NULL,
            FOREIGN KEY (CATEGORY_ID) REFERENCES CATEGORY_LIST(CATEGORY_ID),
            FOREIGN KEY (VENDOR_ID) REFERENCES VENDOR_LIST(VENDOR_ID),
            FOREIGN KEY(GODOWN_ID) REFERENCES GODOWN_LIST(GODOWN_ID)
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
            GODOWN_ID INT UNSIGNED NOT NULL,
            NUM_OF_UNITS INT UNSIGNED NOT NULL,
            UNIT_WT FLOAT NOT NULL,
            RATE FLOAT NOT NULL,
            OPERATION_TYPE VARCHAR(20) NOT NULL,
            TRANSACTION_DATE DATE NOT NULL,
            FOREIGN KEY (CATEGORY_ID) REFERENCES CATEGORY_LIST(CATEGORY_ID),
            FOREIGN KEY (VENDOR_ID) REFERENCES VENDOR_LIST(VENDOR_ID),
            FOREIGN KEY(GODOWN_ID) REFERENCES GODOWN_LIST(GODOWN_ID)
        )
    """)

    

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS DATES (
        TYPE VARCHAR(10) PRIMARY KEY NOT NULL,
        DATE DATE
        )
    """)
    cursor.execute("""
        INSERT IGNORE INTO DATES
        VALUES
        ("START",NULL),
        ("END",NULL)
    """)

    cursor.execute("CREATE USER IF NOT EXISTS 'reader'@'localhost' IDENTIFIED BY 'reader@161387'")
    cursor.execute("GRANT SELECT ON ACCOUNTING_RECORDS.* TO 'reader'@'localhost' ")
    cursor.execute("CREATE USER IF NOT EXISTS 'editor'@'localhost' IDENTIFIED BY 'editor@161387'")
    cursor.execute("GRANT SELECT,INSERT,UPDATE,DELETE ON ACCOUNTING_RECORDS.* TO 'editor'@'localhost' ")
    cursor.execute("FLUSH PRIVILEGES")

    # Store application login password hash
    cursor.execute("CREATE TABLE IF NOT EXISTS yjbbfxamb(SR_NO INT PRIMARY KEY,yjbbfxamb VARCHAR(255))")
    default_passkey="easestock@1234"
    crypt_pwd=password_cryptography.hash_password(default_passkey)
    cursor.execute("INSERT IGNORE INTO yjbbfxamb VALUES(1,%s)",(crypt_pwd,))

    conn.commit()
    cursor.close()
    conn.close()



