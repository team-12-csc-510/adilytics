from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.services import health_service

router = APIRouter(prefix="/health")


@router.get("/")
async def health():
    _health = await health_service.system_checks(verbose=0)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=_health)
