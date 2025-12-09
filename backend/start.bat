@echo off
REM 邻里帮 后端项目启动脚本

echo.
echo ===============================================
echo 邻里帮 后端服务启动脚本
echo ===============================================
echo.

REM 检查 Python 是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误: 未检测到 Python，请先安装 Python
    pause
    exit /b 1
)

echo ✅ Python 已安装

REM 检查依赖是否安装
echo.
echo 正在检查依赖...
pip list | findstr /i fastapi >nul 2>&1
if errorlevel 1 (
    echo ⚠️ 正在安装依赖...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ 安装依赖失败
        pause
        exit /b 1
    )
)

echo ✅ 依赖检查完毕

REM 初始化数据库
echo.
echo 正在初始化数据库...
python init_db.py

REM 启动服务
echo.
echo ===============================================
echo 启动 FastAPI 服务...
echo API 文档地址: http://localhost:8000/docs
echo ===============================================
echo.

python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

pause
