from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1",
    tags=["items"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/items/", tags=["items"])
async def read_items():
    return [{"item": "Lemari"}, {"item": "Meja"}]