import os

from dotenv import load_dotenv

from sqldb import SQLDB

load_dotenv()
db = SQLDB(
    {
        "host": os.getenv("DB_IP"),
        "port": os.getenv("DB_PORT"),
        "database": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
    }
)

users = db.execute("select_users", {}).all()

print(users)
