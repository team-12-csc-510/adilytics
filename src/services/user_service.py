from datetime import datetime, timedelta
from random import randint
from typing import Dict

from fastapi.encoders import jsonable_encoder

from src.database.init_db import Database
from src.models.user_model import UpdateUserModel, UserModel
from src.services.location_service import get_location
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


async def get_total_sessions():
    # https://pymongo.readthedocs.io/en/3.11.0/api/pymongo/collection.html#pymongo.collection.Collection.find
    session_count = 0
    async for user in user_db.collection.find():
        if "session" in user.keys():
            session_count += user["session"]
    return session_count


async def get_new_users():
    # https://pymongo.readthedocs.io/en/3.11.0/api/pymongo/collection.html#pymongo.collection.Collection.find
    user_count = 0
    today = datetime.today()
    days_back = today - timedelta(days=30)
    async for user in user_db.collection.find({"created_at": {"$gte": str(days_back)}}):
        user_count += 1
    return user_count


async def get_user_info_with_location():
    # create a dictionary containing a users at a location, location name, longitude , latitude
    data = {}
    async for user in user_db.collection.find():
        # location_detail = await get_location(user['location_id'])
        if user['location_id'] not in data:
            data[user['location_id']] = {}
            data[user['location_id']]["value"] = 1
            data[user['location_id']]["longitude"] = -78.644257 + randint(1, 10)
            data[user['location_id']]["latitude"]= 35.787743 + randint(1, 10)
            data[user['location_id']]["tooltip"] = {}
            data[user['location_id']]["tooltip"]["content"] = "Hmm {}".format(data[user['location_id']]["value"])
            # < span
            # style =\"font-weight:bold;\">{}</span><br />'.format('abc')
        else:
            data[user['location_id']]["value"] = data[user['location_id']]["value"] + 1
            data[user['location_id']]["tooltip"]["content"] = "Hmm".format(data[user['location_id']]["value"])
    return data
