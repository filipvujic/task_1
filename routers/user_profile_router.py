from fastapi import APIRouter
from services import user_profile_service


router = APIRouter(tags=["UserProfile"], prefix="/user-profile")

@router.get("/get")
async def login():
    return {"message": "Hello User Profiles"}

@router.get("/get-by-id/{id_param}")
async def get_all_users(id_param: str):
    return await user_profile_service.get_by_id(id_param=id_param)

@router.get("/get-by-email/{email_param}")
async def get_all_users(email_param: str):
    return await user_profile_service.get_by_email(email_param=email_param)