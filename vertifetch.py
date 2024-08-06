import platform
import psutil
import subprocess
import os
import socket

img = "/home/ocueye/Documents/code/python/pyfetch/art.txt"

# ANSI escape codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"






def get_distro():
    try:
        return subprocess.check_output(['lsb_release', '-ds']).strip().decode()
    except Exception:
        return "Unknown Distro"

def get_kernel():
    return platform.release()

def get_uptime():
    uptime_seconds = int(psutil.boot_time())
    uptime_string = subprocess.check_output(['uptime', '-p']).strip().decode()
    return uptime_string

def get_packages():
    try:
        if os.path.exists('/usr/bin/dpkg'):
            pkg_count = subprocess.check_output(['dpkg', '--list']).decode().count('\n')
            return f"{pkg_count} (dpkg)"
        elif os.path.exists('/usr/bin/rpm'):
            pkg_count = subprocess.check_output(['rpm', '-qa']).decode().count('\n')
            return f"{pkg_count} (rpm)"
    except Exception:
        return "Unknown"
    return "Unknown"

def get_shell():
    return os.path.basename(os.getenv('SHELL'))

def get_resolution():
    try:
        output = subprocess.check_output(['xdpyinfo']).decode()
        for line in output.split('\n'):
            if 'dimensions:' in line:
                return line.split()[1]
    except Exception:
        return "Unknown"
    return "Unknown"

def get_cpu():
    return platform.processor()

def get_memory():
    mem = psutil.virtual_memory()
    return f"{mem.total // (1024 ** 2)}MB"

def get_hostname():
    return socket.gethostname()

def get_user():
    return os.getenv('USER')

def main():
    print()
    with open (img,'r') as f:
        print(BLUE)
        print(f.read())
        print(RESET)
    print()
    print(f"{BLUE}-{RESET}Hostname: {get_hostname()}")
    print(f"{BLUE}|-{RESET}CPU: {get_cpu()}")
    print(f"{BLUE}|-{RESET}Memory: {get_memory()}")
    print(f"{BLUE}|-{RESET}OS: {get_distro()} ")
    print(f"{BLUE}| |-{RESET}Kernel: {get_kernel()}")
    print(f"{BLUE}| |-{RESET}Uptime: {get_uptime()}")
    print(f"{BLUE}| |-{RESET}Packages: {get_packages()}")
    print(f"{BLUE}| |-{RESET}Shell: {get_shell()}")
    print(f"{BLUE}| | |-{RESET}User: {get_user()}")
    print(f"{BLUE}| | |-{RESET}Resolution: {get_resolution()}")
    
    
    



if __name__ == "__main__":
    main()
