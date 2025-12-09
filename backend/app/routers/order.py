from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.order import Order
from app.models.provider import Provider
from app.schemas.order import OrderCreate, OrderResponse
from app.services.amap_service import amap_route

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create", response_model=dict)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    """创建新订单"""
    new_order = Order(
        user_id=order.user_id,
        desc=order.desc,
        address=order.address,
        lat=order.lat,
        lng=order.lng,
        status=0
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return {"orderId": new_order.id, "status": "success"}

@router.get("/detail")
def order_detail(id: int, db: Session = Depends(get_db)):
    """获取订单详情"""
    order = db.query(Order).filter(Order.id == id).first()
    if not order:
        return {"error": "Order not found"}
    
    provider = None
    route = None
    if order.provider_id:
        provider = db.query(Provider).filter(Provider.id == order.provider_id).first()
        if provider:
            route = amap_route(provider.lng, provider.lat, order.lng, order.lat)

    return {
        "order": {
            "id": order.id,
            "user_id": order.user_id,
            "desc": order.desc,
            "address": order.address,
            "lat": order.lat,
            "lng": order.lng,
            "status": order.status,
            "provider_id": order.provider_id
        },
        "provider": provider,
        "route": route
    }

@router.get("/list")
def order_list(user_id: int, db: Session = Depends(get_db)):
    """获取用户订单列表"""
    orders = db.query(Order).filter(Order.user_id == user_id).all()
    return {"orders": orders, "total": len(orders)}

@router.put("/update/{id}")
def update_order(id: int, status: int, provider_id: int = None, db: Session = Depends(get_db)):
    """更新订单状态"""
    order = db.query(Order).filter(Order.id == id).first()
    if not order:
        return {"error": "Order not found"}
    
    order.status = status
    if provider_id:
        order.provider_id = provider_id
    
    db.commit()
    return {"message": "Order updated successfully"}
