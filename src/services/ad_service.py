from typing import Dict

from fastapi.encoders import jsonable_encoder

from src.database.init_db import Database
from src.models.ad_model import AdModel, UpdateAdModel
from src.services.click_service import (
    list_all_clicks_and_converted,
    list_all_clicks_and_converted_time_range,
)
from src.services.product_service import get_product
from src.utils.database_const import Collections, Databases

ad_db = Database()
ad_db.database = Databases.adilytics.name
ad_db.collection = Collections.ad.name


async def create_ad(ad: AdModel):
    """Function to add a new ad to the ad collection

    :param ad: AdModel object containing the required tuple details
    :return: the inserted tuple
    """
    ad = jsonable_encoder(ad)
    new_ad = await ad_db.collection.insert_one(ad)
    created_ad = await ad_db.collection.find_one({"_id": new_ad.inserted_id})
    return created_ad


async def list_ads(limit: int = 1000):
    """Function to list all the ads in the collection

    :param limit: maximum number to entries to be fetched,
    defaults to 1000
    :return: all the ads
    """
    # TODO: remove to_list & add skip and list
    # https://pymongo.readthedocs.io/en/3.11.0/api/pymongo/collection.html#pymongo.collection.Collection.find
    ads = await ad_db.collection.find().to_list(limit)
    return ads


async def get_ad(id: str):
    """Function to get a particular ad from the collection

    :param id: id of the ad to be retrieved.
    :type id: str
    :return: the requested ad
    """
    if (ad := await ad_db.collection.find_one({"_id": id})) is not None:
        return ad


async def update_ad(id: str, ad: UpdateAdModel):
    """Function to update a particular entry

    :param id: id of the entry to be updated
    :type id: str
    :param ad: UpdateAdModel object with the updated details
    :return: the updated details
    """
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
    """Function to delete a particular entry

    :param id: id of the entry to be deleted
    :type id: str
    :return: the deleted details
    """
    delete_result = await ad_db.collection.delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return True
    return False


async def get_conversions():
    """Function to get how many of the clicked were converted

    :return: total conversions
    """
    # Get all clicks to last 30 days
    converted_ads = await list_all_clicks_and_converted()
    total_conversions = 0
    for ad in converted_ads:
        ad_detail = await get_ad(ad)
        product_detail = await get_product(ad_detail["product_id"])
        total_conversions += product_detail["cost"] * converted_ads[ad]
    return total_conversions


async def get_conversions_time_range(start_time, end_time):
    # Get all clicks to last 30 days
    converted_ads = await list_all_clicks_and_converted_time_range(start_time, end_time)
    total_conversions = 0
    for ad in converted_ads:
        ad_detail = await get_ad(ad)
        product_detail = await get_product(ad_detail["product_id"])
        total_conversions += product_detail["cost"] * converted_ads[ad]
    return total_conversions


async def get_conversions_by_ad_type(ad_type):
    converted_ads = await list_all_clicks_and_converted()
    total_conversions = 0
    for ad in converted_ads:
        ad_detail = await get_ad(ad)
        if ad_type.value == ad_detail["type"]:
            product_detail = await get_product(ad_detail["product_id"])
            total_conversions += product_detail["cost"] * converted_ads[ad]
    return total_conversions
