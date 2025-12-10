from fastapi import APIRouter

from core.config import settings
from .users import router as users_router
from .fipers import router as fipers_router
from .decontamination import router as decontamination_router
from .dec_preset import router as dec_preset_router

ROUTERS: list[tuple[APIRouter, str]] = [
    (users_router, settings.api.v1.users),
    (fipers_router, settings.api.v1.fipers),
    (decontamination_router, settings.api.v1.decontaminations),
    (dec_preset_router, settings.api.v1.dec_presets),
]

router = APIRouter()

for route, prefix in ROUTERS:
    router.include_router(route, prefix=prefix)