from src.rectangle import Rectangle
from src.surface import Surface
from src.utils import WHITE, BLACK, RED, GREEN, window_width, window_height
from src.cpu import CPU
from src.text import Text
from src.memory import Memory
from src.disk import Disk
from src.ip import Ip


class Monitoring():
    def __init__(self):
        ############################################################################
        # CPU
        self.cpu = CPU()
        self.surfCpu = Surface(0, 0, 500, 400)
        self.textCpu = Text(19, 25, self.surfCpu.getSurface(), 15)
        self.rectCpu = Rectangle(20, 50, 200, 15, self.surfCpu.getSurface(), GREEN)
        self.rectCpuUsage = Rectangle(20, 50, 200, 15, self.surfCpu.getSurface(), RED)
        # logic core cpu
        self.xCores = 0
        self.xCoresInside = 0
        self.rectCores = []
        for core in range(self.cpu.getCoresLogical()):
            self.xCores += 20
            if self.xCores > 180:
                self.xCoresInside += 20
                self.rectCores.append(Rectangle(self.xCoresInside, 95, 10, 15, self.surfCpu.getSurface(), GREEN))
            self.rectCores.append(Rectangle(self.xCores, 75, 10, 15, self.surfCpu.getSurface(), GREEN))
        # infos cpu
        self.textCore = Text(20, 130, self.surfCpu.getSurface(), 15)
        self.textCoreLogical = Text(20, 150, self.surfCpu.getSurface(), 15)
        self.textArch = Text(20, 170, self.surfCpu.getSurface(), 15)
        self.textBits = Text(20, 190, self.surfCpu.getSurface(), 15)
        self.textBrand = Text(20, 210, self.surfCpu.getSurface(), 15)
        #############################################################################
        #############################################################################
        # MEMORY
        self.memory = Memory()
        self.surfMemory = Surface(0, 0, 500, 400)
        self.rectMemory = Rectangle(20, 50, 200, 15, self.surfMemory.getSurface(), GREEN)
        self.rectMemoryUsage = Rectangle(20, 50, 200, 15, self.surfMemory.getSurface(), RED)
        # memory info
        self.textMemory = Text(19, 25, self.surfMemory.getSurface(), 15)
        self.textMemoryTotal = Text(19, 130, self.surfMemory.getSurface(), 15)
        self.textMemoryPercent = Text(19, 150, self.surfMemory.getSurface(), 15)
        self.textMemoryUsage = Text(19, 170, self.surfMemory.getSurface(), 15)
        #############################################################################
        #############################################################################
        # DISK
        self.disk = Disk()
        self.surfDisk = Surface(0, 0, 500, 400)
        self.rectDisk = Rectangle(20, 50, 200, 15, self.surfDisk.getSurface(), GREEN)
        self.rectDiskUsage = Rectangle(20, 50, 200, 15, self.surfDisk.getSurface(), RED)
        # disk info
        self.textDisk = Text(19, 25, self.surfDisk.getSurface(), 15)
        self.textDiskTotal = Text(19, 130, self.surfDisk.getSurface(), 15)
        self.textDiskPercent = Text(19, 150, self.surfDisk.getSurface(), 15)
        self.textDiskUsage = Text(19, 170, self.surfDisk.getSurface(), 15)
        #############################################################################
        ###############################################################################
        # IP
        self.ip = Ip
        self.surfIp = Surface(0, 0, 500, 400)
        self.textIp = Text(250, 25, self.surfIp.getSurface(), 15)
        self.textIpEddressLocal = Text(15, 50, self.surfIp.getSurface(), 15)
        self.textIpEddress = Text(15, 100, self.surfIp.getSurface(), 15)
        self.textIpEddressMask = Text(15, 150, self.surfIp.getSurface(), 15)
        self.textIpEddressBroadcast = Text(15, 200, self.surfIp.getSurface(), 15) \
            ###############################################################################
        ###############################################################################
        # INFOS
        self.surfInfo = Surface(0, 0, 500, 400)
        # texts infos cpu
        self.textInfoCpu = Text(10, 10, self.surfInfo.getSurface(), 15)
        self.textInfoCore = Text(20, 30, self.surfInfo.getSurface(), 15)
        self.textInfoCoreLogical = Text(20, 50, self.surfInfo.getSurface(), 15)
        self.textInfoArch = Text(20, 70, self.surfInfo.getSurface(), 15)
        self.textInfoBits = Text(20, 90, self.surfInfo.getSurface(), 15)
        self.textInfoBrand = Text(20, 110, self.surfInfo.getSurface(), 15)
        # texts infos memory

        self.textInfoMemory = Text(10, 140, self.surfInfo.getSurface(), 15)
        self.textInfoMemoryTotal = Text(20, 160, self.surfInfo.getSurface(), 15)
        self.textInfoMemoryPercent = Text(20, 180, self.surfInfo.getSurface(), 15)
        self.textInfoMemoryUsage = Text(20, 200, self.surfInfo.getSurface(), 15)
        # texts infos disk
        self.textInfoDisk = Text(10, 230, self.surfInfo.getSurface(), 15)
        self.textInfoDiskTotal = Text(20, 250, self.surfInfo.getSurface(), 15)
        self.textInfoDiskPercent = Text(20, 270, self.surfInfo.getSurface(), 15)
        self.textInfoDiskUsage = Text(20, 290, self.surfInfo.getSurface(), 15)
        # text ip
        self.textInfoIp = Text(10, 320, self.surfInfo.getSurface(), 15)
        self.textInfoIpEddress = Text(20, 340, self.surfInfo.getSurface(), 15)

        ###############################################################################
        ###############################################################################
        # arrays surface
        self.arrSurface = [self.surfCpu, self.surfMemory, self.surfDisk, self.surfIp, self.surfInfo]

    def update(self, count):
        self.arrSurface[count].draw()
        ###############################################################################
        # cpu
        percentCPU = round((self.cpu.getPercentUsage() * 200) / 100)
        self.rectCpu.draw()
        self.rectCpuUsage.draw()
        self.rectCpuUsage.update(percentCPU)
        self.textCpu.draw(f'CPU {self.cpu.getCpu()} MHz | Usage {percentCPU} %')
        # logic core cpu
        for core in range(self.cpu.getCoresLogical()):
            self.rectCores[core].draw()
        # infos cpu
        self.textCoreLogical.draw(f'Núcleos (Lógicos): {self.cpu.getCoresLogical()}')
        self.textCore.draw(f'Núcleos (Físicos): {self.cpu.getCores()}')
        self.textArch.draw(f'Arquitetura: {self.cpu.getArch()}')
        self.textBits.draw(f'Palavra (bits): {self.cpu.getBits()}')
        self.textBrand.draw(f'Nome: {self.cpu.getBrand()}')
        ###############################################################################
        ###############################################################################
        # memory
        self.rectMemory.draw()
        self.rectMemoryUsage.draw()
        self.rectMemoryUsage.update(round((self.memory.getMemoryPercent() * 200) / 100))
        self.textMemory.draw(f'Memória: {self.memory.getMemoryTotalGb()} GB')
        self.textMemoryTotal.draw(f'Memória Total: {self.memory.getMemoryTotalGb()} GB')
        self.textMemoryUsage.draw(f'Memória Usada: {self.memory.getMemoryUsage()} GB')
        self.textMemoryPercent.draw(f'Memória Porcentagem: {self.memory.getMemoryPercent()}%')
        ###############################################################################
        ###############################################################################
        # disk
        self.rectDisk.draw()
        self.rectDiskUsage.draw()
        self.rectDiskUsage.update(round((self.disk.getDiskPercent() * 200) / 100))
        self.textDisk.draw(f'Disco {self.disk.getDiskTotal()} GB')
        self.textDiskTotal.draw(f'Disco Total {self.disk.getDiskTotal()} GB')
        self.textDiskUsage.draw(f'Disco Usado {self.disk.getDiskUsage()} GB')
        self.textDiskPercent.draw(f'Porcentagem do Disco {self.disk.getDiskPercent()}%')
        ###############################################################################
        ###############################################################################
        # IP
        self.ip = Ip()
        self.textIp.draw('IP')
        self.textIpEddressLocal.draw(f'Endereço Local: {self.ip.getEddressLocal()}')
        self.textIpEddress.draw(f'Endereço: {self.ip.getEddress()}')
        self.textIpEddressMask.draw(f'Endereço Mask: {self.ip.getEddressMask()}')
        self.textIpEddressBroadcast.draw(f'Endereço Broadcast: {self.ip.getEddressBroadcast()}')
        ###############################################################################
        ###############################################################################
        # INFOS
        # cpu
        self.textInfoCpu.draw('CPU:')
        self.textInfoCoreLogical.draw(f'- Núcleos (Lógicos): {self.cpu.getCoresLogical()}')
        self.textInfoCore.draw(f'- Núcleos (Físicos): {self.cpu.getCores()}')
        self.textInfoArch.draw(f'- Arquitetura: {self.cpu.getArch()}')
        self.textInfoBits.draw(f'- Palavra (bits): {self.cpu.getBits()}')
        self.textInfoBrand.draw(f'- Nome: {self.cpu.getBrand()}')
        # memory
        self.textInfoMemory.draw(f'Memória:')
        self.textInfoMemoryTotal.draw(f'- Memória Total: {self.memory.getMemoryTotalGb()} GB')
        self.textInfoMemoryUsage.draw(f'- Memória Usada: {self.memory.getMemoryUsage()} GB')
        self.textInfoMemoryPercent.draw(f'- Memória Porcentagem: {self.memory.getMemoryPercent()}%')
        # disk
        self.textInfoDisk.draw('Disco:')
        self.textInfoDiskTotal.draw(f'- Disco Total {self.disk.getDiskTotal()} GB')
        self.textInfoDiskUsage.draw(f'- Disco Usado {self.disk.getDiskUsage()} GB')
        self.textInfoDiskPercent.draw(f'- Porcentagem do Disco {self.disk.getDiskPercent()}%')
        # ip
        self.textInfoIp.draw('IP:')
        self.textInfoIpEddress.draw(f'- Endereço: {self.ip.getEddress()}')
