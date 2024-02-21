'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal
'''

numero = int(input('Digite um número inteiro: '))
print('1 - Binário\n'
      '2 - Octal\n'
      '3 - Hexadecimal')
base = int(input('Escolha a base de conversão: '))

if base == 1:
    print('Você escolheu binário como base.')
elif base == 2:
    print('Você escolheu Octal como base.')
elif base == 3:
    print('Você escolheu Hexadecimal como base.')
else:
    print('\033[1;31mErro!\033[m Número inválido!')