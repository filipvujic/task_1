from models.models import UserProfile
from database.db_util import DbUtil


async def get_by_id(id_param: str):
    session = DbUtil.get_session()
    ### Using where clause.
    user1 = session.query(UserProfile).where(UserProfile.user_id == id_param).all()[0]

    ### Using filter.
    user2 = session.query(UserProfile).filter(UserProfile.user_id == id_param).all()[0]
    
    #return {"message": user1.to_string()}
    return {"message": user2.to_string()}


async def get_by_email(email_param: str):
    session = DbUtil.get_session()
    ### Using where clause.
    user1 = session.query(UserProfile).where(UserProfile.email == email_param).all()[0]

    ### Using filter.
    user2 = session.query(UserProfile).filter(UserProfile.email == email_param).all()[0]
    
    #return {"message": user1.to_string()}
    return {"message": user2.to_string()}