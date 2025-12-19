from app.database import SessionLocal
from app.models.provider import Provider

def insert_providers():
    db = SessionLocal()

    # 如果已有数据，就不再插入
    exists = db.query(Provider).first()
    if exists:
        print("服务者数据已存在，跳过初始化")
        db.close()
        return

    providers = [
        Provider(name="张三", lat=39.9101, lng=116.4039, base_lat=39.9101, base_lng=116.4039),
        Provider(name="李四", lat=39.9155, lng=116.4080, base_lat=39.9155, base_lng=116.4080),
        Provider(name="王五", lat=39.9180, lng=116.4120, base_lat=39.9180, base_lng=116.4120),
    ]

    db.add_all(providers)
    db.commit()
    db.close()

    print("🎉 初始服务者数据插入成功！")

if __name__ == "__main__":
    insert_providers()
