"""
for c in range(1, 6):
    print(c)
print('FIM')
"""

#Contando de trás para frente:
for c in range(6, 0, -1):
    print(c)
print('Fim\n')

#Pulando números:
for p in range(0, 11, 2):
    print(p)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    # Versão extensa: s = s + n
    s += n
print('O somatório de todos os valores foi {}'.format(s))
