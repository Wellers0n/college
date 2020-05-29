import psutil


class Memory():
    def __init__(self):
        self.mem = psutil.virtual_memory()

    def getMemoryUsage(self):
        return round((self.mem.used + self.mem.inactive) / (1024 * 1024 * 1024), 2) # GB

    def getMemoryPercent(self):
        return round(self.mem.percent)

    def getMemoryTotalGb(self):
        return round(self.mem.total / (1024 * 1024 * 1024), 2) # GB
