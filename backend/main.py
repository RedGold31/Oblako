from sys import exception

import uvicorn
from authx import AuthX, AuthXConfig
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from config import host, port, user, password, bd_name
import psycopg2


app = FastAPI()

try:
    # подключение к бд, данные передаются из файла конфиг(данные взял те что ранее кидал Егор)
    connection = psycopg2.connect(
        host = host,
        port = port,
        user = user,
        password = password,
        database = bd_name

    )
    connection.autocommit = True
    # средство для внесения данных
    with connection.cursor() as cursor:
        cursor.execute( "INSERT INTO users (user_name, password) VALUES ()")
        print("[INFO] data was successfully insert")

    # для извлечения данных
    with connection.cursor() as cursor:
        cursor.execute("SELECT password FROM users WHERE user_name = ")


except Exception as _ex:
    print("[INFO]Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed ")




class UserLoginScheme(BaseModel): #class for users authorization date
    username: str
    password: str

config = AuthXConfig() # configs for JWT and cookies
config.JWT_SECRET_KEY = "SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME = "access_token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)

@app.post("/login")
async def login(creds: UserLoginScheme): # for check correspondence of user data which get and user data from bd
    if creds.username == "admin" and creds.password == "admin": # correspondence check
        token=security.create_access_token(uid="bd_user_id") #token create with id from bd
        response=JSONResponse({"access_token":token})
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token) #create cookie
        return response
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="incorrect username or password") # if data don`t correspondence

if __name__ == "__main__" :
    uvicorn.run(app=app)