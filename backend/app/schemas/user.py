from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    phone: str
    avatar: str = None

class UserResponse(BaseModel):
    id: int
    name: str
    phone: str
    avatar: str = None

    class Config:
        from_attributes = True
