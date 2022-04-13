import os
import glob
import time
import subprocess
import psutil
def show_cpu_info():
    cpu_info = psutil.cpu_percent()
    return cpu_info
def show_mac():
    mac = subprocess.run(['cat', '/sys/class/net/eth0/address'], capture_output=True, text=True)
    mac = mac.stdout.replace(':', '').rstrip()
    return mac

def save_info(device_dir):
    cpu_info = show_cpu_info()
    mac = show_mac()
    if os.path.exists(f'{device_dir}/{mac}'):
        os.remove(f'{device_dir}/{mac}')
    with open(f'{device_dir}/{mac}', 'w') as f:
        f.write(str(cpu_info))
    