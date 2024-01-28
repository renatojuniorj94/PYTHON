#Aula - Operadores aritméticos
"""
+ adição
- subtração
* multiplicação
/ divisão
** potência
// divisão inteira
% resto da divisão
"""

"""
Ordem de precedência:
1 ()
2 potência **
3 multiplicação*, divisão /, divisão inteira //, resto da divisão %
4 adição +, subtração -
"""
"""Para fazer a raíz quadrada, exemplo:
81**(1/2) == 9.0

Para fazer a raíz cúbica, exemplo:
127**(1/3) == 5.026525695313479
"""

"""
#Opções de formatações:
nome = input('Digite seu nome: ')
#Exibe o format em um espaço de 20 caracteres
print('Prazer em te conhecer {:20}!'.format(nome))
#Alinhando o nome a direita
print('Prazer em te conhecer {:>20}!'.format(nome))
#Alinhando o nome a esquerda
print('Prazer em te conhecer {:<20}!'.format(nome))
#Alinhando nome ao centro
print('Prazer em te conhecer {:^20}!'.format(nome))
#Completando os espaços em branco com algum caractere
print('Prazer em te conhecer {:=^20}!'.format(nome))
"""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \no produto é {} \ne a divisão é {:.3f}'.format(s, m, d), end=' ')
# {:.3f} > Acima definimos que serão exibidos 3 números flutuantes no print.
#end='' > Não faz a quebra de linha.
#\n > Para fazer a quebra de linha.
print('Divisão inteira {} e potência {}'.format(di, e))
