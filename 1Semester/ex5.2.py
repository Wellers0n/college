
tupla = (1,2,3,4,5,6,7)

def divideTuple(tupla):
    length = len(tupla)
    middle = round(length/2)
    print(f'primeira tupla: {tupla[0:middle]}')
    print(f'Segunda tupla: {tupla[middle:length]}')

divideTuple(tupla)