'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex:
5! = 5 x 4 x 3 x 2 x 1 = 120
(Fazer esse desafio com while e com for)
'''
'''n = int(input('Digite um número: '))
c = n
fat = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fat *= c
    c -= 1
print('{}'.format(fat))'''

#Usando for
from math import factorial
n = int(input('Digite um número: '))
fat = n
for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c *= n
print(factorial(n))
