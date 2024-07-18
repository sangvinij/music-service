from fastapi import APIRouter, status
from fastapi.params import Path

albums_router = APIRouter(prefix="/albums")


@albums_router.get("/{track_id}", status_code=status.HTTP_200_OK)
async def get_one_album(album_id: int = Path()):
    pass


@albums_router.patch("/{album_id}", status_code=status.HTTP_200_OK)
async def update_one_album(album_id: int = Path()):
    pass


@albums_router.delete("/{album_id}", status_code=status.HTTP_200_OK)
async def delete_one_album(album_id: int = Path()):
    pass


@albums_router.get("/", status_code=status.HTTP_200_OK)
async def get_albums_list():
    pass


@albums_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_album():
    pass
