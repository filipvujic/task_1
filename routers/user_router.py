from fastapi import APIRouter
from models.models import User
from sqlalchemy import select
import main


router = APIRouter(tags=["User"], prefix="/user")

@router.get("/get/{first_name_param}")
async def get_all_users(first_name_param: str):
    ### Using where clause.
    user1 = main.session.query(User).where(User.first_name == first_name_param).all()[0]

    ### Using filter.
    user2 = main.session.query(User).filter(User.first_name == first_name_param).all()[0]
    
    #return {"message": user1.to_string()}
    return {"message": user2.to_string()}