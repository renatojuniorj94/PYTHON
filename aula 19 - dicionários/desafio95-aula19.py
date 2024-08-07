"""
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador
"""
"""jogador = dict()
partidas = list()
lista_jogadores = list()
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    jogador['partidas'] = tot
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]  # jogador['gols'] recebeu uma cópia de partidas.
    jogador['total'] = sum(partidas)
    lista_jogadores.append(jogador.copy())
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Opção inválida!')
    if continuar == 'N':
        break
print('-=' * 30)
print(f'{"Cod":<4}{"Nome":<15}{"gols":<15}{"total":>20}')
print('—' * 55)
for c, j in enumerate(lista_jogadores):
    print(f"{c + 1:<4}{j['nome']:<15}{str(j['gols']):<15}{j['total']:>20}")
print('—' * 55)
print(lista_jogadores)
while True:
    cod_jogador = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if cod_jogador == 999:
        break
    if cod_jogador > len(lista_jogadores) or cod_jogador < 1:
        print('Opção inválida!')
    else:
        nome_sel = lista_jogadores[cod_jogador - 1]['nome']
        print(f'Levantamento do jogador {nome_sel}')
        for c, d in enumerate(lista_jogadores[cod_jogador - 1]['gols']):
            print(f'No jogo {c + 1} fez {d} gols.')"""

#Correto! :D
#Outra maneira de fazer...

time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('—' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('—' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f' —— LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('—' * 40)
print('<<< VOLTE SEMPRE >>>')