from typing import Dict

from fastapi.encoders import jsonable_encoder

from src.database.init_db import Database
from src.models.user_model import UpdateUserModel, UserModel
from src.utils.database_const import Collections, Databases

user_db = Database()
user_db.database = Databases.adilytics.name
user_db.collection = Collections.users.name


async def create_user(user: UserModel):
    user = jsonable_encoder(user)
    new_user = await user_db.collection.insert_one(user)
    created_user = await user_db.collection.find_one({"_id": new_user.inserted_id})
    return created_user


async def list_users(limit: int = 1000):
    # TODO: remove to_list & add skip and list
    # https://pymongo.readthedocs.io/en/3.11.0/api/pymongo/collection.html#pymongo.collection.Collection.find
    students = await user_db.collection.find().to_list(limit)
    return students


async def get_user(id: str):
    if (user := await user_db.collection.find_one({"_id": id})) is not None:
        return user


async def update_user(id: str, user: UpdateUserModel):
    user_dict: Dict[str, str] = {k: v for k, v in user.dict().items() if v is not None}

    if len(user_dict) >= 1:
        update_result = await user_db.collection.update_one(
            {"_id": id}, {"$set": user_dict}
        )

        if update_result.modified_count == 1:
            if (
                updated_user := await user_db.collection.find_one({"_id": id})
            ) is not None:
                return updated_user

    if (existing_user := await user_db.collection.find_one({"_id": id})) is not None:
        return existing_user


async def delete_user(id: str):
    delete_result = await user_db.collection.delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return True
    return False
