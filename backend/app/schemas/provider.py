from pydantic import BaseModel

class ProviderCreate(BaseModel):
    name: str
    avatar: str
    lat: float
    lng: float
    base_lat: float
    base_lng: float

class ProviderResponse(BaseModel):
    id: int
    name: str
    avatar: str
    lat: float
    lng: float

    class Config:
        from_attributes = True
