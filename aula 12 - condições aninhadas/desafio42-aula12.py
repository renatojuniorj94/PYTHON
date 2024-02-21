'''
Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo
de triângulo será formado:
-Equilátero: Todos os lados iguais
-Isósceles: Dois lados iguais
-Escaleno: Todos os lados diferentes
'''

r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR triângulo!')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triângulos!')

if r1 == r2 == r3:
    print('Nós temos um triângulo equilátero.')
elif r1 == r2 != r3 or r1 != r2 == r3 or r1 == r3 != r2:
    print('Nós temos um triângulo isósceles.')
elif r1 != r2 != r3:
    print('Nós temos um triângulo escaleno.')