from src.services.ad_service import get_conversions, get_conversions_time_range
from src.services.click_service import get_total_clicks, get_click_data_time_range
from src.services.user_service import get_new_users, get_total_sessions
from src.utils.time_utils import get_end_month_date, get_start_month_date


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
    data["total_conversion"] = format(await get_conversions(), ".2f")
    # new users
    data["total_new_users"] = await get_new_users()
    sales_data=[]
    for i in range(1,7):
        sales_data.append(format(await get_conversions_time_range(get_start_month_date(i),get_end_month_date(i)),".2f"))
    sales_data.reverse()
    data["sales"]=sales_data

    visitor_data=[]
    # get_click_data_time_range
    normalization= round(1/float(bounce_rate)*100)
    for i in range(1,7):
        visitors = await get_click_data_time_range(get_start_month_date(i),get_end_month_date(i))
        visitors= int(visitors)*normalization
        visitor_data.append(visitors)
    visitor_data.reverse()
    data["visitors"]=visitor_data
    return data
