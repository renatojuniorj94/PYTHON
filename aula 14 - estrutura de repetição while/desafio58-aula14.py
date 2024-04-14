'''
Melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer.
'''

from random import randint
from time import sleep

computador = randint(0, 10)
print('=--' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('=--' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))

