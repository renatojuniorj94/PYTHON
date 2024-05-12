#Listas são MUTÁVEIS
lanche = ['hamburger', 'suco', 'pizza', 'pudim']
print(lanche)
print(len(lanche))

#Substituindo item
lanche[3] = 'sorvete'
print(lanche)

#Adicionando itens no final de uma lista
lanche.append('biscoito')
print(lanche)

#Adicionando em uma determinada posição ou entre dois itens
lanche.insert(0, 'cachorro-quente')
print(lanche)

#Três maneiras de eliminar itens de uma lista
del lanche[3]
lanche.pop(3)
lanche.remove('biscoito')
print(lanche)

#Removendo item somente se ele estiver na lista. Se não estiver, não apresenta erro no console
if 'pizza' in lanche:
    lanche.remove('pizza')
else:
    print('Não achei pizza na lista')

#Declarando lista com range
valores = list(range(4, 11))
print(valores)

#Ordenando números em ordem crescente
desordenados = [8, 2, 5, 4, 9, 3, 0]
desordenados.sort()
print(desordenados)

#Colocando em ordem decrescente
desordenados.sort(reverse=True)
print(desordenados)

valores = list()
'''valores.append(5)
valores.append(9)
valores.append(4)'''
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
#b = a
#Criamos uma ligação entre as listas acima
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')