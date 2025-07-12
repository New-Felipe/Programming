numero = int(input("Digite um número qualquer: "))
while numero % 2 == 0 : #Enquanto for par, continue pedindo mais números
    print("Você digitou um número par! vou pedir para que digite outro número.")
    numero = int(input("Digite um número qualquer: "))
print("Parabéns, você digitou um número ímpar! Agora o programa vai seguir...")

#Laço "For" exemplo 1:
# frutas_em_promocao = ["banana", "Maçã", "Laranja", "acerola"]
# for fruta in frutas_em_promocao:
#  print("Hoje a fruta " + fruta + " Está em promoção! aproveite!")

# For como contador... exemplo 2:
# for x in range(5) :
#   print("O valor de x nesta iteração é: ", x)   