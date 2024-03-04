"""
Crie um programa que faça o computador jogar jokenpô (pedra, papel e tesoura) com você
"""
import random
from random import randint
from time import sleep
'''jogador = int(input('Sua opções:\n'
                    '[ 0 ] PEDRA\n'
                    '[ 1 ] PAPEL\n'
                    '[ 2 ] TESOURA\n'
                    'Qual é a sua jogada? '))
if jogador > 2:
    print('\033[1;31mOpção inválida!\033[m')
    exit()

computador = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-' * 10)
if computador == 0:
    print('O computador jogou PEDRA')
elif computador == 1:
    print('O computador jogou PAPEL')
elif computador == 2:
    print('O computador jogou TESOURA')

if jogador == 0:
    print('Você jogou PEDRA')
elif jogador == 1:
    print('Você jogou PAPEL')
elif jogador == 2:
    print('Você jogou TESOURA')
print('-=-' * 10)

if jogador == computador:
    print('A partida terminou empatada!')
elif jogador == 0 and computador == 1:
    print('Computador venceu!')
elif jogador == 0 and computador == 2:
    print('Você venceu!')
elif jogador == 1 and computador == 0:
    print('Você venceu!')
elif jogador == 1 and computador == 2:
    print('Computador venceu!')
elif jogador == 2 and computador == 0:
    print('Computador venceu!')
elif jogador == 2 and computador == 1:
    print('Você venceu!\n')'''

#Correto! :D

#Outra maneira de fazer

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('O computador escolheu {}'.format(itens[computador]))
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador ==2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador ==2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador ==2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')