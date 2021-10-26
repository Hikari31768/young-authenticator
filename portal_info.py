import requests
def url():
    baseurl='http://enet.portal.com/.../wlanacip=0.0.0.0&wlanuserip='    # 校园网认证地址去掉末尾的IP地址填在这里
    rsp = requests.get(baseurl, stream=True)
    local_ip=rsp.raw._connection.sock.getsockname()[0]
    return (baseurl + local_ip)
    
def ip(url):
    rsp = requests.get(url, stream=True)
    return (rsp.raw._connection.sock.getpeername()[0])