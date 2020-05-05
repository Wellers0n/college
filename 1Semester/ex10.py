import turtle


turtleScreenEX10 = turtle.Screen()
turtleEX10 = turtle.Turtle()

def quadrado(tupleLados):
    if(tupleLados[0] != tupleLados[1] or tupleLados[2] != tupleLados[3]):
        print('Os lados precisam ser iguais para montar um quadrado')
    else:
        for lados in tupleLados:
            turtleEX10.forward(lados)
            turtleEX10.left(90)


quadrado((50, 50, 50, 50))

turtleEX10.penup()

quadrado((30, 30, 30, 30))

turtleScreenEX10.exitonclick()
