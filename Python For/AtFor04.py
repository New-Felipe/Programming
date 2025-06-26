metaMinima = 200
metaIdeal = 500
totalDasVendasDiarias= 0

for dia in range(1, 8):
    vendasDiarias = float(input(f'Digite o valor das Vendas do dia {dia}: '))
    totalDasVendasDiarias = totalDasVendasDiarias + vendasDiarias

    if totalDasVendasDiarias < metaMinima:
        print('Você não atingiu a meta mínima. Continue se esforçando!')
    elif totalDasVendasDiarias < metaIdeal:
        print('Você atingiu a meta mínima mas não a ideal. Continue se esforçando!')
    else:
        print('Parabéns!! Você atingiu a meta ideal!')

print(f'Total das vendas da semana: {totalDasVendasDiarias:.2f}R$')
