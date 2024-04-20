'''
Melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer.
'''

from random import randint
from time import sleep

'''print('-=-' * 20)
print('Vou pensar em número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
computador = randint(0, 10)
contador = 0
print('PROCESSANDO...')
sleep(1)

while computador != jogador:
    print('GANHEI! Eu digitei {} e você digitou {}.'.format(computador, jogador))
    computador = randint(0, 10)
    jogador = int(input('Em que número eu pensei? (de 0 a 10) '))
    print('PROCESSANDO...')
    sleep(1)
    contador += 1
    if jogador == computador:
        print('Você ganhou, PARABÉNS! Eu digitei {} e você digitou {}.'.format(computador, jogador))
print('Você precisou de {} tentativas para acertar.'.format(contador + 1))'''

#Correto! :D

#Outra maneira de fazer

computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpite))