"""
Crie um programa que tenha uma função voto() que vai receber como parâmetro o ano
de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem
voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""
"""from datetime import date


def voto():
    global idade
    anoNasc = int(input('Ano de nascimento: '))
    idade = date.today().year - anoNasc
    if idade == 1:
        print(f'Com {idade} ano: ', end='')
    else:
        print(f'Com {idade} anos: ', end='')
    if idade < 16:
        print('NÃO PODE VOTAR.')
    elif idade < 18:
        print('VOTO OPCIONAL.')
    elif idade < 63:
        print('VOTO OBRIGATÓRIO.')
    else:
        print('NÃO PRECISAR VOTAR')


voto()"""

#Correto! :D
#Outra maneira de fazer...


def voto(ano):
    from datetime import date  # Escopo de função
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))