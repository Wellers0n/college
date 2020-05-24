import pygame
from src.utils import GREEN, RED
from src.rectangle import Rectangle
from src.helpers import freq, percentage, Mem, memory_usage, memory_usage_percent, disk_total, disk_percent, disk_usage, \
    Ip, platform_name, platform_platform, platform_processor, platform_system
from src.text import Text


class Monitoring(pygame.sprite.Sprite):
    def __init__(self):
        # CPU
        self.CPUtotalUsage = round(percentage().user + percentage().system)

        self.CPUText = Text(50, 50 - 25)
        self.CPU = Rectangle(50, 50, 100, 30, GREEN)
        # CPU Usage
        self.CPUUsageText = Text(50, 90)
        self.CPUUsage = Rectangle(50, 50, int(self.CPUtotalUsage), 30, RED)

        # Memory
        self.memory = Rectangle(450, 50, 100, 30, GREEN)
        self.memoryText = Text(450, 50 - 25)
        # Memory usage
        self.memoryUsage = Rectangle(450, 50, memory_usage_percent(), 30, RED)
        self.memoryTextUsage = Text(450, 90)

        # Disk
        self.disk = Rectangle(50, 200, 100, 30, GREEN)
        self.diskText = Text(50, 170)
        # disk usage
        self.diskUsage = Rectangle(50, 200, disk_percent(), 30, RED)
        self.diskTextUsage = Text(50, 240)
        # info ip
        self.ip = Text(50, 400)
        # systen
        self.platform_name = Text(50, 430)
        self.platform_platform = Text(50, 460)
        self.platform_system = Text(50, 490)
        self.platform_processor = Text(50, 520)

    def update(self):
        # CPU
        self.CPUText.display(f'CPU {freq()} GHZ')
        self.CPU.draw()
        self.CPUUsage.draw(round(percentage().user + percentage().system))
        self.CPUUsageText.display(f'CPU Usage {round(percentage().user + percentage().system)} %')
        # Memory
        self.memory.draw()
        self.memoryText.display(f'Memory Total {Mem()} GB')
        self.memoryUsage.draw(memory_usage_percent())
        self.memoryTextUsage.display(f'Memory Usage {memory_usage()} GB')
        # Disk
        self.disk.draw()
        self.diskText.display(f'Disk Total {disk_total()} GB')
        # Disk Usage
        self.diskUsage.draw(disk_percent())
        self.diskTextUsage.display(f'Disk Usage {disk_usage()} GB')
        # IP
        self.ip.display(f'IP config {Ip()}')
        # system
        self.platform_name.display(f'Nome da plataforma: {platform_name()}')
        self.platform_system.display(f'Sistema Operacional: {platform_system()}')
        self.platform_platform.display(f'Plataforma: {platform_platform()}')
        self.platform_processor.display(f'Bits do processador: {platform_processor()}')