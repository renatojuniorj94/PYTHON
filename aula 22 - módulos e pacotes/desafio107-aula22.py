"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobra() e metade().
Faça também um programa que importe esse módulo e
use alguma dessas funções.
"""
from ex107 import moedas
"""p = float(input('Digite o preço: '))
print(f'A metade de {p} é {moedas.metade(p)}')
print(f'O dobro de {p} é {moedas.dobra(p)}')
print(f'Aumentando 10% temos {moedas.aumentar(p)}')
print(f'Reduzindo 13% temos {moedas.diminuir(p)}')
"""
#Correto! :D
#Outra maneira de fazer...

p = float(input('Digite o preço: '))
print(f'A metade de {p} é {moedas.metade(p)}')
print(f'O dobro de {p} é {moedas.dobra(p)}')
print(f'Aumentando 10% temos {moedas.aumentar(p, 10)}')
print(f'Reduzindo 13% temos {moedas.diminuir(p, 13)}')