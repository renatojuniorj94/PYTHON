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
    if idade < 16:
        print('Não pode votar')
    elif idade < 18:
        print('Voto opcional')
    elif idade >= 18 or idade < 63:
        print('Voto obrigatório!')
    elif idade >= 63:
        print('Não precisa votar')


voto()
print(idade)