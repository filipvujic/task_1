from fastapi import APIRouter


router = APIRouter(tags=["Pet"], prefix="/pet")

@router.get("/get")
async def login():
    return {"message": "Hello Pets"}