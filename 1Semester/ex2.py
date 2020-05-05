idadeAnos = int
idadeMeses = int
idadeDias = int

def calcDias(anos, meses, dias):

    total = (anos * 365)

    total = total + (meses * 30)

    total = total + dias

    return print(f'Total dias: {total}')


idadeAnos = int(input('Digite sua idade'))

idadeMeses = int(input('Digite quantos meses'))

idadeDias = int(input('Digite quantos dias'))

calcDias(idadeAnos, idadeMeses, idadeDias)