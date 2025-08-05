from fastapi import APIRouter
from app.schemas import CommandRequest, CommandResponse
from app.services.server import exec_linux_command, exec_windows_command
from app.models import Device
from app.database import SessionLocal

router = APIRouter()

@router.post("/linux/", response_model=CommandResponse)
def linux_command(req: CommandRequest):
    db = SessionLocal()
    device = db.query(Device).filter(Device.id == req.device_id).first()
    if not device:
        return CommandResponse(result="Device not found")
    result = exec_linux_command(device.ip, device.username, device.password, req.command)
    return CommandResponse(result=result)

@router.post("/windows/", response_model=CommandResponse)
def windows_command(req: CommandRequest):
    db = SessionLocal()
    device = db.query(Device).filter(Device.id == req.device_id).first()
    if not device:
        return CommandResponse(result="Device not found")
    result = exec_windows_command(device.ip, device.username, device.password, req.command)
    return CommandResponse(result=result)