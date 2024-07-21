"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
opcionais:
O nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado
não tenha sido informado corretamente.
"""


def ficha(jogador, quant_gols):
    if jogador == '':
        jogador = '<desconhecido>'
    if quant_gols == '':
        quant_gols = 0
    print(f'O jogador {jogador} fez {quant_gols} gol(s) no campeonato.')


jogador = str(input('Nome do jogador: '))
quant_gols = int(input('Número de gols: '))
ficha(jogador, quant_gols)