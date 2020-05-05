tupla = (1, 2, 3, 4, 5)

def verifyValueInTuple(value):
    result = str
    for i in tupla:
        if i == int(value):
            result = f'index da tupla é: {tupla.index(i)}'
            break
        else: result = f'valor {value} não encontrado'
    return print(result)

print('lembrando a tupla está com os seguintes valores: (1, 2, 3, 4, 5)')
value = input('Digite um valor para verificar se existe na tupla: ')

verifyValueInTuple(value)