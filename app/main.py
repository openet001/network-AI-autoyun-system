from fastapi import FastAPI
from app.routers import ai, network, server, vmware
from app.database import Base, engine

# 自动创建数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="智能化网络与服务器运维平台",
    description="基于自然语言的自动化运维与集成平台",
    version="1.0.0"
)

# 路由注册
app.include_router(ai.router, prefix="/ai", tags=["AI助手"])
app.include_router(network.router, prefix="/network", tags=["网络设备"])
app.include_router(server.router, prefix="/server", tags=["服务器"])
app.include_router(vmware.router, prefix="/vmware", tags=["VMware"])