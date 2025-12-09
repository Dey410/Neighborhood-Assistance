"""
测试脚本 - 快速测试 API
"""

import requests
import json

BASE_URL = "http://localhost:8000/api"

def test_create_provider():
    """测试创建服务者"""
    url = f"{BASE_URL}/provider/create"
    data = {
        "name": "张三",
        "avatar": "https://example.com/avatar.jpg",
        "lat": 39.9042,
        "lng": 116.4074,
        "base_lat": 39.9000,
        "base_lng": 116.4000
    }
    response = requests.post(url, json=data)
    print(f"创建服务者: {response.json()}")
    return response.json().get("providerId")

def test_create_order():
    """测试创建订单"""
    url = f"{BASE_URL}/order/create"
    data = {
        "user_id": 1,
        "desc": "帮我买菜",
        "address": "北京市朝阳区建国路",
        "lat": 39.9155,
        "lng": 116.4345
    }
    response = requests.post(url, json=data)
    print(f"创建订单: {response.json()}")
    return response.json().get("orderId")

def test_nearby_providers():
    """测试搜索附近服务者"""
    url = f"{BASE_URL}/provider/nearby?lat=39.9155&lng=116.4345"
    response = requests.get(url)
    print(f"附近服务者: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")

def test_order_detail(order_id):
    """测试获取订单详情"""
    url = f"{BASE_URL}/order/detail?id={order_id}"
    response = requests.get(url)
    print(f"订单详情: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")

if __name__ == "__main__":
    print("=" * 50)
    print("邻里帮 后端 API 测试")
    print("=" * 50)
    
    try:
        # 测试创建服务者
        provider_id = test_create_provider()
        
        # 测试创建订单
        order_id = test_create_order()
        
        # 测试搜索附近服务者
        print("\n" + "=" * 50)
        test_nearby_providers()
        
        # 测试订单详情
        print("\n" + "=" * 50)
        test_order_detail(order_id)
        
        print("\n" + "=" * 50)
        print("✅ 所有测试完成！")
        
    except Exception as e:
        print(f"❌ 错误: {str(e)}")
        print("请确保服务已启动: python -m uvicorn app.main:app --reload")
