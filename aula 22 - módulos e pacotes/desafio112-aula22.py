"""
Dentro do pacote utilidadesCeV que criamos no desafio 111,
temos um módulo chamado dado. Crie uma função chamada
leiaDinheiro() que seja capaz de funcionar como a função
input(), mas como uma validação de dados para aceitar apenas
valores que sejam monetários.
"""
from ex112.utilidadescev import dado
p = dado.leiaDinheiro('Digite: ')
#print(f'O resultado foi {p}')
dado.resumo(p, 35, 22)