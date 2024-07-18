from fastapi import APIRouter

from app.api.routes.v1.albums import albums_router
from app.api.routes.v1.healthcheck import healthcheck_router
from app.api.routes.v1.playlists import playlists_router
from app.api.routes.v1.tracks import tracks_router

api_router: APIRouter = APIRouter(prefix="/v1")
api_router.include_router(healthcheck_router, tags=["healthcheck"])
api_router.include_router(tracks_router, tags=["tracks"])
api_router.include_router(albums_router, tags=["albums"])
api_router.include_router(playlists_router, tags=["playlists"])
