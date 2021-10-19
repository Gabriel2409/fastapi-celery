from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    """Hello world"""
    return {"message": "Hello World"}
