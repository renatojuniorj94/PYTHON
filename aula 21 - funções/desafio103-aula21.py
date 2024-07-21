"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
opcionais:
O nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado
não tenha sido informado corretamente.
"""


def ficha(jogador=0, quant_gols=0):
    jogador = str(input('Nome do jogador: '))
    quant_gols = int(input('Número de gols: '))
    print(f'O jogador {jogador} fez {quant_gols}gol(s) no campeonato.')


ficha()