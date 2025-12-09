from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.provider import Provider
from app.models.order import Order
from app.schemas.provider import ProviderCreate, ProviderResponse
from app.utils.distance import haversine_distance
from app.services.recommend_service import is_recommended
from app.services.location_simulator import simulate_movement

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create", response_model=dict)
def create_provider(provider: ProviderCreate, db: Session = Depends(get_db)):
    """创建服务者"""
    new_provider = Provider(
        name=provider.name,
        avatar=provider.avatar,
        lat=provider.lat,
        lng=provider.lng,
        base_lat=provider.base_lat,
        base_lng=provider.base_lng
    )
    db.add(new_provider)
    db.commit()
    db.refresh(new_provider)
    return {"providerId": new_provider.id, "status": "success"}

@router.get("/nearby")
def nearby(lat: float, lng: float, db: Session = Depends(get_db)):
    """获取附近的服务者"""
    providers = db.query(Provider).all()
    results = []

    for p in providers:
        distance = haversine_distance(lat, lng, p.lat, p.lng)
        recommended = is_recommended(p, lat, lng)
        results.append({
            "id": p.id,
            "name": p.name,
            "avatar": p.avatar,
            "lat": p.lat,
            "lng": p.lng,
            "distance": int(distance),
            "isRecommended": recommended
        })

    results.sort(key=lambda x: x["distance"])
    return {"providers": results}

@router.get("/location")
def get_location(id: int, db: Session = Depends(get_db)):
    """获取服务者当前位置"""
    p = db.query(Provider).filter(Provider.id == id).first()
    if not p:
        return {"error": "Provider not found"}
    return {"lat": p.lat, "lng": p.lng}

@router.get("/{id}")
def get_provider(id: int, db: Session = Depends(get_db)):
    """获取服务者信息"""
    p = db.query(Provider).filter(Provider.id == id).first()
    if not p:
        return {"error": "Provider not found"}
    
    return {
        "id": p.id,
        "name": p.name,
        "avatar": p.avatar,
        "lat": p.lat,
        "lng": p.lng,
        "base_lat": p.base_lat,
        "base_lng": p.base_lng
    }

@router.put("/location/{id}")
def update_location(id: int, lat: float, lng: float, db: Session = Depends(get_db)):
    """更新服务者位置"""
    p = db.query(Provider).filter(Provider.id == id).first()
    if not p:
        return {"error": "Provider not found"}
    
    p.lat = lat
    p.lng = lng
    db.commit()
    return {"message": "Location updated"}

@router.post("/simulate/{id}")
def simulate_location(id: int, db: Session = Depends(get_db)):
    """模拟服务者位置变化"""
    p = db.query(Provider).filter(Provider.id == id).first()
    if not p:
        return {"error": "Provider not found"}
    
    new_lat, new_lng = simulate_movement(p.lat, p.lng)
    p.lat = new_lat
    p.lng = new_lng
    db.commit()
    return {"lat": new_lat, "lng": new_lng}
