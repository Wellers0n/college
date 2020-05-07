import turtle

def quadrado(tupleLados):
    if(tupleLados[0] != tupleLados[1] or tupleLados[2] != tupleLados[3]):
        print('Os lados precisam ser iguais para montar um quadrado')
    else:
        turtleScreenEX8 = turtle.Screen()
        turtleEX8 = turtle.Turtle()
        for lados in tupleLados:
            turtleEX8.forward(lados)
            turtleEX8.left(90)
        turtleScreenEX8.exitonclick()


primeiro = int(input('Digite o primeiro lado: '))
segundo = int(input('Digite o segundo lado: '))
terceiro = int(input('Digite o terceiro lado: '))
quarto = int(input('Digite o quarto lado: '))
''
quadrado((primeiro, segundo, terceiro, quarto))

