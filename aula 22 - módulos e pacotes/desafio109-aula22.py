"""
Modifique as funções que foram criadas no desafio 107
para que elas aceitem um parâmetro a mais, informando se o valor
retornado por elas vai ser ou não formatado pela função moeda(),
desenvolvida no desafio 108.
"""
from ex109 import ex109
preço = float(input('Digite o preço: '))
print(f'A metade de {ex109.moeda(preço)} é {ex109.moeda(ex109.metade(preço))}')
print(f'O dobro de {ex109.moeda(preço)} é {ex109.moeda(ex109.dobra(preço))}')
print(f'Aumentando 10% temos {ex109.moeda(ex109.aumentar(preço))}')
print(f'Reduzindo 13% temos {ex109.moeda(ex109.diminuir(preço))}')