from fastapi import APIRouter, Response, status

healthcheck_router = APIRouter()


@healthcheck_router.get(
    "/healthcheck",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
    },
)
async def healthcheck():
    return Response(status_code=status.HTTP_200_OK)
