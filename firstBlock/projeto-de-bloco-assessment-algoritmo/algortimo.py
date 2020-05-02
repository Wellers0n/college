valorSalario = None
valorEmprestimo = None
porcentagemValor = None
parcela = None
porcentagemReferenteSalario = None

valorSalario = int(input('Digite o valor do seu salário: '))

porcentagemValor = (30 * valorSalario) / 100

parcela = int(input('Digite quantas vezes irá parcelar: '))

porcentagemReferenteSalario = ((parcela/valorSalario) * 100)

if porcentagemValor < porcentagemReferenteSalario:
    print('Você não pode pegar esse empréstimo')

    print('Valor salário: ', valorSalario)
    print('Valor porcentagem de 30%: ', porcentagemValor)
    print('Valor da parcela: ', parcela)
    print('Valor da porcentagem referente ao salario: ', porcentagemReferenteSalario)
else:
    print('Parabéns seu emprestimo foi aceito!')

    print('Valor salário: ', valorSalario)
    print('Valor porcentagem de 30%: ', porcentagemValor)
    print('Valor da parcela: ', parcela)
    print('Valor da porcentagem referente ao salario: ', porcentagemReferenteSalario)

