from fastapi import APIRouter
from core.config import settings
from .api_v1 import router as api_v1_router

# Create empty router - routers will be registered in main.py
api_router = APIRouter()
api_router.include_router(
    api_v1_router,
    prefix=settings.api.v1.prefix,
)