from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    username: str = Field(unique=True)
    email: str = Field(unique=True)
    is_deleted: bool = Field(default=False, index=True)


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=16)


class UserRead(UserBase):
    id: int


class UserUpdate(UserBase):
    password: str
    is_deleted: bool
