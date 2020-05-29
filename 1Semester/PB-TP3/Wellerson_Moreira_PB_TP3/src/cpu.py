import psutil
import cpuinfo


class CPU():
    def __init__(self):
        self.info = cpuinfo.get_cpu_info()

    def getCpu(self):
        # GHz
        return round(psutil.cpu_freq().current / 1000, 1)

    def getPercentUsage(self):
        # percentage usage
        percent = psutil.cpu_times_percent(interval=0.1)
        return percent.user

    def getCoresLogical(self):
        return psutil.cpu_count()

    def getCores(self):
        return psutil.cpu_count(logical=False)

    def getArch(self):
        # Obtendo Arquitetura: X86_64
        return self.info['arch']

    def getBrand(self):
        # Obtendo Nome: Intel(R) Core(TM) i7-3930K CPU @ 3.20GHz
        return self.info['brand']

    def getBits(self):
        # bits do computador: 64
        return self.info['bits']
