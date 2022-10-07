import json

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from src.services.index_service import create_obj

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/")
async def get_index(request: Request):
    """Function to handle the GET request to get a particular index from the
    collection

    :param request: Request of the index to be retrieved.
    :return: JSON object with the requested index and HTTP response or an HTTP error
    """
    val = await create_obj()
    return templates.TemplateResponse(
        "index2.html",
        {
            "request": request,
            "data": val,
            "sales": json.dumps(val["sales"]),
            "ads": (val["ads"]),
            "revenue": json.dumps(val["revenue"]),
            "visitors": json.dumps(val["visitors"]),
            "locations": (val["location_data"]),
        },
    )
