from app.utils.distance import haversine_distance

def is_recommended(provider, order_lat, order_lng, threshold=1000):
    """简单顺路推荐算法：距离 < 1km 就推荐"""
    dist = haversine_distance(provider.lat, provider.lng, order_lat, order_lng)
    return dist < threshold
