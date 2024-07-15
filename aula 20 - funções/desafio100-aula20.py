"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores PARES sorteados pela função anterior.
"""
from random import randint
números = [
    randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
]


def sorteia():
    print(f'Sorteando {len(números)} valores da lista: ', end='')
    for num in números:
        print(num, end=' ')
    print('PRONTO!')


def somaPar():
    par = 0
    for num in números:
        if num % 2 == 0:
            par += num
    print(f'Somando os valores pares de {números}, temos {par}')


sorteia()
somaPar()