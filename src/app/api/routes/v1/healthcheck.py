from fastapi import APIRouter, status, Response

healthcheck_router = APIRouter()




@healthcheck_router.get(
    "/healthcheck",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {},
    },
    tags=["Healthcheck"],
)
async def healthcheck():
    return Response(status_code=status.HTTP_200_OK)
