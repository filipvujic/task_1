from sqlalchemy.orm import Session
from dao.base import BaseDao
from models.models import User
from sqlalchemy import select


### NOT USED FOR NOW
class UserDao(BaseDao):
    def __init__(self, session: Session) -> None:
        super().__init__(session)

    async def create(self, request):
        _user = User(**request.dict())
        self.session.add(_user)
        self.session.commit()
        self.session.refresh(_user)
        return _user

    async def get_by_id(self, user_id: int):
        statement = select(User).where(User.id == user_id)
        return self.session.scalar(statement=statement)

    async def get_by_email(self, email):
        statement = select(User).where(User.email == email)
        return self.session.scalar(statement=statement)

    async def get_all(self):
        statement = select(User).order_by(User.id)
        return self.session.scalars(statement=statement).all()

    async def delete_all(self):
        return await super().delete_all()

    def __init__(self, session: Session) -> None:
        super().__init__(session)
        