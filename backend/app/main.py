from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import order, provider, amap

app = FastAPI(
    title="邻里帮后端服务",
    description="基于位置的邻里服务平台",
    version="1.0.0",
)

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 路由注册
app.include_router(order.router, prefix="/api/order", tags=["订单模块"])
app.include_router(provider.router, prefix="/api/provider", tags=["服务者模块"])
app.include_router(amap.router, prefix="/api/amap", tags=["高德地图"])

@app.get("/")
def root():
    return {
        "message": "NeighborHelp Backend Running",
        "version": "1.0.0",
        "docs": "/docs",
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
