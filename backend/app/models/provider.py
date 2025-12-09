from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Provider(Base):
    __tablename__ = "provider"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    avatar = Column(String(255))
    lat = Column(Float)       # 当前纬度
    lng = Column(Float)       # 当前经度
    base_lat = Column(Float)  # 活动区域纬度
    base_lng = Column(Float)  # 活动区域经度
