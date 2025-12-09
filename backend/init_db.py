"""
数据库初始化脚本
运行此脚本创建所有数据库表
"""

from app.database import engine, Base
from app.models.user import User
from app.models.provider import Provider
from app.models.order import Order

def init_db():
    """创建所有数据库表"""
    Base.metadata.create_all(bind=engine)
    print("✅ 数据库表创建成功！")

if __name__ == "__main__":
    init_db()
