#Tuplas são IMUTÁVEIS.
#Para mudar algum item em uma tupla, temos que parar o programa o modificar o item na criação da variável.

lanche = ('hambúrguer', 'suco', 'pizza', 'pudim')
#Acima temos uma variável composta. Nas versões atuais não é necessário usar parenteses '()'

'''print(lanche)
print(lanche[1:])
print(lanche[:2])
print(lanche[-2:])
for c in lanche:
    print(c)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Ufa, comi pra caramba!')

for cont in range(0, len(lanche)):
    print(lanche[cont])
'''
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

#Colocando em ordem alfabética
print(sorted(lanche))

#Unificando Tuplas, nessa caso a tupla 'a' vem primeiro.
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = (b + a)
print(c)
#Quantos números tem na variável 'c'
print(len(c))
#Contando quando vezes aparece o número '5'
print(c.count(5))
#Mostrando a posição de um determinado número ou item na tupla
#Como tem mais de 1 número '5', nós colocamos para verificar o próximo número '5' na tupla
print(c.index(5, 1))
#Nas tuplas também podemos adicionar strings(str), números inteiros(int) e flutuantes(float)
pessoa = ('Renato', 30, 'M', 1.76)
#Deletando uma variável
del pessoa
print(pessoa)

