import cpu
import helpers


def printLn():
    print(f'Cores: {cpu.cores()}')
    print(f'Cores fisicos: {cpu.phyCores()}')
    print(f'Velocidade: {cpu.freq()} GHz')
    print(f'Consumindo: {cpu.percentage().user + cpu.percentage().system} %')
    print(f'Livre: {cpu.percentage().idle} %')
    print(f'-----------------------')


helpers.setInterval(printLn, 10)
