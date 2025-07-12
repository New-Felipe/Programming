saldo =  1500
valor_saque = 1500

#pequeno exemplo:
# if condição: 
    #comando 1
    #comando 2

#Desvio simples: 
# if saldo >= valor_saque:
   # saldo -= valor_saque
    # comandos para liberar o dinheiro:
    # print("Saque efetuado com sucesso!")

# Usando If e Else:
if saldo >= valor_saque:
    saldo -= valor_saque
    print("Saque efetuado com sucesso!")
else:
    print("Saque não efetuado: Saldo insuficiente")
    