from typing import Dict

from fastapi.encoders import jsonable_encoder

from src.database.init_db import Database
from src.models.ad_model import AdModel, UpdateAdModel
from src.routes.company_route import list_companies
from src.services.location_service import list_locations
from src.utils.database_const import Collections, Databases

ad_db = Database()
ad_db.database = Databases.adilytics.name
ad_db.collection = Collections.ad.name


async def create_obj():
    p = await list_locations()
    return p
