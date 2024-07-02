"""
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador
"""
jogador = dict()
lista = list()
total_de_gols = list()
todos_os_gols = 0
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for partida in range(jogador['partidas']):
        total_de_gols.append(int(input(f'Quantos gols na partida {partida + 1}? ')))
        jogador['gols por partida'] = total_de_gols
        todos_os_gols += total_de_gols[partida]
        jogador['total'] = total_de_gols
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Opção inválida!')
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(lista)