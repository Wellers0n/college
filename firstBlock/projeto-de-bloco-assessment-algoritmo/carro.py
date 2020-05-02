gasolina = 3.98
kmRodadoAno = 10.000
menorValor = float
carroEscolhido = None

tabela = [
    {
        'modelo': 'Chevrolet Ônix',
        'valor': 36.000,
        'imposto': 1.400,
        'consumoMedio': 11.8,
        'valorSeguro': 1.600
    },
    {
        'modelo': 'Ford Fiesta',
        'valor': 32.000,
        'imposto': 1.300,
        'consumoMedio': 13.5,
        'valorSeguro': 1.800
    },
    {
        'modelo': 'VW Fox',
        'valor': 31.000,
        'imposto': 1.450,
        'consumoMedio': 12.3,
        'valorSeguro': 1.300
    },
    {
        'modelo': 'VW Polo',
        'valor': 41.000,
        'imposto': 1.600,
        'consumoMedio': 13.5,
        'valorSeguro': 1.500
    },
    {
        'modelo': 'Hyundai HB20',
        'valor': 40.000,
        'imposto': 1.200,
        'consumoMedio': 11.6,
        'valorSeguro': 1.200
    },
    {
        'modelo': 'Renault Sandero',
        'valor': 30.000,
        'imposto': 1.300,
        'consumoMedio': 12.8,
        'valorSeguro': 1.900
    }
]

for i in tabela:
    totalConsumoGasolina = (kmRodadoAno / i['consumoMedio']) * gasolina
    i['total'] = totalConsumoGasolina + i['valor'] + i['imposto'] + i['valorSeguro']
    menorValor
    if menorValor < i['total']:
        menorValor = i['total']
        carroEscolhido = i['modelo']

    print('Modelo do carro: ', i['modelo'])
    print('Valor Total: %.3f' % (i['valor']))
    print('Consumo médio do carro: %.1f' % (i['consumoMedio']))
    print('Valor do seguro do carro: %.3f' % (i['valorSeguro']))
    print('Total: %.3f' % (i['total']))
    print('=============================')



print('Carro com menos consumo: ', carroEscolhido)
print('Valor com menos consumo: %.3f', menorValor)
