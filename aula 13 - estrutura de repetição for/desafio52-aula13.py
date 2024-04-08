'''
Faça um programa que leia um número inteiro e diga se ele é ou não
um número primo.
'''

num = int(input('Digite um número inteiro: '))

total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} \033[m'.format(c), end='')

print('\nO número {} foi divisível {} vezes.'.format(num, total))

if total == 2:
    print('Ele é um número \033[33mPRIMO!')
else:
    print('Ele \033[31mNÃO\033[m é um número primo!')