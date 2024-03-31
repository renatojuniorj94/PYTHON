'''
Desenvolva um programa que leia seis números inteiros e mostre apenas daqueles
que forem pares. Se o valor digitado for ímpar, desconsidero-o.
'''

qtd = 0
for c in range(0, 6):
    n = int(input('Digite um número inteiro: '))
if n % 2 == 0:
    qtd += 1
print('Você digitou {} números pares.'.format(n))