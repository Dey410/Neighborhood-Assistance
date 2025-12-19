from app.database import Base, engine
from app.models import order, provider, user

def init_db():
    print(" 正在创建数据库表...")
    Base.metadata.create_all(bind=engine)
    print(" 数据库表创建成功！")

if __name__ == "__main__":
    init_db()
