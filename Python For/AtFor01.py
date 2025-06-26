totalCalorias = 0

for i in range(1, 8):
    calorias = float(input('Digite as calorias consumidas no {i}º dia: '))
    totalCalorias = totalCalorias + calorias

print(f'O total de calorias consumidas na semana foi: {totalCalorias} calorias.')
