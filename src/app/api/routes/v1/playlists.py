from fastapi import APIRouter, status
from fastapi.params import Path

tracks_router = APIRouter(prefix="/tracks")


@tracks_router.get("/{playlist_id}", status_code=status.HTTP_200_OK)
async def get_playlist(playlist_id: int = Path()):
    pass


@tracks_router.patch("/{playlist_id}/tracks", status_code=status.HTTP_200_OK)
async def add_track_to_playlist(playlist_id: int = Path()):
    pass


@tracks_router.delete("/{playlist_id}/tracks", status_code=status.HTTP_200_OK)
async def remove_track_from_playlist(playlist_id: int = Path()):
    pass


@tracks_router.delete("/{playlist_id}", status_code=status.HTTP_200_OK)
async def delete_playlist(playlist_id: int = Path()):
    pass


@tracks_router.get("/", status_code=status.HTTP_200_OK)
async def get_playlists():
    pass


@tracks_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_playlist():
    pass
