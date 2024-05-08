'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor
que estão na tupla.
'''

from random import randint
maior = menor = cont = 0
tupla = ()
for c in range(1, 6):
    sort = randint(0, 10)
    tupla += sort,
    cont += 1
    if sort > maior:
        maior = sort

    if cont == 1:
        menor = sort
    if sort < menor:
        menor = sort
print('Os números sorteados foram:', tupla[0], tupla[1], tupla[2], tupla[3], tupla[4])
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')