'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
Último = Souza
'''

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!\n'
      'Primeiro nome = {}\n'
      'Último nome = {}'.format(nome[0], nome[-1]))

#Correto! :D

#Outra maneira

print('Ultimo nome = {}'.format(nome[len(nome)-1]))