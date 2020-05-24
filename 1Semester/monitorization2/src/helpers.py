import psutil
import platform


def freq():
    return round(psutil.cpu_freq().current / 1000, 1)


def cores():
    return psutil.cpu_count()


def phyCores():
    return psutil.cpu_count(logical=False)


def percentage():
    return psutil.cpu_times_percent(interval=1)


def Mem():
    mem = psutil.virtual_memory()
    capacidade = round(mem.total / (1024 * 1024 * 1024), 2)

    return capacidade


def memory_usage():
    mem = psutil.virtual_memory()
    capacidade = round((mem.used + mem.inactive) / (1024 * 1024 * 1024), 2)
    return capacidade


def memory_usage_percent():
    mem = psutil.virtual_memory()
    percent = round(mem.percent)
    return percent


def disk_usage():
    disco = psutil.disk_usage('.')
    return round((disco.used + disco.free) / (1024 * 1024 * 1024), 2)


def disk_total():
    disco = psutil.disk_usage('.')
    return round((disco.total + disco.free) / (1024 * 1024 * 1024), 2)


def disk_percent():
    disco = psutil.disk_usage('.')
    return round(disco.percent)


def Ip():
    addr = psutil.net_if_addrs()
    return addr['wlp2s0'][0].address


def platform_processor():
    return platform.processor()


def platform_name():
    return platform.node()


def platform_platform():
    return platform.platform()


def platform_system():
    return platform.system()
