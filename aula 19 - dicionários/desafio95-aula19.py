"""
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador
"""
jogador = dict()
total_de_gols = list()
todos_os_gols = 0
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    jogador['partidas'] = partidas
    for partida in range(partidas):
        jogador['gols'] = int(input(f'Quantos gols na partida {partida + 1}? '))
        todos_os_gols += jogador['gols']
        jogador['gols por partida'] = total_de_gols[:]
    break
print(jogador)
print(todos_os_gols)
print(jogador['gols por partida'])