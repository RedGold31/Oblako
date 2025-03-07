from db_connect import db

def select_users():
    return db.execute("select_users", {}).all()

