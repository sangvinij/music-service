from fastapi import FastAPI

from app.api.routes.v1 import api_router as api_router_v1


def init_api(app: FastAPI) -> None:
    app.include_router(router=api_router_v1, prefix="/music/api")
