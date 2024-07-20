"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
O primeiro que indique o número a calcular e o outro chamado show, que será um valor
lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""
from math import factorial


def fatorial(fat):
    """
    :param fat: Recebe o número a ser calculado.
    :return: Retorna o fatorial do param fat.
    """
    show = bool
    resultado = 1
    count = 1
    while count <= fat:
        resultado *= count
        count += 1
    while fat > 1:
        print(f'{fat}', end=' x ')
        fat -= 1
    print('1 = ', end='')
    print(resultado)


fatorial(5)

#Maneira correta...


def fatorial(n, show=False):
    """
    —> Calcula o fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#print(fatorial(5, show=True))
help(fatorial)