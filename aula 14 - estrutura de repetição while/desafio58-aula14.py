'''
Melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer.
'''

from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
computador = randint(0, 10)
contador = 0
print('PROCESSANDO...')
sleep(3)

while computador != jogador:
    print('Você errou! Eu digitei {} e você digitou {}.'.format(computador, jogador))
    computador = randint(0, 10)
    jogador = int(input('Em que número eu pensei? (de 0 a 10) '))
    print('PROCESSANDO...')
    sleep(1)
    contador += 1
    if jogador == computador:
        print('Parabéns! Você ganhou! Eu digitei {} e você digitou {}'.format(computador, jogador))
print('Você precisou de {} tentativas para acertar.'.format(contador + 1))