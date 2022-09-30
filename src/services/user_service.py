from fastapi.encoders import jsonable_encoder

from src.database import database
from src.models.user_model import UserModel


async def create_user(user: UserModel):
    user = jsonable_encoder(user)
    new_user = await database["users"].insert_one(user)
    created_user = await database["users"].find_one({"_id": new_user.inserted_id})
    return created_user


async def list_users(limit: int = 1000):
    students = await database["users"].find().to_list(limit)
    return students


async def get_user(id: str):
    if (user := await database["users"].find_one({"_id": id})) is not None:
        return user
