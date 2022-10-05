from fastapi import APIRouter, FastAPI

from . import config
from .routes import (
    ad_route,
    click_route,
    company_route,
    health_route,
    location_route,
    product_route,
    user_route,
)

app = FastAPI()
settings = config.Settings()

router = APIRouter()

router.include_router(health_route.router)
router.include_router(user_route.router)
router.include_router(company_route.router)
router.include_router(location_route.router)
router.include_router(ad_route.router)
router.include_router(click_route.router)
router.include_router(product_route.router)
app.include_router(router)
