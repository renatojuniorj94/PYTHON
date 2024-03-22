"""
Crie um programa que leia um número real qualquer pelo teclado
e mostre na tela a sua porção inteira.
Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira de 6.
"""

import math
num = float(input('Digite um número real: '))
print('O número {} tem a parte inteira de {}'.format(num, math.trunc(num)))#Ou math.trunc

#Ou

from math import floor
print('O número {} tem a parte inteira de {}'.format(num, floor(num)))

#Correto! Mas o método correto é usar trunc.

#Podemos usar também int(num), sem precisar importar a biblioteca math.

print('O número {} tem a parte inteira de {}'.format(num, int(num)))