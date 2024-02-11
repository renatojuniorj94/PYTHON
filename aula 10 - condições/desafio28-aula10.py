'''
Escreva um programa que faça o computador "pensar" em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi
o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

import random

'''print('=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=\n'
      'Vou pensar em um número entre 0 e 5. Tente adivinhar...\n'
      '=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=')
lista = random.choice([0, 1, 2, 3, 4, 5])
escolhido = int(input('Em qual número eu estou pensando? '))
print('Eu escolhi o número {}'.format(lista))
if lista == escolhido:
    print('Parabéns você venceu! :D')
else:
    print('Você perdeu! Tente novamente!')'''

#Correto! :D
#Outra maneira de fazer...

#from random import randint
from time import sleep
computador = random.randint(0, 5) # Fazendo o computado escolher um número inteiro de 0 a 5
print('-=-' * 20)
print('Vou pensar em número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3) # Fazendo o computador aguardar 3 segundos até a resposta.
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))