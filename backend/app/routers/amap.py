from fastapi import APIRouter
from app.services.amap_service import amap_reverse_geocode, amap_route

router = APIRouter()

@router.get("/geocode/reverse")
def reverse_geocode(lat: float, lng: float):
    """高德逆地理编码：坐标转地址"""
    result = amap_reverse_geocode(lat, lng)
    return result

@router.get("/route/driving")
def get_route(origin_lng: float, origin_lat: float, dest_lng: float, dest_lat: float):
    """高德驾车路线规划"""
    result = amap_route(origin_lng, origin_lat, dest_lng, dest_lat)
    return result
