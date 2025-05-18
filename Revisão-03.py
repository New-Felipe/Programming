# Questão 3 - Uma fábrica de tênis deseja monitorar a produção diária e calcular penalidades ou bônus com base na meta 
# de 300 pares por dia. Solicite a produção diária e continue registrando até que o total acumulado ultrapasse 
# 5000 peças. Utilize o laço de repetição “while” para resolver o problema. Aplique:
# - Penalidade de 10% para produções abaixo de 200 peças;
# - Bônus de 15% para produções acima de 400 peças. Exiba a produção ajustada diariamente.

producaoTotal = 0

while producaoTotal <= 5000:
    producao = int(input('Digite o número de peças produzidas hoje:'))

    if producao > 400:
        producaoAjustada = producao * 1.15
        status = "Bônus aplicado."
    elif producao < 200:
        producaoAjustada = producao * 0.90
        status = "Penalidade aplicada."
    else:
        producaoAjustada = producao
        status = "Sem ajustes."

    producaoTotal = producaoTotal + producaoAjustada

    print(f'Produção ajustada hoje: {producaoAjustada:.2f}. Total acumulado: {producaoTotal:.2f} ({status}).')

print('Meta de 5.000 peças alcançadas.')