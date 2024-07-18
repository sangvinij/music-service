from fastapi import APIRouter, status
from fastapi.params import Path

tracks_router = APIRouter(prefix="/tracks")


@tracks_router.get("/{track_id}", status_code=status.HTTP_200_OK)
async def get_one_track(track_id: int = Path()):
    pass


@tracks_router.patch("/{track_id}", status_code=status.HTTP_200_OK)
async def update_one_track(track_id: int = Path()):
    pass


@tracks_router.delete("/{track_id}", status_code=status.HTTP_200_OK)
async def delete_one_track(track_id: int = Path()):
    pass


@tracks_router.get("/", status_code=status.HTTP_200_OK)
async def get_tracks_list():
    pass


@tracks_router.post("/", status_code=status.HTTP_200_OK)
async def create_track():
    pass
