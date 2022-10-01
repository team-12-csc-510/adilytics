from typing import Dict

from fastapi.encoders import jsonable_encoder

from src.database.init_db import Database
from src.models.location_model import UpdateLocationModel, LocationModel
from src.utils.database_const import Collections, Databases

# user_db = Database()
location_db = Database()
# user_db.database = Databases.adilytics.name
location_db.database = Databases.adilytics.name
# user_db.collection = Collections.users.name
location_db.collection = Collections.locations.name


async def create_location(location: LocationModel):
    location = jsonable_encoder(location)
    new_location = await location_db.collection.insert_one(location)
    created_location = await location_db.collection.find_one({"_id": new_location.inserted_id})
    return created_location


async def list_location(limit: int = 1000):
    # TODO: remove to_list & add skip and list
    # https://pymongo.readthedocs.io/en/3.11.0/api/pymongo/collection.html#pymongo.collection.Collection.find
    students = await location_db.collection.find().to_list(limit)
    return students


async def get_location(id: str):
    if (location := await location_db.collection.find_one({"_id": id})) is not None:
        return location


async def update_location(id: str, location: UpdateLocationModel):
    location_dict: Dict[str, str] = {k: v for k, v in location.dict().items() if v is not None}

    if len(location_dict) >= 1:
        update_result = await location_db.collection.update_one(
            {"_id": id}, {"$set": location_dict}
        )

        if update_result.modified_count == 1:
            if (
                updated_location := await location_db.collection.find_one({"_id": id})
            ) is not None:
                return updated_location

    if (existing_location := await location_db.collection.find_one({"_id": id})) is not None:
        return existing_location


async def delete_location(id: str):
    delete_result = await location_db.collection.delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return True
    return False