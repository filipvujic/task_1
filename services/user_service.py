from models.models import User
from database.db_util import DbUtil
from sqlalchemy import delete


async def get_by_id(id_param: str):
    session = DbUtil.get_session()
    ### Using where clause.
    user1 = session.query(User).where(User.id == id_param).all()[0]

    ### Using filter.
    user2 = session.query(User).filter(User.id == id_param).all()[0]
    
    #return {"message": user1.to_string()}
    return {"message": user2.to_string()}

async def delete_by_id(id_param: str):
    session = DbUtil.get_session()

    ### Using filter.
    user1 = session.query(User).filter(User.id == id_param).all()[0]

    statement = delete(User).where(User.id == user1.id)
    session.execute(statement=statement)
    session.commit()
    
    return {"message": f"Deleted user: {user1.to_string()}" }