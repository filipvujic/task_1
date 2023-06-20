from pydantic import BaseModel, validator

# class UserBase(BaseModel):
#     email: str | None
#     first_name: str | None
#     last_name: str | None

class UserCreation(BaseModel):

    first_name: str | None
    last_name: str | None
    dob: str | None
    email: str

    @validator("email", check_fields=False)
    def email_valid(cls, value):
        if not value:
            raise ValueError("Email field can't be blank!!!")
        return value
    
    @validator("first_name", check_fields=False)
    def first_name_valid(cls, value):
        import string
        if any(p in value for p in string.punctuation):
            raise ValueError("First name should not contain punctuation.")
        else:
            return value
        
class UserUpdate(UserCreation):

    id: int