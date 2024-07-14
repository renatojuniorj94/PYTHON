"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep


def maior(*num):
    bigger = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.5)
        if valor > bigger:
            bigger = valor
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {bigger}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

#Correto! :D
#Outra maneira de fazer...


def maior(* num):
    cont = bigger = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            bigger = valor
        else:
            if valor > bigger:
                bigger = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {bigger}.')