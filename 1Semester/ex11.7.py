import turtle

turtleScreenEX11_7 = turtle.Screen()
turtleEX11_7 = turtle.Turtle()

def triangulo():
  primeiro = int(input('Digite o primeiro lado: '))
  segundo = int(input('Digite o segundo lado: '))
  terceiro = int(input('Digite o terceiro lado: '))
  for sides in (primeiro, segundo, terceiro):
    turtleEX11_7.forward(sides)

    turtleEX11_7.left(120)


''
turtleScreenEX11_7.listen()

turtleScreenEX11_7.onkey(triangulo, 't')

turtleScreenEX11_7.exitonclick()
