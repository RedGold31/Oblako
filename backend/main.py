from pydantic import BaseModel, ConfigDict
from fastapi import FastAPI, HTTPException, Response
from fastapi import Depends
from authx import AuthX, AuthXConfig
import uvicorn

app = FastAPI()

class STaskAdd(BaseModel):

   name: str
   description: str | None = None

class STask(STaskAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)

class UserLoginScheme(BaseModel):
    username: str
    password: str

config = AuthXConfig()
config.JWT_SECRET_KEY = "SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)

@app.post("/login")
async def login(creds: UserLoginScheme, response: Response):
    if creds.username == "admin" and creds.password == "admin":
        token=security.create_access_token(uid="bd_user_id")
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"access_token":token}
    raise HTTPException(status_code=401, detail="incorrect username or password")

@app.post("/")
async def add_task(task: STaskAdd = Depends()):
   return {"data": task}

if __name__ == "__main__" :
    uvicorn.run(app=app)