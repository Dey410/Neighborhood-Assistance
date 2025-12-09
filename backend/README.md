# 邻里帮 后端项目

## 项目简介

基于 FastAPI + SQLAlchemy + MySQL 的位置服务平台，支持订单管理、服务者位置推荐和高德地图集成。

## 功能特性

- 🛒 **订单管理**：创建、查询、更新订单状态
- 👤 **服务者管理**：服务者注册、位置更新、附近搜索
- 🗺️ **地图服务**：高德 API 集成，支持地址逆编码和路线规划
- 📍 **智能推荐**：基于距离的顺路推荐算法
- 🎲 **位置模拟**：服务者位置随机漂移模拟

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 配置环境变量

创建 `.env` 文件：

```env
AMAP_KEY=your_amap_key_here
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/neighbor_help
```

### 数据库初始化

```python
from app.database import engine, Base
from app.models import user, provider, order

# 创建所有表
Base.metadata.create_all(bind=engine)
```

### 启动服务

```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

访问 API 文档：`http://localhost:8000/docs`

## API 文档

### 订单模块 (/api/order)

| 方法 | 端点 | 描述 |
|------|------|------|
| POST | /create | 创建订单 |
| GET | /detail?id=1 | 获取订单详情 |
| GET | /list?user_id=1 | 获取用户订单列表 |
| PUT | /update/{id} | 更新订单状态 |

### 服务者模块 (/api/provider)

| 方法 | 端点 | 描述 |
|------|------|------|
| POST | /create | 创建服务者 |
| GET | /nearby?lat=39.9&lng=116.4 | 搜索附近服务者 |
| GET | /location?id=1 | 获取服务者位置 |
| GET | /{id} | 获取服务者信息 |
| PUT | /location/{id} | 更新服务者位置 |
| POST | /simulate/{id} | 模拟服务者位置漂移 |

### 高德地图模块 (/api/amap)

| 方法 | 端点 | 描述 |
|------|------|------|
| GET | /geocode/reverse?lat=39.9&lng=116.4 | 坐标转地址 |
| GET | /route/driving?origin_lng=116.4&origin_lat=39.9&dest_lng=116.5&dest_lat=40.0 | 驾车路线规划 |

## 项目结构

```
backend/
├── app/
│   ├── main.py              # 项目入口
│   ├── config.py            # 配置文件
│   ├── database.py          # 数据库配置
│   ├── models/              # ORM 模型
│   │   ├── user.py
│   │   ├── provider.py
│   │   ├── order.py
│   │   └── __init__.py
│   ├── schemas/             # Pydantic 模型
│   │   ├── user.py
│   │   ├── provider.py
│   │   ├── order.py
│   │   └── __init__.py
│   ├── routers/             # 路由模块
│   │   ├── order.py
│   │   ├── provider.py
│   │   ├── amap.py
│   │   └── __init__.py
│   ├── services/            # 业务逻辑
│   │   ├── amap_service.py
│   │   ├── recommend_service.py
│   │   ├── location_simulator.py
│   │   └── __init__.py
│   └── utils/               # 工具函数
│       ├── distance.py
│       └── __init__.py
├── requirements.txt
└── README.md
```

## 技术栈

- **框架**：FastAPI
- **ORM**：SQLAlchemy
- **数据库**：MySQL
- **API 调用**：requests
- **地图服务**：高德地图

## 开发建议

1. 确保已安装 MySQL 并创建 `neighbor_help` 数据库
2. 获取[高德开发者 Key](https://lbs.amap.com/dev/key/app)
3. 开发时使用 SQLite 可以快速测试，配置 `DATABASE_URL=sqlite:///./neighbor_help.db`
4. 添加数据库迁移工具（如 Alembic）便于版本管理

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT
