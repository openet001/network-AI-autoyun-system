from fastapi import APIRouter
from app.schemas import CommandResponse
from app.services.vmware import list_vms

router = APIRouter()

@router.get("/listvms/", response_model=CommandResponse)
def get_vms():
    vms = list_vms()
    return CommandResponse(result=vms)