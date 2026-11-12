import mysql.connector

db_pwd=None
def get_db_password(db_password):
    global db_pwd
    db_pwd=db_password
def db_connector():#for editing
    return  mysql.connector.connect(
            host="localhost",
            user="editor",
            password='editor@161387',
            database="ACCOUNTING_RECORDS"
        )
def db_connector_root():#for connection
    return  mysql.connector.connect(
                host="localhost",
                user="root",
                password=db_pwd
            )
def db_connector_reader():
    return mysql.connector.connect(
    host='localhost',
    user='reader',
    password='reader@161387',
    database='ACCOUNTING_RECORDS'
    )

