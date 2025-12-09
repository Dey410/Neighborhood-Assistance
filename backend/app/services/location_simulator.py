import random

def simulate_movement(lat, lng):
    """随机模拟位置漂移"""
    lat += (random.random() - 0.5) * 0.0001
    lng += (random.random() - 0.5) * 0.0001
    return lat, lng
