from models.models import User
from db_util import DbUtil


async def get_by_id(id_param: str):
    session = DbUtil.get_session()
    ### Using where clause.
    user1 = session.query(User).where(User.id == id_param).all()[0]

    ### Using filter.
    user2 = session.query(User).filter(User.id == id_param).all()[0]
    
    #return {"message": user1.to_string()}
    return {"message": user2.to_string()}