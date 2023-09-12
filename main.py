from fastapi import FastAPI

from api.v1.api import api_v1_router
from core.config import settings


app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(api_v1_router)
