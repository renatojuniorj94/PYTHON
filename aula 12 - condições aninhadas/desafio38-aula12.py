'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print('O primeiro número é maior.')
elif n2 > n1:
    print('O segundo número é maior.')
elif n1 == n2:  # Aqui podemos usar else
    print('Não existe valor maior, os dois são iguais.')

# Correto! :D
