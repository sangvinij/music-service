from fastapi import APIRouter

from app.api.routes.v1.healthcheck import healthcheck_router

api_router: APIRouter = APIRouter(prefix="/v1")
api_router.include_router(healthcheck_router)
