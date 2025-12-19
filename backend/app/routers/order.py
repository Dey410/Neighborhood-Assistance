from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.order import Order
from app.models.provider import Provider
from app.schemas.order import OrderCreate, OrderAccept
from app.services.amap_service import amap_route
from app.utils.distance import haversine_distance

router = APIRouter(tags=["订单 Order"])

# ============================================================
# 数据库会话依赖
# ============================================================

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ============================================================
# 订单创建
# ============================================================

@router.post("/create")
def create_order(data: OrderCreate, db: Session = Depends(get_db)):
    """
    创建新订单
    初始状态：status = 0（待接单）
    """
    new_order = Order(
        user_id=data.userId,
        desc=data.desc,
        address=data.address,
        lat=data.lat,
        lng=data.lng,
        status=0
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return {
        "orderId": new_order.id,
        "status": "success"
    }

# ============================================================
# 服务者接单
# ============================================================

@router.post("/accept")
def accept_order(data: OrderAccept, db: Session = Depends(get_db)):
    """
    服务者接单
    status: 0 → 1
    """
    order = db.query(Order).filter(Order.id == data.orderId).first()
    if not order:
        return {"error": "订单不存在"}

    if order.status != 0:
        return {
            "error": "订单状态不允许接单",
            "current_status": order.status
        }

    order.provider_id = data.providerId
    order.status = 1
    db.commit()

    return {"message": "接单成功"}

# ============================================================
# 查询附近可接单订单
# ============================================================

@router.get("/nearby")
def nearby_orders(
    lat: float,
    lng: float,
    radius: int = 1000,
    db: Session = Depends(get_db)
):
    """
    查询附近可接单订单（status = 0）
    以服务者当前位置为中心
    """
    orders = db.query(Order).filter(Order.status == 0).all()
    results = []

    for o in orders:
        distance = haversine_distance(lat, lng, o.lat, o.lng)
        if distance <= radius:
            results.append({
                "order_id": o.id,
                "desc": o.desc,
                "address": o.address,
                "lat": o.lat,
                "lng": o.lng,
                "distance": int(distance),
                "created_at": o.created_at
            })

    results.sort(key=lambda x: x["distance"])

    return {
        "count": len(results),
        "orders": results
    }

# ============================================================
# 订单详情（含路线规划）
# ============================================================

@router.get("/detail")
def order_detail(id: int, db: Session = Depends(get_db)):
    """
    获取订单详情
    若已接单，返回服务者信息和路线规划
    """
    order = db.query(Order).filter(Order.id == id).first()
    if not order:
        return {"error": "订单不存在"}

    provider = None
    route = None

    if order.provider_id:
        provider = db.query(Provider).filter(Provider.id == order.provider_id).first()
        if provider:
            route = amap_route(
                provider.lng, provider.lat,
                order.lng, order.lat
            )

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
        "provider": {
            "id": provider.id,
            "name": provider.name,
            "lat": provider.lat,
            "lng": provider.lng
        } if provider else None,
        "route": route
    }

# ============================================================
# 用户订单列表
# ============================================================

@router.get("/list")
def order_list(user_id: int, db: Session = Depends(get_db)):
    """
    获取用户订单列表
    """
    orders = db.query(Order).filter(Order.user_id == user_id).all()
    return {
        "orders": orders,
        "total": len(orders)
    }

# ============================================================
# 完成订单
# ============================================================

@router.put("/complete/{id}")
def complete_order(id: int, db: Session = Depends(get_db)):
    """
    完成订单
    status: 1 → 2
    """
    order = db.query(Order).filter(Order.id == id).first()
    if not order:
        return {"error": "订单不存在"}

    if order.status != 1:
        return {
            "error": "订单状态不允许完成",
            "current_status": order.status
        }

    order.status = 2
    db.commit()

    return {
        "message": "订单已完成",
        "order_id": order.id,
        "status": order.status
    }
