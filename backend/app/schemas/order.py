from pydantic import BaseModel

class OrderCreate(BaseModel):
    userId: int
    desc: str
    address: str
    lat: float
    lng: float

class OrderAccept(BaseModel):
    orderId: int
    providerId: int
