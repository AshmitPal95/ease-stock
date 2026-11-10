import bcrypt
def hash_password(user_password: str):
    passkey=user_password.encode("utf-8")
    salt = bcrypt.gensalt() 
    hashed = bcrypt.hashpw(passkey, salt)
    return hashed.decode("utf-8")
