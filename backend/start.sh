#!/bin/bash
# 邻里帮 后端项目启动脚本

echo ""
echo "==============================================="
echo "邻里帮 后端服务启动脚本"
echo "==============================================="
echo ""

# 检查 Python 是否安装
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未检测到 Python，请先安装 Python"
    exit 1
fi

echo "✅ Python 已安装: $(python3 --version)"

# 检查依赖是否安装
echo ""
echo "正在检查依赖..."
python3 -c "import fastapi" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️ 正在安装依赖..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "❌ 安装依赖失败"
        exit 1
    fi
fi

echo "✅ 依赖检查完毕"

# 初始化数据库
echo ""
echo "正在初始化数据库..."
python3 init_db.py

# 启动服务
echo ""
echo "==============================================="
echo "启动 FastAPI 服务..."
echo "API 文档地址: http://localhost:8000/docs"
echo "==============================================="
echo ""

python3 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
