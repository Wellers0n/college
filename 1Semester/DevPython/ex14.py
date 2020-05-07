def funcString(string):
    if type(string) == str:
        length = len(string) + 1
        middle = round(length / 2)
        first = string[0:middle]
        second = string[middle:length]

        print(f'é uma string {second}{first}')

    else: print('precisa ser uma string')


funcString('aeiou')