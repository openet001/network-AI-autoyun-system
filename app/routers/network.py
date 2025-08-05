from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import DeviceCreate, DeviceOut, CommandRequest, CommandResponse
from app.models import Device
from app.services.network.autodetect import exec_command

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/devices/", response_model=DeviceOut)
def create_device(device: DeviceCreate, db: Session = Depends(get_db)):
    db_device = Device(**device.dict())
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device

@router.get("/devices/", response_model=list[DeviceOut])
def list_devices(db: Session = Depends(get_db)):
    return db.query(Device).all()

@router.post("/command/", response_model=CommandResponse)
def exec_device_command(req: CommandRequest, db: Session = Depends(get_db)):
    device = db.query(Device).filter(Device.id == req.device_id).first()
    if not device:
        return CommandResponse(result="Device not found!")
    result = exec_command(device, req.command)
    return CommandResponse(result=result)