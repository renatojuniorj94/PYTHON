"""
Faça um programa que leia o comprimento do cateto oposto e do cateto
adjacente de um triângulo retângulo, calcule e
mostre o comprimento da hipotenusa.
"""

cop = float(input('Digite o cateto oposto: '))
cad = float(input('Digite o cateto adjacente: '))
pot = (cop ** 2) + (cad ** 2)
hipotenusa = pow(pot, (1/2))
print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))

#Correto!

#Outra maneira de calcular a hipotenusa.
hi = (cop ** 2 + cad ** 2) ** (1/2)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))

#Usando biblioteca math

import math
hip = math.hypot(cop, cad)
print('O comprimento da hipotenusa é {:.2f}'.format(hip))