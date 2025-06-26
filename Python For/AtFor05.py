metaMinima = 10
metaIdeal = 15
totalPorDia = 0

for dia in range(1, 6):
    clientesAT = int(input(f'Informe o valor de clientes atendidod no dia {dia}: '))
    totalPorDia = totalPorDia + clientesAT

    if totalPorDia < metaMinima:
        print('Necessidade de melhorar o atendimento.')
    elif totalPorDia < metaIdeal:
        print('Incentivo para alcançar a meta ideal!!')
    else:
        print('Parabéns! Você atingiu a meta ideal!')

print(f'Total de clientes atendidos na semana: {totalPorDia}')
