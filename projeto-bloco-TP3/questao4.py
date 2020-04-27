nomes = []
notas = []
index = int

for i in range(10):
    nome = input('Digite seu nome ')
    nomes.append(nome)
    nota = int(input(f'Digite a nota do candidato {nome} '))
    notas.append(nota)

index = notas.index(max(notas))
print(f'Nome do ganhador {nomes[index]} com a nota: {notas[index]}')
