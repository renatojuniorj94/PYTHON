"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from random import randint
mini = randint(1, 100)
maxi = randint(1, 100)


def maior(*num):
    tamanho = len(num)
    print('-=' * 30)
    print('Analisando os valores passados...')
    print(f'{num} foram informados {tamanho} valores ao todo.')
    print(f'O maior valor informado foi .')


maior(mini, maxi)