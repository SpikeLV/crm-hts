from fastapi import APIRouter

from core.config import settings
from .users import router as users_router
from .fipers import router as fipers_router
from .jupers import router as jupers_router

ROUTERS: list[tuple[APIRouter, str]] = [
    (users_router, settings.api.v1.users),
    (fipers_router, settings.api.v1.fipers),
    (jupers_router, settings.api.v1.jupers),
]

router = APIRouter()

for route, prefix in ROUTERS:
    router.include_router(route, prefix=prefix)