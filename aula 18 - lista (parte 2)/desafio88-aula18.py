"""
Faça um programa que ajude um jogador da mega-sena a criar palpites.
O programa vai perguntar quantos jogos serão gerados e
vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import sample
from time import sleep
print('—' * 30)
print(f'{'SURPRESINHA MEGA SENA':^30}')
print('—' * 30)
quant_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(quant_jogos):
    jogo = sample(range(1, 61), 6)
    jogo.sort()
    print(f'Jogo {c + 1}: {jogo}')
    sleep(1)
print('-=' * 6, '< BOA SORTE! >', '-=' * 6)

#Correto! :D
#Outra maneira de fazer...

from random import randint
from time import sleep
lista = list()
jogos = list()
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'Sorteando {quant} jogos', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-=' * 6, '< BOA SORTE! >', '-=' * 6)