from fastapi import APIRouter, FastAPI
from fastapi.staticfiles import StaticFiles

from . import config
from .routes import (
    ad_route,
    click_route,
    company_route,
    health_route,
    index_route,
    location_route,
    user_route,
)

app = FastAPI()
settings = config.Settings()

router = APIRouter()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

router.include_router(health_route.router)
router.include_router(user_route.router)
router.include_router(company_route.router)
router.include_router(location_route.router)
router.include_router(ad_route.router)
router.include_router(click_route.router)
router.include_router(index_route.router)
app.include_router(router)
