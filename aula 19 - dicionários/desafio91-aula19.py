"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário
em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter
# https://docs.python.org/pt-br/3/library/operator.html
jogador = {'jogador 1': randint(1, 6),
           'jogador 2': randint(1, 6),
           'jogador 3': randint(1, 6),
           'jogador 4': randint(1, 6)
           }
ranking = dict()
print('Valores sorteados: ')
for k, v in jogador.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('—' * 30)
print(' == RANKING DOS JOGADORES == ')
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'  {i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(1)

#Correto! :D