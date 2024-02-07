"""
Faça um programa que leia um ângulo qualquer e mostre na tela
o valor do seno, cosseno e tangente desse ângulo.
"""
#https://docs.python.org/3/library/math.html
from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tan = tan((radians(ang)))
print('O ângulo de {0} tem o SENO de {1:.2f}\n'
      'O ângulo de {0} tem o COSSENO de {2:.2f}\n'
      'O ângulo de {0} tem a TANGENTE de {3:.2f}'.format(ang, seno, cos, tan))