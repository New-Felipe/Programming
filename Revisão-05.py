 # Questão 5 - Uma montadora de carro está precisando analisar a eficiência de consumo de combustível de cinco modelos 
# de sua marca. Desenvolva um algoritmo que solicite a distância percorrida e o consumo de combustível (em 
# litros) de cada veículo. Em seguida, calcule a eficiência (quilômetros percorridos / litros gastos) e classifique:
# I) Acima de 12 km/L: "Eficiente";
# II) Entre 8 e 12 km/L: "Consumo médio";
# III) Abaixo de 8 km/L: "Alto consumo".
# Mostre a eficiência de cada veículo à medida em que o programa for realizando e a classificação. Utilize o 
# laço de repetição “for” para resolver o problema.

for i in range(1, 6):
    distancia = float(input(f'Digite a distância percorrida pelo veículo {1} (em km): '))
    combustivel = float(input('Digite o consumo de combustível do veículo {i} (em litros: )'))

    if combustivel > 0:
        eficiencia = distancia / combustivel
        if eficiencia > 12:
            status = "Eficiente."
        elif eficiencia >= 8:
            status = "Consumo médio."
        else:
            status = "Alto consumo."
        print(f'Veículo {i}: Eficiência = {eficiencia:.2f} Km/L ({status}.)')
    else:
        print(f'Verículo {i}: Consumo de combustível inválido.')
