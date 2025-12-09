import math

def haversine_distance(lat1, lng1, lat2, lng2):
    """使用 Haversine 公式计算两点间距离（米）"""
    R = 6371000  # 地球半径（米）
    phi1, phi2 = map(math.radians, [lat1, lat2])
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lng2 - lng1)

    a = math.sin(dphi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c
