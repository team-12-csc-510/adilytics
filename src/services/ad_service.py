from typing import Dict

from fastapi.encoders import jsonable_encoder

from src.database.init_db import Database
from src.models.ad_model import AdModel, UpdateAdModel
from src.utils.database_const import Collections, Databases

ad_db = Database()
ad_db.database = Databases.adilytics.name
ad_db.collection = Collections.ad.name


async def create_ad(ad: AdModel):
    ad = jsonable_encoder(ad)
    new_ad = await ad_db.collection.insert_one(ad)
    created_ad = await ad_db.collection.find_one({"_id": new_ad.inserted_id})
    return created_ad


async def list_ads(limit: int = 1000):
    # TODO: remove to_list & add skip and list
    # https://pymongo.readthedocs.io/en/3.11.0/api/pymongo/collection.html#pymongo.collection.Collection.find
    ads = await ad_db.collection.find().to_list(limit)
    return ads


async def get_ad(id: str):
    if (ad := await ad_db.collection.find_one({"_id": id})) is not None:
        return ad


async def update_ad(id: str, ad: UpdateAdModel):
    ad_dict: Dict[str, str] = {k: v for k, v in ad.dict().items() if v is not None}

    if len(ad_dict) >= 1:
        update_result = await ad_db.collection.update_one(
            {"_id": id}, {"$set": ad_dict}
        )

        if update_result.modified_count == 1:
            if (updated_ad := await ad_db.collection.find_one({"_id": id})) is not None:
                return updated_ad

    if (existing_ad := await ad_db.collection.find_one({"_id": id})) is not None:
        return existing_ad


async def delete_ad(id: str):
    delete_result = await ad_db.collection.delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return True
    return False
