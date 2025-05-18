# Questão 07 - Um usuário deseja contratar você para desenvolver um algoritmo que o ajude a saber a média de consumos 
# mensais de energia, bem como os meses que tiveram consumos acima da média. Desenvola um algoritmo 
# que, primeiramente, solicite ao usuário, a quantidade de meses que ele deseja registrar os consumos de 
# energia. Em seguida, o programa deve solicitar o nome do mês e o consumo de cada um deles. Logo após, 
# deve ser calculada a média e exibido todos os nomes de todos os meses que ficaram acima da média, bem 
# como seus consumos

soma = 0
qtdMeses = int(input('Quantos meses você deseja registrar o consumo de energia? '))

mes = [x for x in range(qtdMeses)]
consumo = [x for x in range(qtdMeses)]

for i in range(qtdMeses):
    mes[i] = input(f'Digite o nome do {i + 1}º mês: ')
    consumo[i] = float(input(f'Digite o consumo do mês de {mes[i]} (em kWh). '))
    soma = soma + consumo[i]

media = soma / qtdMeses

print(f'Consumo médio: {media:.2f} kWh.')
print('Meses com consumo acima da média:')

for i in range(qtdMeses):
    if consumo[i] > media:
        print(f'Mês acima da média: {mes[i]}. Consumo desse mês: {consumo[i]:.2f}kWh.')