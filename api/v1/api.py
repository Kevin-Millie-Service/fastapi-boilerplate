from fastapi import APIRouter

from api.v1.basic import test

api_v1_router = APIRouter()
api_v1_router.include_router(test.router, prefix='/test', tags=["test"])