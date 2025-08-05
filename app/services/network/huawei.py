import paramiko
from app.models import Device

def exec_huawei(device: Device, command: str):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(device.ip, username=device.username, password=device.password, timeout=10)
        remote = ssh.invoke_shell()
        remote.send('screen-length 0 temporary\n')
        remote.send(command + '\n')
        remote.send('quit\n')
        output = remote.recv(65535).decode()
        ssh.close()
        return output
    except Exception as e:
        return f"Huawei SSH Error: {str(e)}"

def exec_huawei_fw(device: Device, command: str):
    # 华为防火墙专用
    return exec_huawei(device, command)