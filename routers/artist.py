from fastapi import APIRouter

router = APIRouter()

@router.get("/names")
async def get_artist_names():
    return {"names: " : "Artist Names Here..."}