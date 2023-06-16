from models.models import UserProfile
import main


async def get_by_id(id_param: str):
    ### Using where clause.
    user1 = main.session.query(UserProfile).where(UserProfile.user_id == id_param).all()[0]

    ### Using filter.
    user2 = main.session.query(UserProfile).filter(UserProfile.user_id == id_param).all()[0]
    
    #return {"message": user1.to_string()}
    return {"message": user2.to_string()}


async def get_by_email(email_param: str):
    ### Using where clause.
    user1 = main.session.query(UserProfile).where(UserProfile.email == email_param).all()[0]

    ### Using filter.
    user2 = main.session.query(UserProfile).filter(UserProfile.email == email_param).all()[0]
    
    #return {"message": user1.to_string()}
    return {"message": user2.to_string()}