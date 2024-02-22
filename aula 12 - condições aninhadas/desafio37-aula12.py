'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal
'''

numero = int(input('Digite um número inteiro: '))
print('''1 - Binário
2 - Octal
3 - Hexadecimal''')
opção = int(input('Escolha a base de conversão: '))

if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(numero, bin(numero) [2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual {}.'.format(numero, oct(numero) [2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(numero, hex(numero) [2:]))
else:
    print('\033[1;31mErro!\033[m Número inválido!')

# Correto! :D