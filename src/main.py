import os
from typing import Union

from fastapi import FastAPI
from motor import motor_asyncio

from . import config

app = FastAPI()
settings = config.Settings()
client = motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.users


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
