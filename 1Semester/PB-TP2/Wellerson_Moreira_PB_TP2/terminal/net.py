import psutil

dic_interfaces = psutil.net_if_addrs()
print(dic_interfaces['wlp2s0'][0].address)