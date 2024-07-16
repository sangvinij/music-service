from fastapi import FastAPI

from app.api.routes import init_api
from app.middlewares import init_middlewares
from app.settings.settings import settings


def create_app() -> FastAPI:
    _app = FastAPI(
        title="music_service",
        version=settings.VERSION,
        docs_url="/music/docs",
    )
    init_api(_app)
    init_middlewares(_app)
    return _app


app: FastAPI = create_app()
