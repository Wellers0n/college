tupla = (1,2,3,4,'c',6)


def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True


def passToList(tuple):
    return list(tuple)

def passToTuple(list):
    return tuple(list)

def removeElementTuple(tuple, element):
    list =  passToList(tuple)

    try:
        list.remove(element)
    except ValueError:
        return print('Esse elemento não está na lista')

    print(passToTuple(list))



element = input('Qual element você quer remover ?')

if isnumber(element):
    removeElementTuple(tupla, int(element))

else: removeElementTuple(tupla, element)

