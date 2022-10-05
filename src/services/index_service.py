from typing import Dict

from fastapi.encoders import jsonable_encoder

from src.database.init_db import Database
from src.models.ad_model import AdModel, UpdateAdModel
from src.routes.company_route import list_companies
from src.services.ad_service import get_conversions
from src.services.click_service import list_all_clicks, get_total_clicks, list_all_clicks_and_converted
from src.services.location_service import list_locations
from src.services.user_service import get_total_sessions, get_new_users
from src.utils.database_const import Collections, Databases

ad_db = Database()
ad_db.database = Databases.adilytics.name
ad_db.collection = Collections.ad.name


async def create_obj():
    # click_count = await list_all_clicks()
    # total_sessions = await get_total_clicks()
    total_conversion= await get_conversions()
    return total_conversion