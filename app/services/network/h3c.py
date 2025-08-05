import paramiko
from app.models import Device

def exec_h3c(device: Device, command: str):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(device.ip, username=device.username, password=device.password, timeout=10)
        remote = ssh.invoke_shell()
        remote.send('screen-length disable\n')
        remote.send(command + '\n')
        remote.send('quit\n')
        output = remote.recv(65535).decode()
        ssh.close()
        return output
    except Exception as e:
        return f"H3C SSH Error: {str(e)}"

def exec_h3c_fw(device: Device, command: str):
    # H3C防火墙专用
    return exec_h3c(device, command)