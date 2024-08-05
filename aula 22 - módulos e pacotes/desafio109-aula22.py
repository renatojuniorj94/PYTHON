"""
Modifique as funções que foram criadas no desafio 107
para que elas aceitem um parâmetro a mais, informando se o valor
retornado por elas vai ser ou não formatado pela função moeda(),
desenvolvida no desafio 108.
"""
from ex107 import moedas
preço = float(input('Digite o preço: '))
print(f'A metade de {moedas.moeda(preço)} é {moedas.moeda(moedas.metade(preço))}')
print(f'O dobro de {moedas.moeda(preço)} é {moedas.moeda(moedas.dobra(preço))}')
print(f'Aumentando 10% temos {moedas.moeda(moedas.aumentar(preço))}')
print(f'Reduzindo 13% temos {moedas.moeda(moedas.diminuir(preço))}')