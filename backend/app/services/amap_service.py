import requests
from app.config import AMAP_KEY

def amap_reverse_geocode(lat, lng):
    """高德地址逆编码：根据坐标获取地址"""
    url = "https://restapi.amap.com/v3/geocode/regeo"
    params = {"key": AMAP_KEY, "location": f"{lng},{lat}"}
    try:
        return requests.get(url, params=params, timeout=5).json()
    except Exception as e:
        return {"error": str(e)}

def amap_route(origin_lng, origin_lat, dest_lng, dest_lat):
    """高德驾车路线规划"""
    url = "https://restapi.amap.com/v5/direction/driving"
    params = {
        "key": AMAP_KEY,
        "origin": f"{origin_lng},{origin_lat}",
        "destination": f"{dest_lng},{dest_lat}",
    }
    try:
        return requests.get(url, params=params, timeout=5).json()
    except Exception as e:
        return {"error": str(e)}
