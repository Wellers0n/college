adapessoas = None
garcon = None
conta = None
consumo = None
pessoas = None

conta  = int(input('Digite o valor da conta: '))

pessoas = int(input("Digite o valor da pessoas: "))

garcon = conta * 0.1
cadapessoas = conta / pessoas
consumo = conta - garcon

print("Total conta: ", conta);
print("Total consumo: ", consumo);
print("Total para o garçon", garcon);
print("Pessoas na mesa: ", cadapessoas);
