from app.models import Device
from app.services.network import cisco, juniper, arista, f5, huawei, h3c, generic

def exec_command(device: Device, command: str) -> str:
    dtype = device.type.lower()
    vendor = device.vendor.lower()
    # Cisco
    if "cisco" in vendor:
        if "asa" in dtype or "ftd" in dtype:
            return cisco.exec_cisco_asa(device, command)
        elif "wlc" in dtype:
            return cisco.exec_cisco_wlc(device, command)
        else:
            return cisco.exec_cisco(device, command)
    elif "juniper" in vendor:
        return juniper.exec_juniper(device, command)
    elif "arista" in vendor:
        return arista.exec_arista(device, command)
    elif "f5" in vendor:
        return f5.exec_f5(device, command)
    elif "huawei" in vendor:
        if "firewall" in dtype:
            return huawei.exec_huawei_fw(device, command)
        else:
            return huawei.exec_huawei(device, command)
    elif "h3c" in vendor:
        if "firewall" in dtype:
            return h3c.exec_h3c_fw(device, command)
        else:
            return h3c.exec_h3c(device, command)
    else:
        return generic.ssh_exec_command(device, command)