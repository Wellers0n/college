
def factorialFor(n):
    result = 1
    for i in range(n):
        result = result * (n - i)
    print(f'Fatorial de {n} é: {result}')



factorialFor(5)