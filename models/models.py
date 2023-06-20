from typing import List
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from database.db_util import Base
from schemas import user as userschema


class User(Base):
    
    __tablename__ = "user"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    first_name = Column("firstname", String)
    last_name = Column("lastname", String)
    dob = Column("date_of_birth", Date)
    user_profile: Mapped["UserProfile"] = relationship()

    def __init__(self, first_name, last_name, dob, email):
        #self.first_name = first_name
        self.first_name = userschema.UserCreation.first_name_valid(first_name)
        self.last_name = last_name
        self.dob = dob
        self.user_profile = UserProfile(email)

    def to_string(self):
        return f"ID: {self.id}, Name: {self.first_name}, Surname: {self.last_name}, DOB: {self.dob}, Email: {self.user_profile.email}"


class UserProfile(Base):
    __tablename__ = "user_profile"
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="cascade"), primary_key=True)
    user: Mapped["User"] = relationship(back_populates="user_profile")
    email =Column("email", String)
    company = Column("company", String)
    pets: Mapped[List["Pet"]] = relationship(back_populates="owner")

    def __init__(self, email):
        super().__init__()
        #self.email = email
        self.email = userschema.UserCreation.email_valid(email)
        self.company = "Qcerris"
    
    def to_string(self):
        return f"ID: {self.user_id}, Email: {self.email}, Company: {self.company}, Pets: {self.pets}"


class Pet(Base):
    __tablename__ = "pet"
    id = mapped_column("id", Integer, primary_key=True, autoincrement=True)
    type = Column("type", String)
    name = mapped_column("name", String)
    age = Column("age", Integer)
    owner_id: Mapped[int] = mapped_column(ForeignKey("user_profile.user_id", ondelete="cascade"))
    owner: Mapped["UserProfile"] = relationship(back_populates="pets")
    
    def __init__(self, type, name, age, owner: UserProfile):
        self.type = type
        self.name = name
        self.age = age
        self.owner = owner