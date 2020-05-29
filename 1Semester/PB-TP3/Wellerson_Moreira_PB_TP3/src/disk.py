import psutil


class Disk():
    def __init__(self):
        self.disk = psutil.disk_usage('.')

    def getDiskTotal(self):
        return round((self.disk.total + self.disk.free) / (1024 * 1024 * 1024), 2)  # GB

    def getDiskUsage(self):
        return round((self.disk.used + self.disk.free) / (1024 * 1024 * 1024), 2)  # GB

    def getDiskPercent(self):
        return round(self.disk.percent)
