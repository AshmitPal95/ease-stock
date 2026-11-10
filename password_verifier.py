import bcrypt
import mysql.connector
import config
def check_passkey(user_passkey):
    conn=config.db_connector_reader()
    cursor=conn.cursor()
    cursor.execute("SELECT yjbbfxamb FROM yjbbfxamb WHERE SR_NO=1")
    required_passkey=cursor.fetchone()[0].encode('utf-8')
    cursor.close()
    conn.close()
    if bcrypt.checkpw(user_passkey.encode('utf-8'),required_passkey):
        return True
    else:
        return False


