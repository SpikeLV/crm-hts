from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from api import api_router
from core.models.db_helper import db_helper
from contextlib import asynccontextmanager
from core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    #startup event
    yield
    #shutdown event
    print("Shutting down...")
    await db_helper.dispose()

main_app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan = lifespan,
)

# Add CORS middleware to allow requests from frontend
main_app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors.get_origins_list(),
    allow_credentials=settings.cors.allow_credentials,
    allow_methods=settings.cors.allow_methods,
    allow_headers=settings.cors.allow_headers,
)

main_app.include_router(
    api_router, 
    prefix=settings.api.prefix)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=settings.run.reload)