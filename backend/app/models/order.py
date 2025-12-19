from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    
    user_id = Column(Integer, nullable=False)
    desc = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)

    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)

    provider_id = Column(Integer, ForeignKey("providers.id"), nullable=True)

    status = Column(Integer, default=0)  # 0=待接单, 1=已接单

    created_at = Column(DateTime, server_default=func.now())
