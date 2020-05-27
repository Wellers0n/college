import psutil


class Ip():
    def __init__(self):
        self.ip = psutil.net_if_addrs()

    def getEddressLocal(self):
        return self.ip['lo'][0].address

    def getEddress(self):
        return self.ip['wlp2s0'][0].address

    def getEddressMask(self):
        return self.ip['wlp2s0'][0].netmask

    def getEddressBroadcast(self):
        return self.ip['wlp2s0'][0].broadcast