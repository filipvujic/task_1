from database.db_util import DbUtil
from dao.user_dao import UserDao
from models.models import User
from schemas.user import UserBase, UserUpdate

async def create(user: UserBase):
    session = DbUtil.get_session()
    await UserDao(session).create(user)
    return {"message": f"Created user: {user}" }


async def get_by_id(id_param: str):
    session = DbUtil.get_session()
    ### Using where clause.
    #user = session.query(User).where(User.id == id_param).all()[0]

    ### Using filter.
    #user = session.query(User).filter(User.id == id_param).all()[0]
    
    ### Using DAO class.
    user = await UserDao(session).get_by_id(id_param)
    #return {"message": user1.to_string()}
    return {"message": user.to_string()}

async def update(user: UserUpdate):
    session = DbUtil.get_session()
    await UserDao(session).update(user)
    return {"message": f"Created user: {user}" }

async def delete_by_id(id_param: str):
    session = DbUtil.get_session()

    ### Using filter.
    #user = session.query(User).filter(User.id == id_param).all()[0]
    user = await get_by_id(id_param)
    await UserDao(session).delete_by_id(id_param)

    return {"message": f"Deleted user: {user}" }

