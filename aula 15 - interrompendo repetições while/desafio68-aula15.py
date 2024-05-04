'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador
PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

print('=-' * 15, end='=\n')
print(f'{'VAMOS JOGAR PAR OU ÍMPAR':^30}')
print('=-' * 15, end='=\n')

import random
resultado = bool
qtd_vit = 0
while True:
    jogador = int(input('Digite um valor [De 0 a 10]: '))
    while jogador < 0 or jogador > 10:
        print('Número\033[1;43m INVÁLIDO!\033[m Tente novamente.')
        jogador = int(input('Digite um valor [De 0 a 10]: '))
    jog_ip = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    while jog_ip not in ['P', 'I']:
        print('Opção\033[1;43m INVÁLIDA!\033[m Tente novamente.')
        jog_ip = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print('—' * 60)
    comp_ip = par_imp = str
    computador = random.randint(0, 10)
    soma = jogador + computador
    if jog_ip == 'I':
        comp_ip = 'P'
    elif jog_ip == 'P':
        comp_ip = 'I'
    if soma % 2 == 0:
        par_imp = 'PAR'
    else:
        par_imp = 'ÍMPAR'
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} deu {par_imp}')
    print('—' * 60)
    vitoria = 'Você \033[1;32mVENCEU\033[m!\nVamos jogar novamente...'
    derrota = 'Você \033[1;31mPERDEU\033[m!'
    if jog_ip == 'P' and par_imp == 'PAR':
        resultado = True
        print(vitoria)
        print('=-' * 30 + '=')
        qtd_vit += 1
    elif jog_ip == 'I' and par_imp == 'ÍMPAR':
        resultado = True
        print(vitoria)
        print('=-' * 30 + '=')
        qtd_vit += 1
    else:
        print(derrota)
        print('=-' * 30 + '=')
        print(f'\033[41mGAME OVER\033[m! Você venceu {qtd_vit} vezes.')
        break

#Correto! :D
#Outra maneira de fazer

'''
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
'''