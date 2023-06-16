from models.models import User
import main


async def get_by_id(id_param: str):
    ### Using where clause.
    user1 = main.session.query(User).where(User.id == id_param).all()[0]

    ### Using filter.
    user2 = main.session.query(User).filter(User.id == id_param).all()[0]
    
    #return {"message": user1.to_string()}
    return {"message": user2.to_string()}