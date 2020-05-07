import turtle

turtleScreenEX11_7 = turtle.Screen()
turtleEX11_7 = turtle.Turtle()

def circulo():
    for sides in range(90):
        turtleEX11_7.forward(10)

        turtleEX11_7.left(4)


turtleScreenEX11_7.listen()

turtleScreenEX11_7.onkey(circulo, 'c')

turtleScreenEX11_7.exitonclick()
