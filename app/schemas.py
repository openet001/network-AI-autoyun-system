from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DeviceBase(BaseModel):
    name: str
    ip: str
    type: str
    vendor: str
    username: str
    password: str

class DeviceCreate(DeviceBase):
    pass

class DeviceOut(DeviceBase):
    id: int
    create_time: datetime

    class Config:
        orm_mode = True

class CommandRequest(BaseModel):
    device_id: int
    command: str

class CommandResponse(BaseModel):
    result: str

class AIRequest(BaseModel):
    question: str

class AIResponse(BaseModel):
    answer: str

class LogOut(BaseModel):
    id: int
    user: str
    device_id: int
    operation: str
    result: str
    timestamp: datetime

    class Config:
        orm_mode = True