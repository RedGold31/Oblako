from pydantic import BaseModel, ConfigDict
from fastapi import FastAPI
import uvicorn

app = FastAPI()

class STaskAdd(BaseModel):

   name: str
   description: str | None = None

class STask(STaskAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)

@app.get("/")
async def add_task(task: STaskAdd):
   return {"data": task}