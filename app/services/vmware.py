# 需要安装pyvmomi
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl
import os

def list_vms():
    try:
        context = ssl._create_unverified_context()
        si = SmartConnect(host=os.getenv("VMWARE_HOST"),
                          user=os.getenv("VMWARE_USER"),
                          pwd=os.getenv("VMWARE_PASS"),
                          port=int(os.getenv("VMWARE_PORT", "443")),
                          sslContext=context)
        content = si.RetrieveContent()
        vms = []
        for dc in content.rootFolder.childEntity:
            for vm in dc.vmFolder.childEntity:
                if isinstance(vm, vim.VirtualMachine):
                    vms.append(vm.name)
        Disconnect(si)
        return "\n".join(vms)
    except Exception as e:
        return f"VMware Error: {str(e)}"