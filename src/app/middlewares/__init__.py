from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.middlewares.cors import cors_settings


def init_middlewares(app: FastAPI) -> None:
    app.add_middleware(CORSMiddleware, **cors_settings)
