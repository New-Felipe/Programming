# Questão 06 - Desenvolva um algoritmo que solicite o número de peças produzidas por cinco operadores em um turno. 
# Aplique as seguintes regras:
# I) Produção acima de 150 peças: bônus de 20% no valor total produzido;
# II) Entre 100 e 150 peças: bônus de 10%;
# III) Abaixo de 100 peças: sem bônus. 
# Considere o valor de R$ 2,00 por peça produzida e exiba o valor total ajustado por operador.
# Utilize o laço de repetição “for” para resolver o problema.

valorPorPeca = 2

for i in range(1, 6):
    producao = int(input(f'Digite o número de peças roduzidas pelo operador {i}: '))
    valorTotal = producao * valorPorPeca

    if producao > 150:
        valorTotal = valorTotal * 1.20
        status = "Bônus de 20%."
    elif producao >= 100:
        valorTotal = valorTotal * 1.10
    else:
        status = "Sem bônus."

    print(f'Operador {i}: valor total ajsutado = R$ {valorTotal:.2f} ({status})')
