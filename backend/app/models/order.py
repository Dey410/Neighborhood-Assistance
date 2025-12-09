from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base

class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    provider_id = Column(Integer, ForeignKey("provider.id"), nullable=True)
    desc = Column(String(255))
    address = Column(String(255))
    lat = Column(Float)
    lng = Column(Float)
    status = Column(Integer, default=0)  # 0待接单,1服务中,2完成
