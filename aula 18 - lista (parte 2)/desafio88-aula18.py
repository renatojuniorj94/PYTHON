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
