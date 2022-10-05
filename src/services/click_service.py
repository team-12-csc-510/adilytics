from datetime import datetime, timedelta
from typing import Dict

from fastapi.encoders import jsonable_encoder

from src.database.init_db import Database
from src.models.click_model import ClickModel, UpdateClickModel
from src.utils.database_const import Collections, Databases
from src.utils.time_utils import now, str2datetime, timediff30

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


async def list_all_clicks(limit: int = 1000):
    # TODO: remove to_list & add skip and list
    # https://pymongo.readthedocs.io/en/3.11.0/api/pymongo/collection.html#pymongo.collection.Collection.find
    clicks = await click_db.collection.find().to_list(limit)
    allclk: Dict = dict()
    for inst in clicks:
        dt_now = now()
        dt_inst = str2datetime(inst.get("updated_at"))
        if timediff30(dt_now - dt_inst):
            if allclk.get(inst.get("ad_id")) is None:
                allclk[inst.get("ad_id")] = 1
            else:
                allclk[inst.get("ad_id")] += 1
        else:
            allclk[inst.get("ad_id")] = 0
    return allclk


async def get_total_clicks():
    # https://pymongo.readthedocs.io/en/3.11.0/api/pymongo/collection.html#pymongo.collection.Collection.find
    click_count = 0
    async for click in click_db.collection.find():
        click_count += 1
    return click_count


async def list_all_clicks_and_converted(limit: int = 1000):
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

async def list_all_clicks_and_converted_time_range(startDate,endDate):
    # https://pymongo.readthedocs.io/en/3.11.0/api/pymongo/collection.html#pymongo.collection.Collection.find
    today = datetime.today()
    days_back = today - timedelta(days=30)
    allclk: Dict = dict()
    async for click in click_db.collection.find(
        {"is_converted": True, "created_at": {"$gte": str(startDate),"$lt": str(endDate)}}
    ):
        if allclk.get(click.get("ad_id")) is None:
            allclk[click.get("ad_id")] = 1
        else:
            allclk[click.get("ad_id")] += 1
    return allclk

async def get_click_data_time_range(start_time,end_time):
    # https://pymongo.readthedocs.io/en/3.11.0/api/pymongo/collection.html#pymongo.collection.Collection.find
    clicks = 0
    async for click in click_db.collection.find(
        {"is_converted": True, "created_at": {"$gte": str(start_time),"$lt": str(end_time)}}
    ):
        clicks+=1
    return clicks