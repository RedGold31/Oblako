from pydantic import BaseModel


class UserLoginScheme(BaseModel): #class for users authorization date
    username: str
    password: str