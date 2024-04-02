'''
Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética.
No final, mostre os 10 primeiros termos dessa progressão.
'''

t = int(input('Digite o termo: '))
r = int(input('Digite a razão: '))

for c in range(t, 1000, r):
    print(c)