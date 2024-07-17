"""
Crie um programa que tenha uma função voto() que vai receber como parâmetro o ano
de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem
voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""


def voto(nasc):
    nasc = int(input('Ano de nascimento: '))
    if nasc < 16:
        print('Não pode votar')
    elif nasc == 17:
        print('Voto opcional')
    elif 18 <= nasc < 63:
        print('Voto obrigatório!')
    else:
        print('Voto opcional')


voto()