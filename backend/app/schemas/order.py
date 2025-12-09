from pydantic import BaseModel
from typing import Optional

class OrderCreate(BaseModel):
    user_id: int
    desc: str
    address: str
    lat: float
    lng: float

class OrderResponse(BaseModel):
    id: int
    user_id: int
    desc: str
    address: str
    lat: float
    lng: float
    status: int
    provider_id: Optional[int] = None

    class Config:
        from_attributes = True
