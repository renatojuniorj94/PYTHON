'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada
um dos dígitos separados.
Ex:
Digite um número: 1834
Unidade: 4
Dezena: 3
centena: 8
milhar: 1
'''
'''
num = float(input('Digite um número de 0 a 9999: '))
print('Dezena: {}'.format(num[-1]))
print('Dezena: {}'.format(num[-2]))
print('Centena: {}'.format(num[-3]))
print('Milhar: {}'.format(num[-4]))
'''

#Errado! :(

#Maneira correta de fazer:
num = int(input('Informe um número de 0 a 9999: '))
n = str(num)
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))

#Outra maneira(melhor ainda):
print('_______________________\n')
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))