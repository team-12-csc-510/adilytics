from src.services.ad_service import get_conversions
from src.services.click_service import get_total_clicks
from src.services.user_service import get_new_users, get_total_sessions


async def create_obj():
    # click count in last month
    data = {}
    # data["click_count"] = await list_all_clicks()
    # bounce rate= clicks/ sessions
    total_clicks = await get_total_clicks()
    total_session = await get_total_sessions()
    bounce_rate = ((total_session - total_clicks) / total_session) * 100
    bounce_rate = format(bounce_rate, ".2f")
    data["bounce_rate"] = bounce_rate
    # conversions
    data["total_conversion"] = await get_conversions()
    # new users
    data["total_new_users"] = await get_new_users()
    return data
