from pydantic import BaseModel


class UserLoginDTO(BaseModel):
    email: str
    password: str


class UserRegisterDTO(BaseModel):
    username: str
    email: str
    password: str


class UserDTO(BaseModel):
    id: int
    username: str
    email: str
