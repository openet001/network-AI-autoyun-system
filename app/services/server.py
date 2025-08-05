import paramiko
import winrm

def exec_linux_command(ip, username, password, command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password, timeout=10)
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode() + stderr.read().decode()
        ssh.close()
        return output
    except Exception as e:
        return f"Linux SSH Error: {str(e)}"

def exec_windows_command(ip, username, password, command):
    try:
        session = winrm.Session(ip, auth=(username, password))
        r = session.run_cmd(command)
        return r.std_out.decode() + r.std_err.decode()
    except Exception as e:
        return f"Windows WinRM Error: {str(e)}"