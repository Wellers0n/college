idade = int
nome = None

idade = int(input('Qual é sua idade ?'))
nome = input('Qual é seu nome? ')


if idade >= 18 and idade <= 65:
    print(f'{nome} você tem {idade} anos por isso você é eleitor obrigatório')

elif idade >= 16 and idade <= 18 or idade > 65:
    print(f'{nome} você tem {idade} anos por isso você é eleitor facultativo')
else:
    print(f'{nome} você tem {idade} anos por isso você não é eleitor')
