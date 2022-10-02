from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/")
async def get_index(request: Request):
    return templates.TemplateResponse("index2.html", {"request": request})
