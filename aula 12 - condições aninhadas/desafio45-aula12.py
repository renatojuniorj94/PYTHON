"""
Crie um programa que faça o computador jogar jokenpô (pedra, papel e tesoura) com você
"""
import random
from random import randint
from time import sleep
jogador = int(input('Sua opções:\n'
                    '[ 0 ] PEDRA\n'
                    '[ 1 ] PAPEL\n'
                    '[ 2 ] TESOURA\n'
                    'Qual é a sua jogada? '))
if jogador != 0 and 1 and 2:
    print('\033[1;31mOpção inválida!\033[m')

lista = ['pedra', 'papel', 'tesoura']
computador = random.randint('pedra', 'papel', 'tesoura')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-' * 10)
print('O computador jogou {}'.format(computador))
print('Você jogou {}'.format(jogador))
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
    print('Você venceu!')