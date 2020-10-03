from pydantic import BaseModel, constr, conint


class UserBase(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    name: str
    password: str
