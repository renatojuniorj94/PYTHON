"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total
de gols feitos durante o campeonato.
"""
jogador = dict()
atleta = list()
jogador['nome'] = str(input('Digite o nome do Jogador: '))
jogador['partidas'] = int(input('Nº de partidas: '))
jogador['gols'] = int(input(f'Gol na partida'))