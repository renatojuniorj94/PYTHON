"""
Crie um programa que leia um número real qualquer pelo teclado
e mostre na tela a sua porção inteira.
Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira de 6.
"""

import math
num = float(input('Digite um número real: '))
print('O número {} tem a parte inteira de {}'.format(num, math.floor(num)))

#Ou

from math import floor
print('O número {} tem a parte inteira de {}'.format(num, floor(num)))