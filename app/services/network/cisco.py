import paramiko
from app.models import Device

def exec_cisco(device: Device, command: str):
    # 普通Cisco IOS/IOS-XE/IOS-XR/NX-OS
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(device.ip, username=device.username, password=device.password, timeout=10)
        remote = ssh.invoke_shell()
        remote.send('terminal length 0\n')
        remote.send(command + '\n')
        remote.send('exit\n')
        output = remote.recv(65535).decode()
        ssh.close()
        return output
    except Exception as e:
        return f"Cisco SSH Error: {str(e)}"

def exec_cisco_asa(device: Device, command: str):
    # ASA/FTD 设备
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(device.ip, username=device.username, password=device.password, timeout=10)
        remote = ssh.invoke_shell()
        remote.send('terminal pager 0\n') # 关闭分页
        remote.send(command + '\n')
        remote.send('exit\n')
        output = remote.recv(65535).decode()
        ssh.close()
        return output
    except Exception as e:
        return f"Cisco ASA SSH Error: {str(e)}"

def exec_cisco_wlc(device: Device, command: str):
    # WLC 设备
    return exec_cisco(device, command)