'''
Faça um programa que leia três números e mostre qual é o maior
e qual é o menor.
'''
print('Digite 3 números')
a = float(input('Número 1: '))
b = float(input('Número 2: '))
c = float(input('Número 3: '))
maior = max(a, b, c)
menor = min(a, b, c)
print('O maior número da lista é {} e o menor número é {}'.format(maior, menor))

#Outras maneiras de fazer...

'''
if a < b and a < c:
    menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor é {}'.format(menor))

if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor é {}'.format(maior))
'''


'''
#Outra maneira...
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
'''

#Outra maneira...
'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite um último número: '))
l = [n1, n2, n3]
l.sort()
print(f'O maior número é {l[2]} e o menor é {l[0]}')
'''
