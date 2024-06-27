"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total
de gols feitos durante o campeonato.
"""
#Nome
#quantidade de partidas
#gols por partida
#total de gols marcados
jogador = dict()
atleta = list()
total_gols = 0
jogador['nome'] = str(input('Digite o nome do Jogador: '))
num_partidas = int(input('Nº de partidas: '))
jogador['partidas'] = num_partidas
for c in range(num_partidas):
    jogador['gols'] = int(input(f'Gol(s) na partida {c + 1}: '))
    total_gols += jogador['gols']

print(total_gols)
print(jogador)