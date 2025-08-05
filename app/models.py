from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Device(Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), unique=True, index=True)
    ip = Column(String(32), unique=True, index=True)
    type = Column(String(32))
    vendor = Column(String(32))
    username = Column(String(64))
    password = Column(String(128))
    create_time = Column(DateTime, default=datetime.utcnow)

class OperationLog(Base):
    __tablename__ = 'operation_logs'
    id = Column(Integer, primary_key=True, index=True)
    user = Column(String(64))
    device_id = Column(Integer, ForeignKey("devices.id"))
    operation = Column(Text)
    result = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
    device = relationship("Device")