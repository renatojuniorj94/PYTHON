'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de futebol,
na ordem de colocação. Depois mostre:
A - Apenas os 5 primeiros colocados.
B - Os últimos 4 colocados da tabela.
C - Uma lista com os times em ordem alfabética.
D - Em que posição na tabela está o time da Chapecoense.
'''
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG',
         'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport', 'Vitória', 'Coritiba', 'Avaí',
         'Ponte Preta', 'Atlético-GO')
print('-=' * 25)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 25)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 25)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 25)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 25)
enumerate(times)
print(f'A {times[7]} está na {times.index('Chapecoense') + 1}ª posição')

#Correto! :D