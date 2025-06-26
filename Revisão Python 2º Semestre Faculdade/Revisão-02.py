# Questão 2 - Desenvolva um algoritmo que realize o controle e cálculo do lucro de uma loja. Primeiramente o algoritmo 
# deve perguntar ao usuário a quantidade de dias que ele deseja ralizar o controle. Em seguida, o programa 
# deve solicitar o faturamento e o custo diário da loja. O algoritmo deverá registrar os valores até calcular o 
# lucro total dos dias informados pelo usuário. Se em algum momento o lucro diário for negativo, exiba um 
# alerta. Utilize o laço de repetição “while” para resolver o problema.

lucroSemanal = 0
dias = 0
periodo = int(input('Por quantos dias você deseja realizar o controle de lucros? '))

while dias < periodo:
    faturamento = int(input(f'Digite o faturamento do dia {dias + 1} (em R$): '))
    custo = float(input(f'Digite o custo do dia {dias + 1} (em R$: )'))
    lucroDiario = faturamento - custo
    lucroSemanal = lucroSemanal - lucroDiario
    dias = dias + 1 #Nesta linha, estamos incrementando (+1), para que a variável "dias" possa ter um novo valor e ser analisada novamente na condição da linha 5.

    if lucroDiario < 0:
        print('Alerta: Lucro diário negativo!')

    print(f'Lucro acumulado até agora: R$ {lucroSemanal:.2f}')

print(f'Lucro total da semana: R$ {lucroSemanal:.2f}')