"""
Crie um programa que tenha uma função voto() que vai receber como parâmetro o ano
de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem
voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""
from datetime import date


def voto():
    global idade
    anoNasc = int(input('Ano de nascimento: '))
    idade = date.today().year - anoNasc
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        print('NÃO PODE VOTAR.')
    elif idade < 18:
        print('VOTO OPCIONAL.')
    elif idade < 63:
        print('VOTO OBRIGATÓRIO.')
    else:
        print('NÃO PRECISAR VOTAR')


voto()