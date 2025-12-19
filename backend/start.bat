@echo off
REM ==================================================
REM 邻里帮 NeighborHelp 后端服务启动脚本 (Windows)
REM ==================================================

echo.
echo ===============================================
echo   邻里帮 后端服务启动脚本
echo ===============================================
echo.

REM 进入脚本所在目录（backend 目录）
cd /d "%~dp0"

echo 当前路径：
cd
echo.

REM 确认关键文件存在
if not exist app\main.py (
    echo 错误：未找到 app\main.py
    echo 请确认 start.bat 位于 backend\ 目录下。
    pause
    exit /b 1
)

echo 成功定位到 backend 目录。
echo.

REM 检查 Python
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误：未检测到 Python，请先安装 Python 3.9+
    pause
    exit /b 1
)

echo Python 已检测到。
echo.

REM 安装 / 更新依赖（pip 会自动跳过已安装的）
if exist requirements.txt (
    echo 正在检查并安装依赖...
    pip install -r requirements.txt
) else (
    echo 警告：未找到 requirements.txt
)

echo.
echo 正在初始化数据库（create_all 为幂等操作）...
python init_db.py

echo.
echo ===============================================
echo   启动 FastAPI 服务（开发模式）
echo   API 文档地址: http://127.0.0.1:8000/docs
echo ===============================================
echo.

REM 启动服务（--reload 仅用于开发环境）
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

pause
