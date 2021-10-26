from env import ping, sys
from portal_info import url, ip
# 在下方输入登录用户名、密码和校园网认证地址
username='18000000000'
password='12345678'
# 还有一个baseurl参数在同目录下的portal_info.py里需要更改

# 检查系统兼容性
if(sys()==0):
    print('系统不兼容，中断程序')
    quit()

# 拼接认证地址&获取认证地址ip
portal_url=url()
portal_ip=ip(portal_url)
# 检查网络连通性
if(ping('223.5.5.5')):      # 检查公网连通性
    print('已连接互联网')
    quit()
else:
    if(ping(portal_ip)):    # 检查是否连接校园网
        print('已连接校园网，开始认证')
    else:
        print('未联网，请连接网络后重试')
        quit()

# 开始登录
from login import login
for i in range(5):          # 若联网不成功重试5次
    login( username, password, portal_url )
    # 验证是否登录成功
    if (ping('223.5.5.5')):
        print('已连接互联网')
        quit()
    print('连接失败,正在进行第', i+1, '次尝试')
