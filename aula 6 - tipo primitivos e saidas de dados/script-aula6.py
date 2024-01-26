# int > É um tipo primitivo, que transforma uma string em número.
"""
Todos os tipos primitivos:
int > Números inteiros (Ex: 7, -4, 0, 9875)
float > Números reais(com pontos flutuantes) (Ex: 4.5, 0.076, -15.223, 7.0)
bool > Lógicos(booleanos) (Ex: True, False)
str > Strings(Frases, palavras...) (Ex: 'Olá, mundo!', '7.5')
"""
#Para exibir o tipo primitivo usamos 'type'
#Ex: print(type(n1))

"""
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
s = n1 + n2
print('A soma vale', s)
#Outra forma de exibir o print:
print('A soma vale {}'.format(s)) # {} > Nós chamamos de máscara.
print(type(s))
"""

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
s = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))