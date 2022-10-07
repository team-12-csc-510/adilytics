from typing import Dict

from fastapi.encoders import jsonable_encoder

from src.database.init_db import Database
from src.models.location_model import LocationModel, UpdateLocationModel
from src.utils.database_const import Collections, Databases

location_db = Database()
location_db.database = Databases.adilytics.name
location_db.collection = Collections.location.name


async def create_location(location: LocationModel):
    """Function to add a new location to the location collection

    :param location: LocationModel object containing the required tuple details
    :return: the inserted tuple
    """
    location = jsonable_encoder(location)
    new_location = await location_db.collection.insert_one(location)
    created_location = await location_db.collection.find_one(
        {"_id": new_location.inserted_id}
    )
    return created_location


async def list_locations(limit: int = 1000):
    """Function to list all the locations in the collection

    :param limit: maximum number to entries to be fetched,
    defaults to 1000
    :return: all the locations
    """
    # TODO: remove to_list & add skip and list
    # https://pymongo.readthedocs.io/en/3.11.0/api/pymongo/collection.html#pymongo.collection.Collection.find
    students = await location_db.collection.find().to_list(limit)
    return students


async def get_location(id: str):
    """Function to get a particular location from the collection

    :param id: id of the location to be retrieved.
    :type id: str
    :return: the requested location
    """
    if (location := await location_db.collection.find_one({"_id": id})) is not None:
        return location
    else:
        return None


async def update_location(id: str, location: UpdateLocationModel):
    """Function to update a particular entry

    :param id: id of the entry to be updated
    :type id: str
    :param location: UpdateLocationModel object with the updated details
    :return: the updated details
    """
    location_dict: Dict[str, str] = {
        k: v for k, v in location.dict().items() if v is not None
    }

    if len(location_dict) >= 1:
        update_result = await location_db.collection.update_one(
            {"_id": id}, {"$set": location_dict}
        )

        if update_result.modified_count == 1:
            if (
                updated_location := await location_db.collection.find_one({"_id": id})
            ) is not None:
                return updated_location

    if (
        existing_location := await location_db.collection.find_one({"_id": id})
    ) is not None:
        return existing_location


async def delete_location(id: str):
    """Function to delete a particular entry

    :param id: id of the entry to be deleted
    :type id: str
    :return: the deleted details
    """
    delete_result = await location_db.collection.delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return True
    return False
