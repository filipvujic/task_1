from sqlalchemy.orm import Session
from dao.base import BaseDao
from models.models import User, UserProfile
from sqlalchemy import select, delete, update


class UserDao(BaseDao):
    def __init__(self, session: Session) -> None:
        super().__init__(session)

    async def create(self, request):
        user = User(**request.dict())
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    async def get_by_id(self, user_id: int):
        statement = select(User).where(User.id == user_id)
        return self.session.scalar(statement=statement)

    async def get_by_email(self, email):
        statement = select(User).where(User.email == email)
        return self.session.scalar(statement=statement)

    async def get_all(self):
        statement = select(User).order_by(User.id)
        return self.session.scalars(statement=statement).all()

    async def update(self, request):
        req_dict: dict = request.dict()
        user_id = req_dict.pop("id")
        user = await self.get_by_id(user_id)
        email = req_dict.pop("email")
        
        ### Update user table.
        statement = update(User).where(User.id == user_id).values(req_dict)
        self.session.execute(statement)
        
        ### Update user profile table.
        statement = update(UserProfile).where(UserProfile.user_id == user.id).values(email=email)
        self.session.execute(statement)
        self.session.commit()

        #self.session.refresh(user)

    async def delete_all(self):
        return await super().delete_all()
    
    async def delete_by_id(self, id_param: int):
        statement = delete(User).where(User.id == id_param)
        self.session.execute(statement=statement)
        self.session.commit()
    
    def __init__(self, session: Session) -> None:
        super().__init__(session)
        