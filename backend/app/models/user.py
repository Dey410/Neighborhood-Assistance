from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    phone = Column(String(20), unique=True)
    avatar = Column(String(255), nullable=True)
