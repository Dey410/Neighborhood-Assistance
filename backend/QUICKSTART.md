快速开始指南 - 邻里帮后端项目
================================

## 📦 项目已完成文件列表

backend/
├── app/
│   ├── __init__.py
│   ├── main.py                    ✅ 项目入口
│   ├── config.py                  ✅ 配置文件
│   ├── database.py                ✅ 数据库配置
│   │
│   ├── models/                    ✅ 数据模型
│   │   ├── user.py
│   │   ├── provider.py
│   │   ├── order.py
│   │   └── __init__.py
│   │
│   ├── schemas/                   ✅ 请求/响应模型
│   │   ├── user.py
│   │   ├── provider.py
│   │   ├── order.py
│   │   └── __init__.py
│   │
│   ├── routers/                   ✅ API 路由
│   │   ├── order.py               - 订单管理 API
│   │   ├── provider.py            - 服务者管理 API
│   │   ├── amap.py                - 高德地图 API
│   │   └── __init__.py
│   │
│   ├── services/                  ✅ 业务逻辑
│   │   ├── amap_service.py        - 高德 API 调用
│   │   ├── location_simulator.py  - 位置模拟
│   │   ├── recommend_service.py   - 顺路推荐
│   │   └── __init__.py
│   │
│   └── utils/                     ✅ 工具函数
│       ├── distance.py            - Haversine 距离计算
│       └── __init__.py
│
├── init_db.py                     ✅ 数据库初始化脚本
├── test_api.py                    ✅ API 测试脚本
├── start.bat                      ✅ Windows 启动脚本
├── start.sh                       ✅ Linux/Mac 启动脚本
├── requirements.txt               ✅ 项目依赖
├── .env.example                   ✅ 环境变量示例
└── README.md                      ✅ 项目文档

## 🚀 快速启动步骤

### 步骤 1: 配置环境变量

复制 `.env.example` 为 `.env`：

Windows (PowerShell):
  Copy-Item .env.example -Destination .env

Linux/Mac:
  cp .env.example .env

编辑 `.env` 文件：
  AMAP_KEY=your_amap_key_here
  DATABASE_URL=mysql+pymysql://root:password@localhost:3306/neighbor_help

### 步骤 2: 安装依赖

pip install -r requirements.txt

### 步骤 3: 初始化数据库

python init_db.py

或使用启动脚本（包含自动初始化）：
  Windows: start.bat
  Linux/Mac: bash start.sh

### 步骤 4: 启动服务

#### 方式 1: 使用启动脚本（推荐）

Windows:
  start.bat

Linux/Mac:
  bash start.sh

#### 方式 2: 手动启动

python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

### 步骤 5: 访问 API

打开浏览器访问：
  http://localhost:8000/docs

即可看到完整的 API 文档（Swagger UI）

## 📝 测试 API

运行测试脚本（需要先启动服务）：

python test_api.py

## 🔌 核心 API 端点

### 订单 API
POST   /api/order/create              - 创建订单
GET    /api/order/detail?id=1         - 获取订单详情
GET    /api/order/list?user_id=1      - 获取订单列表
PUT    /api/order/update/1            - 更新订单状态

### 服务者 API
POST   /api/provider/create           - 创建服务者
GET    /api/provider/nearby           - 搜索附近服务者
GET    /api/provider/{id}             - 获取服务者信息
PUT    /api/provider/location/{id}    - 更新位置
GET    /api/provider/location?id=1    - 获取当前位置
POST   /api/provider/simulate/{id}    - 模拟位置变化

### 高德地图 API
GET    /api/amap/geocode/reverse      - 坐标转地址
GET    /api/amap/route/driving        - 驾车路线规划

## 💡 项目特点

✨ 完整的 MVP 实现
✨ 代码极简，便于学习和扩展
✨ 包含完整的 API 文档
✨ 支持位置模拟和推荐算法
✨ 高德地图集成
✨ SQLAlchemy ORM 封装
✨ Pydantic 数据验证
✨ CORS 跨域配置
✨ 自动化启动脚本

## 🔧 主要技术栈

- FastAPI: 高性能 Web 框架
- SQLAlchemy: ORM 框架
- MySQL: 关系数据库
- Pydantic: 数据验证
- Uvicorn: ASGI 服务器
- Requests: HTTP 客户端
- Python-dotenv: 环境变量管理

## 📚 数据库表结构

### user 表
id (PK), name, phone, avatar

### provider 表
id (PK), name, avatar, lat, lng, base_lat, base_lng

### order 表
id (PK), user_id, provider_id (FK), desc, address, lat, lng, status

## ⚠️ 注意事项

1. 确保已安装 MySQL 并创建 neighbor_help 数据库
2. 获取高德地图 API Key：https://lbs.amap.com/dev/key/app
3. 修改 .env 中的数据库连接字符串
4. 开发时可使用 SQLite 快速测试
5. 生产环境需配置日志、异常处理等

## 🎯 下一步

1. 补充数据库迁移工具（Alembic）
2. 添加用户认证（JWT）
3. 完善错误处理和日志
4. 添加单元测试
5. 前端集成
6. 性能优化和缓存

## 📖 更多帮助

查看 README.md 获取完整文档
访问 http://localhost:8000/docs 查看 API 文档

祝你使用愉快！ 🎉
