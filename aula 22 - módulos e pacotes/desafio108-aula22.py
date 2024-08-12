"""
Adapte o código do desafio 107, criando uma função
adicional chamada moeda() que consiga mostrar os valores
como um valor monetário formatado.
"""
from ex108 import moedas
preço = float(input('Digite o preço: '))
print(f'A metade de {moedas.moeda(preço)} é {moedas.moeda(moedas.metade(preço))}')
print(f'O dobro de {moedas.moeda(preço)} é {moedas.moeda(moedas.dobra(preço))}')
print(f'Aumentando 10% temos {moedas.moeda(moedas.aumentar(preço, 10))}')
print(f'Reduzindo 13% temos {moedas.moeda(moedas.diminuir(preço, 13))}')