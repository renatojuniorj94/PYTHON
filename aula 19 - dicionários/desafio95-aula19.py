"""
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador
"""
jogador = dict()
lista = list()
gols_por_partida = list()
total_gols = 0
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for partida in range(jogador['partidas']):
        gols = int(input(f'Quantos gols na partida {partida + 1}? '))
        gols_por_partida.append(gols)
        jogador['gols por partida'] = gols_por_partida
        total_gols += gols
        jogador['total'] = total_gols
        lista.append(jogador)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Opção inválida!')
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(lista)
print()
print(jogador)

