from random import randint
from time import sleep
opçoes = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Sua opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('PEEEDRA')
sleep(1)
print('PAPEELL')
sleep(1)
print('TEEESOURA!!!')
print('-=' * 11)
print(f'Computador Jogou {opçoes[computador]}')
print(f'Jogador Jogou {opçoes[jogador]}')
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('Empatou!!')
    elif jogador == 1:
        print('O(a) Jogador(a) Venceu!')
    elif jogador == 2:
        print('Computador Venceu! =/')
    else:
        print('A Jogada Foi Inválidada! Joga sério cara')
elif computador == 1:
    if jogador == 0:
        print('O Computador Venceu! =/')
    elif jogador == 1:
        print('Empatou!!')
    elif jogador == 2:
        print('O(a) Jogador(a) Venceu!')
    else:
        print('A Jogada Foi Inválidada! Joga sério cara')
elif computador == 2:
    if jogador == 0:
        print('O(a) Jogador(a) Venceu!')
    elif jogador == 1:
        print('O Computador Venceu! =/')
    elif jogador == 2:
        print('Empatou!!')
    else:
        print('Jogada Inválida! Joga sério cara')
