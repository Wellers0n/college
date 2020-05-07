import turtle

turtleScreenEX7 = turtle.Screen()
turtleEX7 = turtle.Turtle()

def isTriangle(x, y, z):
    tupla = (x, y, z)

    soma = y + z

    if y < soma or z < soma:
        if x == y and y == z:
            print('Triângulo Equilátero: os comprimentos dos três lados são iguais.')
        elif x == y or y == z or  z == x:
            print('Triângulo Isósceles: os comprimentos de dois lados são iguais.')
        else: print('Triângulo Escaleno: os comprimentos dos três lados são diferentes.')

    else: print('não é um triangulo válido')
    return tupla

primeiro = int(input('Digite o primeiro lado: '))
segundo = int(input('Digite o segundo lado: '))
terceiro = int(input('Digite o terceiro lado: '))

def  triangulo(tupleSides):
    """ Desenha um triangulo de lado."""
    for sides in tupleSides:
        turtleEX7.forward(sides)

        turtleEX7.left(120)

triangulo(isTriangle(primeiro, segundo, terceiro))
turtleScreenEX7.exitonclick()