saldoCorrente = float(input('Digite o saldo corrente da sua conta: '))
qtdDeposito = int(input('Quantos Depósitos você quer realizar? '))
saldoTotal = 0

for i in range(0, qtdDeposito):
    deposito = int(input(f'Digite o valor do {i + 1}º depósito: '))
    saldoTotal = saldoTotal + deposito
    print(f'Saldo após o depósito: R$ {saldoTotal + saldoCorrente:.2f}')

