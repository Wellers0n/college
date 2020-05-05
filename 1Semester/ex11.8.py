import turtle

turtleScreenEX11_7 = turtle.Screen()
turtleEX11_7 = turtle.Turtle()

def quadrado():
    primeiro = int(input('Digite o primeiro lado: '))
    segundo = int(input('Digite o segundo lado: '))
    terceiro = int(input('Digite o terceiro lado: '))
    quarto = int(input('Digite o quarto lado: '))
    for sides in (primeiro, segundo, terceiro, quarto):
        turtleEX11_7.forward(sides)

        turtleEX11_7.left(90)


turtleScreenEX11_7.listen()

turtleScreenEX11_7.onkey(quadrado, 'q')

turtleScreenEX11_7.exitonclick()
