from fastapi import APIRouter
from services import user_service


router = APIRouter(tags=["User"], prefix="/user")

@router.get("/get-by-id/{id_param}")
async def get_by_id(id_param: str):
    return await user_service.get_by_id(id_param=id_param)