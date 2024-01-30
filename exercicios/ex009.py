#Faça um programa que leia um número
#inteiro qualquer e mostre na tela a sua tabuada.

t = int(input('Digite um número inteiro: '))
print('A tabuada de {} é:'.format(t))
print('_____________')
print('{} x  1 = {}'.format(t, t*1))
print('{} x  2 = {}'.format(t, t*2))
print('{} x  3 = {}'.format(t, t*3))
print('{} x  4 = {}'.format(t, t*4))
print('{} x  5 = {}'.format(t, t*5))
print('{} x  6 = {}'.format(t, t*6))
print('{} x  7 = {}'.format(t, t*7))
print('{} x  8 = {}'.format(t, t*8))
print('{} x  9 = {}'.format(t, t*9))
print('{} x 10 = {}'.format(t, t*10))
print('_____________\n')

#Correto
#Outra maneira de fazer

print('_' * 12)
#{:2} > Estamos separando 2 dígitos.
print('{} x {:2} = {}'.format(t, 1, t*1))
print('{} x {:2} = {}'.format(t, 2, t*2))
print('{} x {:2} = {}'.format(t, 3, t*3))
print('{} x {:2} = {}'.format(t, 4, t*4))
print('{} x {:2} = {}'.format(t, 5, t*5))
print('{} x {:2} = {}'.format(t, 6, t*6))
print('{} x {:2} = {}'.format(t, 7, t*7))
print('{} x {:2} = {}'.format(t, 8, t*8))
print('{} x {:2} = {}'.format(t, 9, t*9))
print('{} x {} = {}'.format(t, 10, t*10))
print('_' * 12)