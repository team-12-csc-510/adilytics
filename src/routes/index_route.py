from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from src.services.index_service import create_obj

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/")
async def get_index(request: Request):
    val = await create_obj()
    return templates.TemplateResponse("index2.html", {"request": request})
