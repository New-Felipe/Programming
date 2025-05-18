# Questão 08 - Um site de comparação de preços de produtos deseja contratar você para desenvolver um programa. 
# Primeiramente, o algoritmo deverá solicitar quantos produtos o usuário deseja comparar. Em seguida, o 
# usuário deve digitar o nome do produto e o preço encontrado em duas lojas. Ao final, o programa deverá 
# informar, para cada produto, qual loja ele está com o preço menor.

produtos = int(input('Quantos produtos você deseja comprar? '))

nomes = [x for x in range(produtos)]
precosLoja1 = [x for x in range(produtos)]
precosLoja2 = [x for x in range(produtos)]

for i in range(produtos):
    nomes[i] = input(f'Digite o nome do produto {i + 1}: ')
    precosLoja1[i] = float(input(f'Digite o preço do {nomes[i]} da Loja 1: R$ '))
    precosLoja2[i] = float(input(f'Digite o preço do {nomes[i]} da Loja 2: R$ '))

print('\nComparação de preços: ')
for i in range(produtos):
    if precosLoja1[i] < precosLoja2[i]:
        print(f'O produto {nomes[i]} da Loja 1 é mais barato, com o preço de R$ {precosLoja1[i]:.2f}.')
    elif precosLoja1[i] > precosLoja2[i]:
        print(f'O produto {nomes[i]} da Loja 2 é mais barato, com o preço de R$ {precosLoja2[i]:.2f}.')
    else:
        print(f'O produto {nomes[i]} tem o mesmo preço em ambas as lojas: R$ {precosLoja1[i]:.2f}')
        