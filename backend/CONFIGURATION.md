"""
邻里帮后端项目配置指南
========================

本文件包含了项目的完整配置说明和使用指南。
"""

# ============================================================
# 1. MySQL 数据库配置
# ============================================================

"""
首先需要安装 MySQL 并创建数据库。

Windows 用户：
  1. 下载 MySQL 社区版：https://dev.mysql.com/downloads/mysql/
  2. 运行安装程序，记住密码
  3. 打开命令行，执行：
     mysql -u root -p
  4. 输入密码后，执行：
     CREATE DATABASE neighbor_help DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

Linux/Mac 用户：
  brew install mysql  (Mac)
  sudo apt-get install mysql-server  (Linux)
  
  mysql -u root -p
  CREATE DATABASE neighbor_help DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
"""

# ============================================================
# 2. 高德地图 API Key 配置
# ============================================================

"""
获取高德 API Key：
  1. 访问 https://lbs.amap.com/dev/key/app
  2. 注册或登录高德开放平台账号
  3. 创建新应用，获取 Web 服务 API Key
  4. 复制 Key 到 .env 文件中

注意：高德 API 有免费配额限制，生产环境需考虑成本。
"""

# ============================================================
# 3. 环境变量配置
# ============================================================

"""
编辑 .env 文件，配置以下变量：

AMAP_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/neighbor_help

其中：
  - AMAP_KEY: 你的高德 API Key
  - DATABASE_URL: MySQL 数据库连接字符串
    格式: mysql+pymysql://用户名:密码@主机:端口/数据库名

数据库 URL 组成说明：
  mysql+pymysql：驱动程序
  root：MySQL 用户名
  password：MySQL 密码
  localhost：数据库主机
  3306：MySQL 默认端口
  neighbor_help：数据库名
"""

# ============================================================
# 4. Python 虚拟环境配置（可选但推荐）
# ============================================================

"""
创建虚拟环境可以避免包冲突。

Windows:
  python -m venv venv
  venv\Scripts\activate

Linux/Mac:
  python3 -m venv venv
  source venv/bin/activate

激活虚拟环境后，再运行：
  pip install -r requirements.txt
"""

# ============================================================
# 5. 项目依赖详解
# ============================================================

"""
requirements.txt 中的包：

fastapi>=0.68.0
  - 现代化的 Python Web 框架
  - 自动 API 文档生成
  - 类型提示支持

uvicorn[standard]>=0.15.0
  - ASGI 服务器
  - 用于运行 FastAPI 应用

SQLAlchemy>=1.4.0
  - Python ORM 框架
  - 支持多种数据库
  - 提供面向对象的数据库操作

pymysql>=1.0.2
  - Python MySQL 驱动
  - 与 SQLAlchemy 配合使用

requests>=2.26.0
  - HTTP 请求库
  - 调用高德 API 时使用

python-dotenv>=0.19.0
  - 环境变量管理
  - 从 .env 文件读取配置

pydantic>=1.8.0
  - 数据验证和序列化
  - 自动生成 JSON schema
"""

# ============================================================
# 6. 数据库初始化
# ============================================================

"""
初始化数据库有两种方式：

方式 1：使用脚本
  python init_db.py

方式 2：手动初始化
  python
  >>> from app.database import engine, Base
  >>> from app.models.user import User
  >>> from app.models.provider import Provider
  >>> from app.models.order import Order
  >>> Base.metadata.create_all(bind=engine)
  >>> exit()

脚本会根据 models 中的定义自动创建所有表。
"""

# ============================================================
# 7. 服务启动
# ============================================================

"""
启动 FastAPI 服务：

基本启动：
  python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

参数说明：
  --reload：代码改动时自动重启（仅开发环境）
  --host：绑定地址（0.0.0.0 表示所有网络接口）
  --port：监听端口（默认 8000）

生产环境启动（不使用 reload）：
  python -m uvicorn app.main:app --host 0.0.0.0 --port 8000

使用启动脚本（推荐）：
  Windows: start.bat
  Linux/Mac: bash start.sh
"""

# ============================================================
# 8. API 文档访问
# ============================================================

"""
启动服务后，可以通过以下地址访问 API 文档：

Swagger UI（推荐）：
  http://localhost:8000/docs

ReDoc（备选）：
  http://localhost:8000/redoc

这些文档由 FastAPI 自动生成，可以直接测试 API。
"""

# ============================================================
# 9. 测试 API
# ============================================================

"""
运行测试脚本（需要先启动服务）：
  python test_api.py

或使用 curl 命令测试：

1. 创建服务者
  curl -X POST http://localhost:8000/api/provider/create \
    -H "Content-Type: application/json" \
    -d '{
      "name": "张三",
      "avatar": "https://example.com/avatar.jpg",
      "lat": 39.9042,
      "lng": 116.4074,
      "base_lat": 39.9000,
      "base_lng": 116.4000
    }'

2. 创建订单
  curl -X POST http://localhost:8000/api/order/create \
    -H "Content-Type: application/json" \
    -d '{
      "user_id": 1,
      "desc": "帮我买菜",
      "address": "北京市朝阳区建国路",
      "lat": 39.9155,
      "lng": 116.4345
    }'

3. 搜索附近服务者
  curl 'http://localhost:8000/api/provider/nearby?lat=39.9155&lng=116.4345'
"""

# ============================================================
# 10. 常见问题排查
# ============================================================

"""
Q1: 启动时报 "No module named 'app'"
  A: 确保在 backend 目录下运行命令，且当前目录在 Python 路径中

Q2: 数据库连接失败
  A: 检查：
    1. MySQL 服务是否启动
    2. 数据库是否创建
    3. .env 中的连接字符串是否正确
    4. 用户名和密码是否正确

Q3: 高德 API 报错
  A: 检查：
    1. API Key 是否正确
    2. Key 是否有权限（Web 服务 API）
    3. 是否超过免费配额
    4. 网络连接是否正常

Q4: 端口 8000 已被占用
  A: 使用其他端口启动：
    python -m uvicorn app.main:app --port 8001

Q5: 请求返回 CORS 错误
  A: 已在 main.py 中配置 CORS，允许所有来源
    如需限制，修改 main.py 中的 allow_origins
"""

# ============================================================
# 11. 生产环境部署建议
# ============================================================

"""
部署前检查清单：

1. 依赖管理
   - 确保 requirements.txt 中的版本号明确
   - 使用虚拟环境隔离依赖
   - 定期更新安全补丁

2. 环境变量
   - 使用 .env 管理敏感信息
   - 不要将 .env 提交到版本控制
   - 生产环境使用不同的 Key 和数据库

3. 数据库
   - 定期备份
   - 配置主从复制（高可用）
   - 创建合适的索引优化查询

4. 服务器配置
   - 使用 Gunicorn / Uvicorn 替代 Uvicorn --reload
   - 配置反向代理（Nginx）
   - 启用 HTTPS
   - 配置防火墙和安全组

5. 监控和日志
   - 配置日志系统
   - 监控服务器资源使用
   - 设置错误告警

6. API 限速
   - 实现 Rate Limiting
   - 保护关键接口

7. 版本控制
   - 使用 Git 管理代码
   - 设置 CI/CD 流程
"""

# ============================================================
# 12. 项目扩展建议
# ============================================================

"""
后续开发方向：

1. 用户认证
   - 实现用户注册和登录
   - 使用 JWT Token
   - 添加权限控制

2. 实时通知
   - WebSocket 实现实时位置更新
   - 订单状态推送
   - 消息通知系统

3. 支付集成
   - 接入微信支付或支付宝
   - 订单结算管理

4. 数据分析
   - 订单统计
   - 服务者评分系统
   - 收益统计

5. 优化算法
   - 更复杂的匹配算法
   - 机器学习推荐
   - 路线优化

6. 前端应用
   - Web 端（Vue/React）
   - 移动端（App/小程序）
   - 管理后台

7. 基础设施
   - 数据库集群
   - 缓存系统（Redis）
   - 消息队列（RabbitMQ）
   - 搜索引擎（Elasticsearch）
"""

# ============================================================
# 13. 技术支持和资源
# ============================================================

"""
学习资源：

官方文档：
  - FastAPI: https://fastapi.tiangolo.com/
  - SQLAlchemy: https://docs.sqlalchemy.org/
  - Pydantic: https://docs.pydantic.dev/
  - MySQL: https://dev.mysql.com/doc/

社区资源：
  - FastAPI GitHub: https://github.com/tiangolo/fastapi
  - Stack Overflow: https://stackoverflow.com/
  - Python 官方: https://www.python.org/

高德地图：
  - API 文档: https://lbs.amap.com/api/webservice/guide/api/weatherinfo
  - 开发者社区: https://lbs.amap.com/community
"""

# ============================================================
# 14. 许可证和使用条款
# ============================================================

"""
本项目采用 MIT 许可证，允许自由使用、修改和分发。
详见 LICENSE 文件。

使用高德地图 API 时，请遵守高德的服务条款和隐私政策。
"""

print("配置指南已生成，请查看本文件了解详细信息。")
