"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobra() e metade().
Faça também um programa que importe esse módulo e
use alguma dessas funções.
"""
from ex107 import moedas
preço = float(input('Digite o preço: '))
print(f'A metade de {preço} é {moedas.metade(preço)}')
print(f'O dobro de {preço} é {moedas.dobra(preço)}')
print(f'Aumentando 10% temos {moedas.aumentar(preço)}')
print(f'Reduzindo 13% temos {moedas.diminuir(preço)}')