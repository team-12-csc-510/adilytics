import os

from fastapi import APIRouter, FastAPI
from starlette.staticfiles import StaticFiles

from . import config
from .routes import (
    ad_route,
    click_route,
    company_route,
    health_route,
    index_route,
    location_route,
    product_route,
    user_route,
)

# Initialize App
app = FastAPI()
# Load App settings
settings = config.Settings()
script_dir = os.path.dirname(__file__)
st_abs_file_path = os.path.join(script_dir, "..", "static/")

# Initialize Routes
router = APIRouter()
app.mount("/static", StaticFiles(directory=st_abs_file_path, html=True), name="static")
router.include_router(health_route.router)
router.include_router(user_route.router)
router.include_router(company_route.router)
router.include_router(location_route.router)
router.include_router(ad_route.router)
router.include_router(click_route.router)
router.include_router(product_route.router)
router.include_router(index_route.router)
app.include_router(router)
