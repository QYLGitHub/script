import netifaces


def get_current_ip():
    """获取本机ip
    :return 本地ip以及外网ip type: list
    """
    ips = []
    exclude_iface = ['lo']
    interfaces = netifaces.interfaces()
    for iface in interfaces:
        if iface not in exclude_iface:
            if netifaces.AF_INET in netifaces.ifaddresses(iface):
                addrs = netifaces.ifaddresses(iface)[netifaces.AF_INET]
                for addr in addrs:
                    ips.append(addr['addr'])
    return ips
