# Questão 04 - Maria acabou de ser efetivada em uma clínica veterinária e precisa de sua ajuda para organizar os 
# experimentos do laboratório ao qual ela é responsável. Ela precisa saber, ao final de cada semana (considere 
# 5 dias, a quantidade de dias trabalhados na semana), quantas cobaias foram utilizadas no laboratório e o 
# percentual de cada tipo de cobaia utilizada. Maria trabalha com apenas um tipo de cobaia por dia, para seus 
# testes. As cobaias são: Ratos, coelhos e sapos. Faça um programa que solicite, por dia, a quantidade e o 
# tipo de cobaias que foi utilizado. Ao final da semana trabalhada, o progrma deve mostrar um relatório, com 
# o total de cobaias e o percentual de cada um em relação ao total de cobaias utilizadas. Utilize o laço de 
# repetição “for” para resolver o problema.

ratos = 0
sapos = 0
coelhos = 0

for i in range(0, 5):
    print('\nEscolha uma opção:')
    print('1 - Rato')
    print('2 - Sapo')
    print('3 - Coelho')

    tipo = int(input(f'Informe o tipo de cobaia do {i + 1}ª dia: '))
    qtdcobaias = int(input(f'Informe a quantidade de cobaias do {i + 1}ª dia: '))

    if tipo == 1:
        ratos = ratos + qtdcobaias

    elif tipo == 2:
        sapos = sapos + qtdcobaias
    
    else:
        coelhos = coelhos + qtdcobaias
    
total = coelhos + ratos + sapos

pCoelhos = (coelhos / total) * 100
pRatos = (ratos / total) * 100
pSapos = (sapos / total) * 100

print('\nRELATÓRIO FINAL:')

print(f'Total de cobaias: {total}.')
print(f'Total de coelhos: {coelhos}.')
print(f'Total de ratos: {ratos}.')
print(f'Percentual de coelhos: {pCoelhos:.2f}%.')
print(f'Percentual de ratos: {pRatos:.2f}%.')
print(f'Percentual de sapos: {pSapos:.2f}%.')
