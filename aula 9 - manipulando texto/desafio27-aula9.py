'''
Faça um programa que leia o nome completo de uma pessoa , mostrando em seguida
o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
Último = Souza
'''

nome = str(input('Digite seu nome completo: '))
split = nome.split()
print('Primeiro nome = {}\n'
      'Último nome = {}'.format(split[0], split[:]))