import paramiko
from app.models import Device

def exec_juniper(device: Device, command: str):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(device.ip, username=device.username, password=device.password, timeout=10)
        remote = ssh.invoke_shell()
        remote.send('set cli screen-length 0\n')
        remote.send(command + '\n')
        remote.send('exit\n')
        output = remote.recv(65535).decode()
        ssh.close()
        return output
    except Exception as e:
        return f"Juniper SSH Error: {str(e)}"