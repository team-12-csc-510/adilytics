from typing import Dict

from fastapi.encoders import jsonable_encoder

from src.database.init_db import Database
from src.models.click_model import ClickModel, UpdateClickModel
from src.utils.database_const import Collections, Databases

click_db = Database()
click_db.database = Databases.adilytics.name
click_db.collection = Collections.click.name


async def create_click(click: ClickModel):
    click = jsonable_encoder(click)
    new_click = await click_db.collection.insert_one(click)
    created_new_click = await click_db.collection.find_one(
        {"_id": new_click.inserted_id}
    )
    return created_new_click


async def list_clicks(limit: int = 1000):
    # TODO: remove to_list & add skip and list
    # https://pymongo.readthedocs.io/en/3.11.0/api/pymongo/collection.html#pymongo.collection.Collection.find
    clicks = await click_db.collection.find().to_list(limit)
    return clicks


async def get_click(id: str):
    if (click := await click_db.collection.find_one({"_id": id})) is not None:
        return click


async def update_click(id: str, click: UpdateClickModel):
    click_dict: Dict[str, str] = {
        k: v for k, v in click.dict().items() if v is not None
    }

    if len(click_dict) >= 1:
        update_result = await click_db.collection.update_one(
            {"_id": id}, {"$set": click_dict}
        )

        if update_result.modified_count == 1:
            if (
                updated_click := await click_db.collection.find_one({"_id": id})
            ) is not None:
                return updated_click

    if (existing_click := await click_db.collection.find_one({"_id": id})) is not None:
        return existing_click


async def delete_click(id: str):
    delete_result = await click_db.collection.delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return True
    return False
