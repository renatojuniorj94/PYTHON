"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas
posições na tabela
"""
num = []
for c in range(0, 5):
    num.append(int(input('Digite um número: ')))
print(f'O maior valor digitado foi {max(num)} e menor valor digitado foi {min(num)}')
for c, v in enumerate(num):
    print(f'Na posição {c} encontrei o valor {v}!')

