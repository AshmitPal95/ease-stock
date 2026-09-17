import mysql.connector

db_pwd=None
def get_db_password(db_password):
    global db_pwd
    db_pwd=db_password
def db_connector():
    return  mysql.connector.connect(
            host="localhost",
            user="root",
            password=db_pwd,
            database="ACCOUNTING_RECORDS"
        )
