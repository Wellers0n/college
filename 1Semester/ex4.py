def factorialWhile(n):
    number = n
    result = 1
    while number:
        number = number - 1
        result = result * (n - number)

    print(f'O fatorial de {n} é: {result}')



factorialWhile(5)