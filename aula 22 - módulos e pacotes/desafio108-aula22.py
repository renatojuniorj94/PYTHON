"""
Adapte o código do desafio 107, criando uma função
adicional chamada moeda() que consiga mostrar os valores
como um valor monetário formatado.
"""
from ex107 import moedas
preço = float(input('Digite o preço: '))
print(f'A metade de {preço} é {moedas.metade(preço)}')
print(f'O dobro de {preço} é {moedas.dobra(preço)}')
print(f'Aumentando 10% temos {moedas.aumentar(preço)}')
print(f'Reduzindo 13% temos {moedas.diminuir(preço)}')