from fastapi import APIRouter, FastAPI

from . import config
from .routes import company_route, health_route, user_route

app = FastAPI()
settings = config.Settings()

router = APIRouter()

router.include_router(health_route.router)
router.include_router(user_route.router)
router.include_router(company_route.router)
app.include_router(router)
