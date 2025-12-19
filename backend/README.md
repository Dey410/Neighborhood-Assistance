# 邻里帮（NeighborHelp）后端项目

> 一个基于 **空间位置的邻里互助后端服务**，
>  支持订单发布、附近接单、路径规划与地图能力集成。

------

## 📌 项目简介

**邻里帮（NeighborHelp）** 是一个基于 FastAPI 构建的后端服务，
 面向小区 / 校园等本地化场景，通过 **地理位置 + 距离规则** 实现邻里互助撮合。

项目以 **工程完整性与可演示性** 为目标，具备完整的业务闭环：

> 发布订单 → 附近订单推荐 → 服务者接单 → 路径规划 → 完成订单

------

## ✨ 核心功能

### 🧾 订单系统

- 创建订单（自动记录地理位置）
- 查询用户订单列表
- 附近可接单订单查询（基于距离）
- 服务者接单
- 订单完成（状态机）

### 🧍 服务者系统

- 服务者创建与查询
- 实时位置更新
- 附近服务者搜索
- 服务者位置模拟（用于演示）

### 🗺 地图与空间能力

- 高德地图 API 集成
- 坐标 → 地址逆地理编码
- 服务者 → 订单 路径规划
- 基于 Haversine 公式的距离计算

------

## 🚀 快速开始（推荐方式）

### 1️⃣ 安装依赖

```
pip install -r requirements.txt
```

------

### 2️⃣ 配置环境变量

在项目根目录创建 `.env` 文件：

```
AMAP_KEY=你的高德_KEY
DATABASE_URL=sqlite:///./neighbor_help.db
```

> 💡 本项目默认使用 **SQLite**，无需额外数据库服务，适合课程 / 比赛 / Demo。

------

### 3️⃣ 初始化数据库

```
python init_db.py
python init_data.py
```

- `init_db.py`：创建数据库表（幂等）
- `init_data.py`：插入初始服务者数据（防重复）

------

### 4️⃣ 启动后端服务

#### Windows

```
start.bat
```

#### Linux / macOS

```
sh start.sh
```

启动成功后访问：

- 接口文档（Swagger）：
   👉 http://127.0.0.1:8000/docs
- 健康检查：
   👉 http://127.0.0.1:8000/health

------

## 📚 API 接口概览

### 📦 订单模块 `/api/order`

| 方法 | 接口              | 描述                   |
| ---- | ----------------- | ---------------------- |
| POST | `/create`         | 创建订单               |
| POST | `/accept`         | 服务者接单             |
| GET  | `/nearby`         | 查询附近可接单订单     |
| GET  | `/detail?id=1`    | 查询订单详情（含路线） |
| GET  | `/list?user_id=1` | 查询用户订单列表       |
| PUT  | `/complete/{id}`  | 完成订单               |

**订单状态说明：**

- `0`：待接单
- `1`：已接单
- `2`：已完成

------

### 🧍 服务者模块 `/api/provider`

| 方法 | 接口             | 描述           |
| ---- | ---------------- | -------------- |
| POST | `/create`        | 创建服务者     |
| GET  | `/nearby`        | 查询附近服务者 |
| PUT  | `/location/{id}` | 更新服务者位置 |
| POST | `/simulate/{id}` | 模拟位置漂移   |

------

### 🗺 地图模块 `/api/amap`

| 方法 | 接口               | 描述         |
| ---- | ------------------ | ------------ |
| GET  | `/geocode/reverse` | 坐标 → 地址  |
| GET  | `/route/driving`   | 驾车路线规划 |

------

## 🗂 项目结构

```
backend/
├── app/
│   ├── main.py              # FastAPI 应用入口
│   ├── config.py            # 配置加载
│   ├── database.py          # 数据库连接
│   ├── models/              # ORM 模型
│   ├── schemas/             # 请求 / 响应模型
│   ├── routers/             # API 路由
│   ├── services/            # 业务逻辑
│   └── utils/               # 工具函数（距离计算等）
├── init_db.py               # 数据库初始化
├── init_data.py             # 初始数据插入
├── start.bat                # Windows 启动脚本
├── start.sh                 # Linux/macOS 启动脚本
├── requirements.txt
├── README.md
```

------

## 🧠 技术选型

- **Web 框架**：FastAPI
- **ORM**：SQLAlchemy
- **数据库**：SQLite（MVP / Demo）
- **地图服务**：高德地图 API
- **HTTP 客户端**：requests
- **配置管理**：python-dotenv

------

## 📎 设计说明

- 推荐策略采用 **基于空间距离的规则推荐**
- 优先保证 **实时性、可解释性、稳定性**
- 架构支持后续升级：
  - MySQL / PostgreSQL
  - Redis 缓存
  - 智能调度 / 学习型推荐
