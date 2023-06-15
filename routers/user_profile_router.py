from fastapi import APIRouter


router = APIRouter(tags=["UserProfile"], prefix="/user_profile")

@router.get("/get")
async def login():
    return {"message": "Hello User Profiles"}