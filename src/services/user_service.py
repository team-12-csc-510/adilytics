from typing import Dict

from fastapi.encoders import jsonable_encoder

from src.database import database
from src.models.user_model import UpdateUserModel, UserModel


async def create_user(user: UserModel):
    user = jsonable_encoder(user)
    new_user = await database["users"].insert_one(user)
    created_user = await database["users"].find_one(
        {"_id": new_user.inserted_id}
    )
    return created_user


async def list_users(limit: int = 1000):
    students = await database["users"].find().to_list(limit)
    return students


async def get_user(id: str):
    if (user := await database["users"].find_one({"_id": id})) is not None:
        return user


async def update_user(id: str, user: UpdateUserModel):
    user_dict: Dict[str, str] = {
        k: v for k, v in user.dict().items() if v is not None
    }

    if len(user_dict) >= 1:
        update_result = await database["users"].update_one(
            {"_id": id}, {"$set": user_dict}
        )

        if update_result.modified_count == 1:
            if (
                updated_user := await database["users"].find_one({"_id": id})
            ) is not None:
                return updated_user

    if (
        existing_user := await database["users"].find_one({"_id": id})
    ) is not None:
        return existing_user


async def delete_user(id: str):
    delete_result = await database["users"].delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return True
    return False
