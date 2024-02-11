'''
Faça um programa que leia três números e mostre qual é o maior
e qual é o menor.
'''
print('Digite 3 números')
a1 = float(input('Número 1: '))
a2 = float(input('Número 2: '))
a3 = float(input('Número 3: '))
maior = max(a1, a2, a3)
menor = min(a1, a2, a3)
print('O maior número da lista é {} e o menor número é {}'.format(maior, menor))
