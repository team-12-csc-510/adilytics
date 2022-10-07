from datetime import datetime, timedelta
from typing import Dict

from fastapi.encoders import jsonable_encoder

from src.database.init_db import Database
from src.models.click_model import ClickModel, UpdateClickModel
from src.utils.database_const import Collections, Databases

click_db = Database()
click_db.database = Databases.adilytics.name
click_db.collection = Collections.click.name


async def create_click(click: ClickModel):
    """
    Function to add a new ad to the click collection

    :param ad: ClickModel object containing the required tuple details
    :return: the inserted tuple
    """
    click = jsonable_encoder(click)
    new_click = await click_db.collection.insert_one(click)
    created_new_click = await click_db.collection.find_one(
        {"_id": new_click.inserted_id}
    )
    return created_new_click


async def list_clicks(limit: int = 1000):
    """
    Function to list all the clicks in the collection

    :param limit: maximum number to entries to be fetched,
    defaults to 1000
    :return: all the clicks
    """
    # TODO: remove to_list & add skip and list
    # https://pymongo.readthedocs.io/en/3.11.0/api/pymongo/collection.html#pymongo.collection.Collection.find
    clicks = await click_db.collection.find().to_list(limit)
    return clicks


async def get_click(id: str):
    """
    Function to get a particular click from the collection

    :param id: id of the click to be retrieved.
    :type id: str
    :return: the requested click
    """
    if (click := await click_db.collection.find_one({"_id": id})) is not None:
        return click


async def update_click(id: str, click: UpdateClickModel):
    """
    Function to update a particular entry

    :param id: id of the entry to be updated
    :type id: str
    :param ad: UpdateClickModel object with the updated details
    :return: the updated details
    """
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
    """
    Function to delete a particular entry

    :param id: id of the entry to be deleted
    :type id: str
    :return: the deleted details
    """

    delete_result = await click_db.collection.delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return True
    return False


async def list_all_clicks(limit: int = 1000):
    """
    Function to get user click count in past 30 days
    :param limit:
    :return: Total number of clicks
    """
    # TODO: remove to_list & add skip and list
    # https://pymongo.readthedocs.io/en/3.11.0/api/pymongo/collection.html#pymongo.collection.Collection.find
    user_count = 0
    today = datetime.now()
    days_back = today - timedelta(days=30)
    async for click in click_db.collection.find(
        {"created_at": {"$gte": str(days_back)}}
    ):
        user_count += 1
    return user_count


async def get_total_clicks():
    """
    Function to get total click counts in the Click collection
    :return: Total clicks
    """
    # https://pymongo.readthedocs.io/en/3.11.0/api/pymongo/collection.html#pymongo.collection.Collection.find
    click_count = 0
    async for click in click_db.collection.find():
        click_count += 1
    return click_count


async def list_all_clicks_and_converted(limit: int = 1000):
    """
    Function to get all the converted clicks
    :param limit:
    :return: Count of converted clicks
    """
    # https://pymongo.readthedocs.io/en/3.11.0/api/pymongo/collection.html#pymongo.collection.Collection.find
    today = datetime.today()
    days_back = today - timedelta(days=30)
    allclk: Dict = dict()
    async for click in click_db.collection.find(
        {"is_converted": True, "created_at": {"$gte": str(days_back)}}
    ):
        if allclk.get(click.get("ad_id")) is None:
            allclk[click.get("ad_id")] = 1
        else:
            allclk[click.get("ad_id")] += 1
    return allclk


async def list_all_clicks_and_converted_time_range(startDate, endDate):
    # https://pymongo.readthedocs.io/en/3.11.0/api/pymongo/collection.html#pymongo.collection.Collection.find
    allclk: Dict = dict()
    async for click in click_db.collection.find(
        {
            "is_converted": True,
            "created_at": {"$gte": str(startDate), "$lt": str(endDate)},
        }
    ):
        if allclk.get(click.get("ad_id")) is None:
            allclk[click.get("ad_id")] = 1
        else:
            allclk[click.get("ad_id")] += 1
    return allclk


async def get_click_data_time_range(start_time, end_time):
    # https://pymongo.readthedocs.io/en/3.11.0/api/pymongo/collection.html#pymongo.collection.Collection.find
    clicks = 0
    async for click in click_db.collection.find(
        {
            "is_converted": True,
            "created_at": {"$gte": str(start_time), "$lt": str(end_time)},
        }
    ):
        clicks += 1
    return clicks
