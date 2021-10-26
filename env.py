import os, platform
def sys():
    sys=0
    if platform.system().lower() == 'linux':
        sys=1
    elif platform.system().lower() == 'windows':
        sys=2
    return sys
def ping(url):
    status=1
    if sys()==1:
        exit_code = os.system('ping -c 1 ' + url + ' >/dev/null 2>&1')
    elif sys()==2:
        exit_code = os.system('ping >nul 2>nul ' + url + ' -n 1')
    if exit_code:
        status=0
    return status