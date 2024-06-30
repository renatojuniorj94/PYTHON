"""
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador
"""
while True:
    jogador = dict()
    atleta = list()
    partidas = list()
    total_gols = list()
    todos_os_gols = 0
    jogador['nome'] = str(input('Digite o nome do Jogador: '))
    num_partidas = int(input('Nº de partidas: '))
    jogador['partidas'] = num_partidas
    for c in range(num_partidas):
        total_gols.append(int(input(f'Gol(s) na partida {c + 1}: ')))
        todos_os_gols += total_gols[c]
        jogador['gols por partida'] = total_gols[:]
        jogador['total'] = todos_os_gols
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
    while continuar != 'S':
        print('Opção inválida! Tente novamente.')
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continuar == 'N':
            break


print('-=' * 40)
print(f'Nome do atleta: {jogador['nome']}')
print(f'Gols por partida: {jogador['gols por partida']}')
print(f'Fez um total de {jogador['total']} gols')
print('-=' * 40)
print(f'O jogador {jogador['nome']} jogou {jogador['partidas']} partidas.')
for c in range(jogador['partidas']):
    print(f'=>Na partida {c + 1}, fez {jogador['gols por partida'][c]} gols.'.rjust(32))
print(f'Fez um total de {jogador['total']} gols')