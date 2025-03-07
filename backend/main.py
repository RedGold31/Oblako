import uvicorn
from authx import AuthX, AuthXConfig
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from models import UserLoginScheme
from bd_connect.functions import select_users

app = FastAPI()

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